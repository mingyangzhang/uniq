#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class HubSiteWanDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'capacity': 'str',
            
            
            'lanInterfaceName': 'list[str]',
            
            
            'deviceId': 'str',
            
            
            'wanCloud': 'WanCloudDTO',
            
            
            'wanType': 'str',
            
            
            'deviceType': 'str',
            
            
            'managementIpAddress': 'str',
            
            
            'bandwidth': 'str',
            
            
            'downloadBW': 'str',
            
            
            'natIp': 'str',
            
            
            'serviceProvider': 'str',
            
            
            'pathId': 'int',
            
            
            'mcDevice': 'bool',
            
            
            'defaultGW': 'str',
            
            
            'wanInterfaceName': 'str',
            
            
            'wanIp': 'str',
            
            
            'coexistenceLoopbackInterfaceName': 'str',
            
            
            'coexistenceLoopbackInterfaceIpAddress': 'str',
            
            
            'geoLocation': 'str',
            
            
            'vspWanType': 'str',
            
            
            'vspEnabled': 'bool',
            
            
            'dhcpEnabled': 'bool',
            
            
            'wanLabel': 'str',
            
            
            'vspWanLebel': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'capacity': 'capacity',
            
            'lanInterfaceName': 'lanInterfaceName',
            
            'deviceId': 'deviceId',
            
            'wanCloud': 'wanCloud',
            
            'wanType': 'wanType',
            
            'deviceType': 'deviceType',
            
            'managementIpAddress': 'managementIpAddress',
            
            'bandwidth': 'bandwidth',
            
            'downloadBW': 'downloadBW',
            
            'natIp': 'natIp',
            
            'serviceProvider': 'serviceProvider',
            
            'pathId': 'pathId',
            
            'mcDevice': 'mcDevice',
            
            'defaultGW': 'defaultGW',
            
            'wanInterfaceName': 'wanInterfaceName',
            
            'wanIp': 'wanIp',
            
            'coexistenceLoopbackInterfaceName': 'coexistenceLoopbackInterfaceName',
            
            'coexistenceLoopbackInterfaceIpAddress': 'coexistenceLoopbackInterfaceIpAddress',
            
            'geoLocation': 'geoLocation',
            
            'vspWanType': 'vspWanType',
            
            'vspEnabled': 'vspEnabled',
            
            'dhcpEnabled': 'dhcpEnabled',
            
            'wanLabel': 'wanLabel',
            
            'vspWanLebel': 'vspWanLebel',
            
            'id': 'id'
            
        }       

        
        
        self.capacity = None # str
        
        
        self.lanInterfaceName = None # list[str]
        
        
        self.deviceId = None # str
        
        
        self.wanCloud = None # WanCloudDTO
        
        
        self.wanType = None # str
        
        
        self.deviceType = None # str
        
        
        self.managementIpAddress = None # str
        
        
        self.bandwidth = None # str
        
        
        self.downloadBW = None # str
        
        
        self.natIp = None # str
        
        
        self.serviceProvider = None # str
        
        
        self.pathId = None # int
        
        
        self.mcDevice = None # bool
        
        
        self.defaultGW = None # str
        
        
        self.wanInterfaceName = None # str
        
        
        self.wanIp = None # str
        
        
        self.coexistenceLoopbackInterfaceName = None # str
        
        
        self.coexistenceLoopbackInterfaceIpAddress = None # str
        
        
        self.geoLocation = None # str
        
        
        self.vspWanType = None # str
        
        
        self.vspEnabled = None # bool
        
        
        self.dhcpEnabled = None # bool
        
        
        self.wanLabel = None # str
        
        
        self.vspWanLebel = None # str
        
        
        self.id = None # str
        
