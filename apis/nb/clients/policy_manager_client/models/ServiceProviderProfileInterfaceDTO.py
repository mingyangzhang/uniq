#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ServiceProviderProfileInterfaceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'deviceId': 'str',
            
            
            'policyScope': 'str',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'deviceName': 'str',
            
            
            'interfaceId': 'str',
            
            
            'interfaceName': 'str',
            
            
            'serviceProviderProfileVersion': 'int',
            
            
            'current': 'bool',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'deviceId': 'deviceId',
            
            'policyScope': 'policyScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'deviceName': 'deviceName',
            
            'interfaceId': 'interfaceId',
            
            'interfaceName': 'interfaceName',
            
            'serviceProviderProfileVersion': 'serviceProviderProfileVersion',
            
            'current': 'current',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        
        self.deviceId = None # str
        
        
        self.policyScope = None # str
        
        
        self.scopeWirelessSegment = None # str
        
        
        self.deviceName = None # str
        
        
        self.interfaceId = None # str
        
        
        self.interfaceName = None # str
        
        
        self.serviceProviderProfileVersion = None # int
        
        
        self.current = None # bool
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
