'''
Created on 15 Dec 2018

@author: simon
'''
from enum import Enum

class TypeDefType(Enum):
    CLASS = 0
    TYPE = 1


class TypeDef(object):
    
    _package = None
    _name = None
    _type = None
    
    def __init__(self, **kw):
        self._name = kw.get('name', self._name)
        self._package = kw.get('package', self._package)
        self._type = kw.get('type', self._type)
        
    def get_members(self):
        return []

class ClassDef(TypeDef):
    
    _extendsClass = None
    _attributes = None
    _methods = None
    
    def __init__(self, **kw):
        kw['type'] = TypeDefType.CLASS
        TypeDef.__init__(self, **kw)
        self._extendsClass = kw.get('extendsClass', self._extendsClass)
        self._attributes = kw.get('attributes', self._attributes)
        self._methods = kw.get('methods', self._methods)
        
        if self._attributes:
            for attribute in self._attributes:
                attribute.parent(self)
        
        if self._methods:    
            for method in self._methods:
                method.parent(self)
        
    def get_members(self):
        members = []
        if self._attributes != None:
            members = members + self._attributes
        if self._methods != None:
            members = members + self._methods
        return members
    
    def get_fields(self):
        return self._attributes if self._attributes is not None else []
    
    def get_methods(self):
        return self._methods if self._methods is not None else []
   
   
class EnumDef(TypeDef):
    
    _fields = None
    
    def __init__(self, **kw):
        kw['type'] = TypeDefType.TYPE
        TypeDef.__init__(self, **kw)
        self._fields = kw.get('fields', self._fields)
        
        if self._fields:
            for field in self._fields:
                field.parent(self)

        
    def get_members(self):
        return self._fields if self._fields is not None else []
        
    def get_fields(self):
        return self._fields if self._fields is not None else []
    
        
class MemberDefType(Enum):
    FIELD = 0
    METHOD = 1
    
    
class MemberDef(object):
    
    _memberOfType = None
    _name = None
    _type = None
    
    def __init__(self, **kw):
        self._memberOfType = kw.get('memberOfType', self._memberOfType)
        self._name = kw.get('name', self._name)
        self._type = kw.get('type', self._type)
        
    def parent(self, *args):
        if len(args) > 0:
            self._memberOfType = args[0]
        return self._memberOfType
        
        
class FieldDefType(Enum):
    ATTRIBUTE = 0
    EXPRESSION = 1
    LITERAL = 2
    LIST = 3
    
    
class FieldDef(MemberDef):
    
    _dataType = None
    _fieldType = None
    
    def __init__(self, **kw):
        kw['type'] = MemberDefType.FIELD
        MemberDef.__init__(self, **kw)
        self._dataType = kw.get('dataType', self._dataType)
        self._fieldType = kw.get('fieldType', self._fieldType)
        
class AttributeDef(FieldDef):
    
    _initialValue = None
    
    def __init__(self, **kw):
        kw['fieldType'] = FieldDefType.ATTRIBUTE
        FieldDef.__init__(self, **kw)
        self._initialValue = kw.get('initialValue', self._initialValue)
            
        
class ExpressionDef(FieldDef):
    
    def __init__(self, **kw):
        kw['fieldType'] = FieldDefType.EXPRESSION
        FieldDef.__init__(self, **kw)
            
        
class LiteralDef(FieldDef):
    
    _value = None
    
    def __init__(self, **kw):
        kw['fieldType'] = FieldDefType.LITERAL
        FieldDef.__init__(self, **kw)
        self._value = kw.get('value', self._value)
            
        
class ListDef(FieldDef):
    
    def __init__(self, **kw):
        kw['fieldType'] = FieldDefType.LIST
        FieldDef.__init__(self, **kw)
            
      
class MethodDef(MemberDef):
    
    _returnType = None
    
    def __init__(self, **kw):  
        kw['type'] = MemberDefType.METHOD
        MemberDef.__init__(self, **kw)
        self._returnType = kw.get('returnType', self._returnType)
    