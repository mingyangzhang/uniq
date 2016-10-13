#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TopologyViewDto(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'description': 'str',
            
            
            'topology': 'Topology',
            
            
            'applicationUuid': 'str',
            
            
            'pageUuid': 'str',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'description': 'description',
            
            'topology': 'topology',
            
            'applicationUuid': 'applicationUuid',
            
            'pageUuid': 'pageUuid',
            
            'name': 'name'
            
        }       

        
        #Unique Identifier for View
        
        self.id = None # str
        
        #View description
        
        self.description = None # str
        
        #Topology being represented by this view
        
        self.topology = None # Topology
        
        #Application unique identifier for this view
        
        self.applicationUuid = None # str
        
        #Page unique identifier for this view inside the corresponding application
        
        self.pageUuid = None # str
        
        #View name
        
        self.name = None # str
        
