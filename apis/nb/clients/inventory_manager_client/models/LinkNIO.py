#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LinkNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'linkStatus': 'str',
            
            
            'numUpdates': 'int',
            
            
            'avgUpdateFrequency': 'int',
            
            
            'endDeviceHostName': 'str',
            
            
            'endDeviceId': 'str',
            
            
            'endPortId': 'str',
            
            
            'endDeviceIpAddress': 'str',
            
            
            'startDeviceId': 'str',
            
            
            'startPortId': 'str',
            
            
            'attributeInfo': 'object'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'lastUpdated': 'lastUpdated',
            
            'linkStatus': 'linkStatus',
            
            'numUpdates': 'numUpdates',
            
            'avgUpdateFrequency': 'avgUpdateFrequency',
            
            'endDeviceHostName': 'endDeviceHostName',
            
            'endDeviceId': 'endDeviceId',
            
            'endPortId': 'endPortId',
            
            'endDeviceIpAddress': 'endDeviceIpAddress',
            
            'startDeviceId': 'startDeviceId',
            
            'startPortId': 'startPortId',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        
        self.id = None # str
        
        
        self.lastUpdated = None # str
        
        
        self.linkStatus = None # str
        
        
        self.numUpdates = None # int
        
        
        self.avgUpdateFrequency = None # int
        
        
        self.endDeviceHostName = None # str
        
        
        self.endDeviceId = None # str
        
        
        self.endPortId = None # str
        
        
        self.endDeviceIpAddress = None # str
        
        
        self.startDeviceId = None # str
        
        
        self.startPortId = None # str
        
        
        self.attributeInfo = None # object
        
