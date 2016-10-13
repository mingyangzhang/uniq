#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteIPAddressPoolDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'prefix': 'str',
            
            
            'ipAddress': 'str',
            
            
            'vlanType': 'str',
            
            
            'vlanId': 'str',
            
            
            'siteName': 'str',
            
            
            'ipAddressType': 'str',
            
            
            'isBrownFieldSite': 'bool',
            
            
            'ipv4Subnet': 'str',
            
            
            'deviceSerialNumber': 'list[str]',
            
            
            'layer3Site': 'bool'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'prefix': 'prefix',
            
            'ipAddress': 'ipAddress',
            
            'vlanType': 'vlanType',
            
            'vlanId': 'vlanId',
            
            'siteName': 'siteName',
            
            'ipAddressType': 'ipAddressType',
            
            'isBrownFieldSite': 'isBrownFieldSite',
            
            'ipv4Subnet': 'ipv4Subnet',
            
            'deviceSerialNumber': 'deviceSerialNumber',
            
            'layer3Site': 'layer3Site'
            
        }       

        
        
        self.id = None # str
        
        
        self.prefix = None # str
        
        
        self.ipAddress = None # str
        
        
        self.vlanType = None # str
        
        
        self.vlanId = None # str
        
        
        self.siteName = None # str
        
        
        self.ipAddressType = None # str
        
        
        self.isBrownFieldSite = None # bool
        
        
        self.ipv4Subnet = None # str
        
        
        self.deviceSerialNumber = None # list[str]
        
        
        self.layer3Site = None # bool
        
