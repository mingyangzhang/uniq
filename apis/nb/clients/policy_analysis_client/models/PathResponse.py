#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PathResponse(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'request': 'FlowAnalysis',
            
            
            'networkElements': 'list[NetworkElement]',
            
            
            'lastUpdate': 'str',
            
            
            'detailedStatus': 'DetailedStatus',
            
            
            'networkElementsInfo': 'list[NetworkElementInfo]',
            
            
            'properties': 'list[str]'
            
        }

        self.attributeMap = {
            
            'request': 'request',
            
            'networkElements': 'networkElements',
            
            'lastUpdate': 'lastUpdate',
            
            'detailedStatus': 'detailedStatus',
            
            'networkElementsInfo': 'networkElementsInfo',
            
            'properties': 'properties'
            
        }       

        
        #Describes the source and destination for a path trace
        
        self.request = None # FlowAnalysis
        
        
        self.networkElements = None # list[NetworkElement]
        
        #Last updated time
        
        self.lastUpdate = None # str
        
        #Detailed Status of the calculation of Path Trace with its inclusions
        
        self.detailedStatus = None # DetailedStatus
        
        #Nodes travesed along a path, including source and destination
        
        self.networkElementsInfo = None # list[NetworkElementInfo]
        
        #Properties for path trace
        
        self.properties = None # list[str]
        
