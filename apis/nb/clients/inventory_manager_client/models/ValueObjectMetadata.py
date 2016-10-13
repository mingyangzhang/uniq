#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ValueObjectMetadata(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'version': 'str',
            
            
            'description': 'str',
            
            
            'type': 'Class',
            
            
            'stereotypes': 'list[AbstractStereotype]'
            
        }

        self.attributeMap = {
            
            'version': 'version',
            
            'description': 'description',
            
            'type': 'type',
            
            'stereotypes': 'stereotypes'
            
        }       

        
        
        self.version = None # str
        
        
        self.description = None # str
        
        
        self.type = None # Class
        
        
        self.stereotypes = None # list[AbstractStereotype]
        
