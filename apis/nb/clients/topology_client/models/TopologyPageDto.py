#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TopologyPageDto(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'description': 'str',
            
            
            'defaultViewId': 'str',
            
            
            'applicationUuid': 'str',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'description': 'description',
            
            'defaultViewId': 'defaultViewId',
            
            'applicationUuid': 'applicationUuid',
            
            'name': 'name'
            
        }       

        
        #Unique identifier for this Page
        
        self.id = None # str
        
        #Description for this Page
        
        self.description = None # str
        
        #Default View unique identifier for this Page
        
        self.defaultViewId = None # str
        
        #Application unique identifier for this Page
        
        self.applicationUuid = None # str
        
        #Name for this Page
        
        self.name = None # str
        
