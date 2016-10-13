#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class EntityMetadata(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'associationClass': 'bool',
            
            
            'description': 'str',
            
            
            'type': 'Class',
            
            
            'version': 'str',
            
            
            'stereotypes': 'list[AbstractStereotype]'
            
        }

        self.attributeMap = {
            
            'associationClass': 'associationClass',
            
            'description': 'description',
            
            'type': 'type',
            
            'version': 'version',
            
            'stereotypes': 'stereotypes'
            
        }       

        
        
        self.associationClass = None # bool
        
        
        self.description = None # str
        
        
        self.type = None # Class
        
        
        self.version = None # str
        
        
        self.stereotypes = None # list[AbstractStereotype]
        
