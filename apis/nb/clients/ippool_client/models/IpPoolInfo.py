#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IpPoolInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'role': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'id': 'str',
            
            
            'apicAppName': 'str',
            
            
            'nextAddress': 'str',
            
            
            'ipPoolName': 'str',
            
            
            'creationOrder': 'int',
            
            
            'createTime': 'int',
            
            
            'ipPool': 'str',
            
            
            'startAddress': 'str',
            
            
            'endAddress': 'str',
            
            
            'dhcpServerIp': 'list[str]',
            
            
            'gateway': 'list[str]',
            
            
            'interAppOverlap': 'bool',
            
            
            'shared': 'bool',
            
            
            'usagePercentage': 'int',
            
            
            'freeIpCount': 'int',
            
            
            'excludeNetworkBroadcastAddress': 'bool',
            
            
            'parentId': 'str'
            
        }

        self.attributeMap = {
            
            'role': 'role',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'id': 'id',
            
            'apicAppName': 'apicAppName',
            
            'nextAddress': 'nextAddress',
            
            'ipPoolName': 'ipPoolName',
            
            'creationOrder': 'creationOrder',
            
            'createTime': 'createTime',
            
            'ipPool': 'ipPool',
            
            'startAddress': 'startAddress',
            
            'endAddress': 'endAddress',
            
            'dhcpServerIp': 'dhcpServerIp',
            
            'gateway': 'gateway',
            
            'interAppOverlap': 'interAppOverlap',
            
            'shared': 'shared',
            
            'usagePercentage': 'usagePercentage',
            
            'freeIpCount': 'freeIpCount',
            
            'excludeNetworkBroadcastAddress': 'excludeNetworkBroadcastAddress',
            
            'parentId': 'parentId'
            
        }       

        
        #Used to group IP Address Pools
        
        self.role = None # str
        
        #IP Address Pool last updated time
        
        self.lastUpdateTime = None # int
        
        #UUID of IP Address Pool
        
        self.id = None # str
        
        #APIC-EM App Name
        
        self.apicAppName = None # str
        
        #Next available IP address in IP Address Pool
        
        self.nextAddress = None # str
        
        #IP Address Pool name
        
        self.ipPoolName = None # str
        
        #Creation order of IP Address Pool
        
        self.creationOrder = None # int
        
        #IP Address Pool creation time
        
        self.createTime = None # int
        
        #IP subnet in CIDR format
        
        self.ipPool = None # str
        
        #First IP address in IP Address Pool
        
        self.startAddress = None # str
        
        #Last IP address in IP Address Pool
        
        self.endAddress = None # str
        
        #DHCP server hostname or IP address list
        
        self.dhcpServerIp = None # list[str]
        
        #Gateway IP address list
        
        self.gateway = None # list[str]
        
        #If true then overlapping IP pool is supported between APIC-EM Apps. Default value is false
        
        self.interAppOverlap = None # bool
        
        #If true then duplicate/overlapping pool is supported. Default value is false
        
        self.shared = None # bool
        
        #Current usage percentage of IP Address Pool
        
        self.usagePercentage = None # int
        
        #IP Address Pool free IP count
        
        self.freeIpCount = None # int
        
        #If true then network and broadcast IP address will not be used in the usable range. Default value is false
        
        self.excludeNetworkBroadcastAddress = None # bool
        
        #Parent IP Address Pool UUID
        
        self.parentId = None # str
