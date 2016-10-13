#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NeighborhoodDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'listofScalableGroups': 'list[str]',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'type': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'listofScalableGroups': 'listofScalableGroups',
            
            'name': 'name',
            
            'id': 'id',
            
            'type': 'type'
            
        }       

        
        #Description of the group
        
        self.description = None # str
        
        #List of Scalable Groups
        
        self.listofScalableGroups = None # list[str]
        
        #Neighborhood Name
        
        self.name = None # str
        
        #UUID of the Neighborhood
        
        self.id = None # str
        
        #Isolation Property
        
        self.type = None # str
        
