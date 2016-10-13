#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AttributeMetadata(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'attribute': 'bool',
            
            
            'required': 'bool',
            
            
            'collectionInterfaceType': 'Class«object»',
            
            
            'associationEnd': 'bool',
            
            
            'collectionImplType': 'Class«object»',
            
            
            'defaultValue': 'dict',
            
            
            'ordered': 'bool',
            
            
            'collection': 'bool',
            
            
            'maxCardinality': 'int',
            
            
            'minCardinality': 'int',
            
            
            'unique': 'bool',
            
            
            'name': 'str',
            
            
            'description': 'str',
            
            
            'version': 'str',
            
            
            'stereotypes': 'list[AbstractStereotype]',
            
            
            'type': 'Class'
            
        }

        self.attributeMap = {
            
            'attribute': 'attribute',
            
            'required': 'required',
            
            'collectionInterfaceType': 'collectionInterfaceType',
            
            'associationEnd': 'associationEnd',
            
            'collectionImplType': 'collectionImplType',
            
            'defaultValue': 'defaultValue',
            
            'ordered': 'ordered',
            
            'collection': 'collection',
            
            'maxCardinality': 'maxCardinality',
            
            'minCardinality': 'minCardinality',
            
            'unique': 'unique',
            
            'name': 'name',
            
            'description': 'description',
            
            'version': 'version',
            
            'stereotypes': 'stereotypes',
            
            'type': 'type'
            
        }       

        
        
        self.attribute = None # bool
        
        
        self.required = None # bool
        
        
        self.collectionInterfaceType = None # Class«object»
        
        
        self.associationEnd = None # bool
        
        
        self.collectionImplType = None # Class«object»
        
        
        self.defaultValue = None # dict
        
        
        self.ordered = None # bool
        
        
        self.collection = None # bool
        
        
        self.maxCardinality = None # int
        
        
        self.minCardinality = None # int
        
        
        self.unique = None # bool
        
        
        self.name = None # str
        
        
        self.description = None # str
        
        
        self.version = None # str
        
        
        self.stereotypes = None # list[AbstractStereotype]
        
        
        self.type = None # Class
        
