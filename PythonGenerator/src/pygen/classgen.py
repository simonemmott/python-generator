'''
Created on 15 Dec 2018

@author: simon
'''
import os
import itertools

class AttributeGen(object):

    _generator = None
    
    def __init__(self, generator, **kw):
        self._generator = generator
        
    def _write_initial_def(self, attributeDef, **kw):
        default_value = 'None'
        self._generator._write_line('_%s = %s' % (attributeDef._name, default_value))
                               
    def _write_init(self, attributeDef, **kw):
        self._generator._write_line("self._%s = kw.get('%s', self._%s)" % (attributeDef._name, attributeDef._name, attributeDef._name))
                               

class Generator(object):
    
    _writer = None;
    _indentStep = '  '
    _depth = 0
    _indentStr = ''
    _attrGen = None
    
    def __init__(self, **kw):
        self._writer = kw.get('writer', self._writer)
        self._indentStep = kw.get('indent', self._indentStep)
        self._depth = kw.get('depth', self._depth)
        
        if not self._writer:
            raise ValueError("No writer supplied when creating Generator instant")
        
        for _ in itertools.repeat(None, self._depth):
            self._indentStr = self._indentStr + self._indentStep
            
        self._attrGen = AttributeGen(self)


    def generate(self, classDef, **kw):
        
        self._write_line('class %s(%s):' % (classDef._name, classDef._extendsClass._name if classDef._extendsClass else 'object'))
        
        self._write_linesep()
        self._indent()
        for attr in classDef._attributes:
            self._attrGen._write_initial_def(attr)
            
        self._generate_init(classDef)
        
        self._outdent()
        self._flush()
        
    def _generate_init(self, classDef):
        self._write_linesep()
        self._write_line('def __init__(self, **kw):')
        self._indent()
        for attr in classDef._attributes:
            self._attrGen._write_init(attr)
        self._outdent()
        

        
    
    def _indent(self):
        self._depth += 1
        self._indentStr = self._indentStr + self._indentStep
            
    def _outdent(self):
        if self._depth > 0:
            self._depth -= 1
            self._indentStr = self._indentStr[:-len(self._indentStep)]
            
    def _write_indent(self):
        self._writer.write(self._indentStr)        
    
    def _write(self, chars):
        self._writer.write(chars)
        
    def _write_line(self, chars):
        self._writer.write(self._indentStr+chars+os.linesep)
        
    def _write_linesep(self):
        self._writer.write(os.linesep)
        
    def _flush(self):
        self._writer.flush()
    
    
    