#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TopologyApplicationDto(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'description': 'str',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'description': 'description',
            
            'name': 'name'
            
        }       

        
        #Unique identifier for this Application
        
        self.id = None # str
        
        #Description for this Application
        
        self.description = None # str
        
        #Name for this Application
        
        self.name = None # str
        
