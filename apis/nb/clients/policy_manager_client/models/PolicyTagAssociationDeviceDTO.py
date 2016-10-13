#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyTagAssociationDeviceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'restricted': 'bool',
            
            
            'deviceIp': 'str',
            
            
            'unAssigned': 'bool',
            
            
            'deviceId': 'str',
            
            
            'deviceName': 'str',
            
            
            'restrictedReason': 'str',
            
            
            'deviceType': 'str',
            
            
            'deviceRole': 'str'
            
        }

        self.attributeMap = {
            
            'restricted': 'restricted',
            
            'deviceIp': 'deviceIp',
            
            'unAssigned': 'unAssigned',
            
            'deviceId': 'deviceId',
            
            'deviceName': 'deviceName',
            
            'restrictedReason': 'restrictedReason',
            
            'deviceType': 'deviceType',
            
            'deviceRole': 'deviceRole'
            
        }       

        
        
        self.restricted = None # bool
        
        
        self.deviceIp = None # str
        
        
        self.unAssigned = None # bool
        
        
        self.deviceId = None # str
        
        
        self.deviceName = None # str
        
        
        self.restrictedReason = None # str
        
        
        self.deviceType = None # str
        
        
        self.deviceRole = None # str
        
