#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PropertyMetadata(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'attribute': 'bool',
            
            
            'name': 'str',
            
            
            'ordered': 'bool',
            
            
            'collection': 'bool',
            
            
            'collectionInterfaceType': 'Class«object»',
            
            
            'unique': 'bool',
            
            
            'maxCardinality': 'int',
            
            
            'associationEnd': 'bool',
            
            
            'collectionImplType': 'Class«object»',
            
            
            'minCardinality': 'int',
            
            
            'description': 'str',
            
            
            'type': 'Class',
            
            
            'version': 'str',
            
            
            'stereotypes': 'list[AbstractStereotype]'
            
        }

        self.attributeMap = {
            
            'attribute': 'attribute',
            
            'name': 'name',
            
            'ordered': 'ordered',
            
            'collection': 'collection',
            
            'collectionInterfaceType': 'collectionInterfaceType',
            
            'unique': 'unique',
            
            'maxCardinality': 'maxCardinality',
            
            'associationEnd': 'associationEnd',
            
            'collectionImplType': 'collectionImplType',
            
            'minCardinality': 'minCardinality',
            
            'description': 'description',
            
            'type': 'type',
            
            'version': 'version',
            
            'stereotypes': 'stereotypes'
            
        }       

        
        
        self.attribute = None # bool
        
        
        self.name = None # str
        
        
        self.ordered = None # bool
        
        
        self.collection = None # bool
        
        
        self.collectionInterfaceType = None # Class«object»
        
        
        self.unique = None # bool
        
        
        self.maxCardinality = None # int
        
        
        self.associationEnd = None # bool
        
        
        self.collectionImplType = None # Class«object»
        
        
        self.minCardinality = None # int
        
        
        self.description = None # str
        
        
        self.type = None # Class
        
        
        self.version = None # str
        
        
        self.stereotypes = None # list[AbstractStereotype]
        
