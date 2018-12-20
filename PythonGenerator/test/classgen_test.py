'''
Created on 16 Dec 2018

@author: simon
'''
import unittest, os
from pygen import model
from pygen.classgen import Generator


class StringWriter(object):
    _buff = ''
    
    def write(self, chars):
        self._buff = self._buff + chars
        
    def flush(self):
        pass
        
    def __str__(self, *args, **kwargs):
        return self._buff


class ClassGenTest(unittest.TestCase):


    def testNewClassGen(self):
        sw = StringWriter()
        gen = Generator(writer=sw)
        
        assert gen._indentStr == ''
        assert gen._depth == 0
        assert gen._indentStep == '  '

        gen = Generator(
            writer=sw, 
            indent='    ', 
            depth=2)
        
        assert gen._indentStr == '        '
        assert gen._depth == 2
        assert gen._indentStep == '    '

    def testIndentOutdent(self):
        sw = StringWriter()
        gen = Generator(writer=sw)
        
        assert gen._indentStr == ''
        assert gen._depth == 0
        assert gen._indentStep == '  '
        
        gen._indent()
        assert gen._indentStr == '  '
        assert gen._depth == 1
        
        gen._indent()
        assert gen._indentStr == '    '
        assert gen._depth == 2
        
        gen._outdent()
        assert gen._indentStr == '  '
        assert gen._depth == 1
        
        gen._outdent()
        assert gen._indentStr == ''
        assert gen._depth == 0
        
        gen._outdent()
        assert gen._indentStr == ''
        assert gen._depth == 0
        
    def testWrite(self):
        sw = StringWriter()
        gen = Generator(writer=sw)
        
        gen._write('XXX')
        assert sw.__str__() == 'XXX'
        
        gen._write('YYY')
        assert sw.__str__() == 'XXXYYY'

    def testWriteIndent(self):
        sw = StringWriter()
        gen = Generator(writer=sw, depth=2)
        
        gen._write_indent()
        assert sw.__str__() == '    '

    def testWriteLine(self):
        sw = StringWriter()
        gen = Generator(writer=sw, depth=2)
        
        gen._write_line('XXX')
        assert sw.__str__() == '    XXX'+os.linesep

    def testWriteLinesep(self):
        sw = StringWriter()
        gen = Generator(writer=sw, depth=2)
        
        gen._write_linesep()
        assert sw.__str__() == os.linesep

    def testGenerate(self):
        sw = StringWriter()
        gen = Generator(writer=sw)
        
        baseClass = model.ClassDef(
            package='a.package',
            name='BaseClass')
        
        attrs = [
            model.AttributeDef(name='attrA'),
            model.AttributeDef(name='attrB')
        ]    
                
        cls = model.ClassDef(
            package='a.package',
            name='TypeA',
            extendsClass=baseClass,
            attributes=attrs)
        
        gen.generate(cls)
        
        expected =  'class TypeA(BaseClass):'+os.linesep+\
                    ''+os.linesep+\
                    '  _attrA = None'+os.linesep+\
                    '  _attrB = None'+os.linesep+\
                    ''+os.linesep+\
                    '  def __init__(self, **kw):'+os.linesep+\
                    "    self._attrA = kw.get('attrA', self._attrA)"+os.linesep+\
                    "    self._attrB = kw.get('attrB', self._attrB)"+os.linesep+\
                    ''
        
        assert sw.__str__() ==  expected
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()