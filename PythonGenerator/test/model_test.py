'''
Created on 15 Dec 2018

@author: simon
'''
import unittest
from pygen import model


class TypeDefTest(unittest.TestCase):


    def testNewInstance(self):
        inst = model.TypeDef(
            package='a.package',
            name='TypeA',
            type=model.TypeDefType.CLASS)
        
        assert inst._package == 'a.package'
        assert inst._name == 'TypeA'
        assert inst._type == model.TypeDefType.CLASS
        
        assert len(inst.get_members()) == 0


class ClassDefTest(unittest.TestCase):


    def testNewInstance(self):
        
        baseClass = model.ClassDef(
            package='a.package',
            name='BaseClass')
        
        attrs = [
            model.AttributeDef(name='attrA'),
            model.AttributeDef(name='attrB')
        ]    
        
        methods = [
            model.MethodDef(name='methodA'),
            model.MethodDef(name='methodB')
        ]    
        
        inst = model.ClassDef(
            package='a.package',
            name='TypeA',
            extendsClass=baseClass,
            attributes=attrs,
            methods=methods)
        
        assert inst._package == 'a.package'
        assert inst._name == 'TypeA'
        assert inst._type == model.TypeDefType.CLASS
        assert inst._extendsClass == baseClass
        assert inst._attributes[0]._name == 'attrA'
        assert inst._attributes[1]._name == 'attrB'
        assert len(inst._attributes) == 2
        assert inst._methods[0]._name == 'methodA'
        assert inst._methods[1]._name == 'methodB'
        assert len(inst._methods) == 2
        assert len(inst.get_members()) == 4
        assert inst.get_members()[0]._name  == 'attrA'
        assert inst.get_members()[1]._name  == 'attrB'
        assert inst.get_members()[2]._name  == 'methodA'
        assert inst.get_members()[3]._name  == 'methodB'
        for member in inst.get_members():
            assert member.parent() == inst


class EnumDefTest(unittest.TestCase):


    def testNewInstance(self):

        fields = [
            model.AttributeDef(name='FIELD_A'),
            model.AttributeDef(name='FIELD_B')
        ]    

        inst = model.EnumDef(
            package='a.package',
            name='EnumA',
            fields=fields)
        
        assert inst._package == 'a.package'
        assert inst._name == 'EnumA'
        assert inst._type == model.TypeDefType.TYPE
        assert inst._fields[0]._name == 'FIELD_A'
        assert inst._fields[1]._name == 'FIELD_B'
        assert inst.get_fields()[0]._name == 'FIELD_A'
        assert inst.get_fields()[1]._name == 'FIELD_B'
        assert inst.get_members()[0]._name == 'FIELD_A'
        assert inst.get_members()[1]._name == 'FIELD_B'
        for member in inst.get_members():
            assert member.parent() == inst


class MemberDefTest(unittest.TestCase):


    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.MemberDef(
            memberOfType=cls,
            name='FieldA',
            type=model.MemberDefType.FIELD)
        
        assert inst._memberOfType == cls
        assert inst._name == 'FieldA'
        assert inst._type == model.MemberDefType.FIELD
           
    def testParent(self):

        cls = model.ClassDef(
            package='a.package',
            name='TypeA')
        cls1 = model.ClassDef(
            pacakge='a.package',
            name='TypeB'
        )
        
        inst = model.MemberDef(
            memberOfType=cls,
            name='FieldA',
            type=model.MemberDefType.FIELD)

        assert inst.parent() == cls
        
        inst.parent(cls1)
        assert inst.parent() == cls1


class FieldDefTest(unittest.TestCase):

    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='ClassA')
        typeA = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.FieldDef(
            memberOfType=cls,
            name='fieldA',
            dataType=typeA,
            fieldType=model.FieldDefType.ATTRIBUTE
        )
        
        assert inst._memberOfType == cls
        assert inst._name == 'fieldA'
        assert inst._type == model.MemberDefType.FIELD
        assert inst._dataType == typeA
        assert inst._fieldType == model.FieldDefType.ATTRIBUTE
        
        
class AttributeDefTest(unittest.TestCase):

    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='ClassA')
        typeA = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.AttributeDef(
            memberOfType=cls,
            name='fieldA',
            dataType=typeA
        )
        
        assert inst._memberOfType == cls
        assert inst._name == 'fieldA'
        assert inst._type == model.MemberDefType.FIELD
        assert inst._dataType == typeA
        assert inst._fieldType == model.FieldDefType.ATTRIBUTE
        
        
class ExpressionDefTest(unittest.TestCase):

    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='ClassA')
        typeA = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.ExpressionDef(
            memberOfType=cls,
            name='expressionA',
            dataType=typeA
        )
        
        assert inst._memberOfType == cls
        assert inst._name == 'expressionA'
        assert inst._type == model.MemberDefType.FIELD
        assert inst._dataType == typeA
        assert inst._fieldType == model.FieldDefType.EXPRESSION
        
        
class LiteralDefTest(unittest.TestCase):

    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='ClassA')
        typeA = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.LiteralDef(
            memberOfType=cls,
            name='LITERAL_A',
            dataType=typeA,
            value='Value'
        )
        
        assert inst._memberOfType == cls
        assert inst._name == 'LITERAL_A'
        assert inst._type == model.MemberDefType.FIELD
        assert inst._dataType == typeA
        assert inst._fieldType == model.FieldDefType.LITERAL
        assert inst._value == 'Value'
        
        
class ListDefTest(unittest.TestCase):

    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='ClassA')
        typeA = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.ListDef(
            memberOfType=cls,
            name='listA',
            dataType=typeA
        )
        
        assert inst._memberOfType == cls
        assert inst._name == 'listA'
        assert inst._type == model.MemberDefType.FIELD
        assert inst._dataType == typeA
        assert inst._fieldType == model.FieldDefType.LIST
        
        
class MethodDefTest(unittest.TestCase):

    def testNewInstance(self):
        
        cls = model.ClassDef(
            package='a.package',
            name='ClassA')
        typeA = model.ClassDef(
            package='a.package',
            name='TypeA')
        
        inst = model.MethodDef(
            memberOfType=cls,
            name='methodA',
            returnType=typeA
        )
        
        assert inst._memberOfType == cls
        assert inst._name == 'methodA'
        assert inst._type == model.MemberDefType.METHOD
        assert inst._returnType == typeA
        
        
if __name__ == "__main__":
    unittest.main()