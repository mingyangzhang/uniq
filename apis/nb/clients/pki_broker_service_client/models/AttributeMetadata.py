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
            
            
            'defaultValue': 'object',
            
            
            'required': 'bool',
            
            
            'collectionInterfaceType': 'Class«object»',
            
            
            'associationEnd': 'bool',
            
            
            'collectionImplType': 'Class«object»',
            
            
            'name': 'str',
            
            
            'ordered': 'bool',
            
            
            'collection': 'bool',
            
            
            'unique': 'bool',
            
            
            'maxCardinality': 'int',
            
            
            'minCardinality': 'int',
            
            
            'description': 'str',
            
            
            'type': 'Class',
            
            
            'version': 'str',
            
            
            'stereotypes': 'list[AbstractStereotype]'
            
        }

        self.attributeMap = {
            
            'attribute': 'attribute',
            
            'defaultValue': 'defaultValue',
            
            'required': 'required',
            
            'collectionInterfaceType': 'collectionInterfaceType',
            
            'associationEnd': 'associationEnd',
            
            'collectionImplType': 'collectionImplType',
            
            'name': 'name',
            
            'ordered': 'ordered',
            
            'collection': 'collection',
            
            'unique': 'unique',
            
            'maxCardinality': 'maxCardinality',
            
            'minCardinality': 'minCardinality',
            
            'description': 'description',
            
            'type': 'type',
            
            'version': 'version',
            
            'stereotypes': 'stereotypes'
            
        }       

        
        
        self.attribute = None # bool
        
        
        self.defaultValue = None # object
        
        
        self.required = None # bool
        
        
        self.collectionInterfaceType = None # Class«object»
        
        
        self.associationEnd = None # bool
        
        
        self.collectionImplType = None # Class«object»
        
        
        self.name = None # str
        
        
        self.ordered = None # bool
        
        
        self.collection = None # bool
        
        
        self.unique = None # bool
        
        
        self.maxCardinality = None # int
        
        
        self.minCardinality = None # int
        
        
        self.description = None # str
        
        
        self.type = None # Class
        
        
        self.version = None # str
        
        
        self.stereotypes = None # list[AbstractStereotype]
        
