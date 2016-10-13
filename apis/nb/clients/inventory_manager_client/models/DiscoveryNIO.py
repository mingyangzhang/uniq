#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DiscoveryNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'name': 'str',
            
            
            'globalCredentialIdList': 'list[str]',
            
            
            'ipFilterList': 'str',
            
            
            'passwordList': 'str',
            
            
            'enablePasswordList': 'str',
            
            
            'snmpAuthPassphrase': 'str',
            
            
            'snmpPrivPassphrase': 'str',
            
            
            'snmpPrivProtocol': 'str',
            
            
            'snmpAuthProtocol': 'str',
            
            
            'userNameList': 'str',
            
            
            'isAutoCdp': 'bool',
            
            
            'parentDiscoveryId': 'str',
            
            
            'cdpLevel': 'int',
            
            
            'snmpRoCommunity': 'str',
            
            
            'snmpRwCommunity': 'str',
            
            
            'protocolOrder': 'str',
            
            
            'discoveryCondition': 'str',
            
            
            'numDevices': 'int',
            
            
            'retryCount': 'int',
            
            
            'discoveryType': 'str',
            
            
            'ipAddressList': 'str',
            
            
            'timeOut': 'int',
            
            
            'id': 'str',
            
            
            'discoveryStatus': 'str',
            
            
            'snmpMode': 'str',
            
            
            'deviceIds': 'str',
            
            
            'snmpUserName': 'str',
            
            
            'attributeInfo': 'object'
            
        }

        self.attributeMap = {
            
            'name': 'name',
            
            'globalCredentialIdList': 'globalCredentialIdList',
            
            'ipFilterList': 'ipFilterList',
            
            'passwordList': 'passwordList',
            
            'enablePasswordList': 'enablePasswordList',
            
            'snmpAuthPassphrase': 'snmpAuthPassphrase',
            
            'snmpPrivPassphrase': 'snmpPrivPassphrase',
            
            'snmpPrivProtocol': 'snmpPrivProtocol',
            
            'snmpAuthProtocol': 'snmpAuthProtocol',
            
            'userNameList': 'userNameList',
            
            'isAutoCdp': 'isAutoCdp',
            
            'parentDiscoveryId': 'parentDiscoveryId',
            
            'cdpLevel': 'cdpLevel',
            
            'snmpRoCommunity': 'snmpRoCommunity',
            
            'snmpRwCommunity': 'snmpRwCommunity',
            
            'protocolOrder': 'protocolOrder',
            
            'discoveryCondition': 'discoveryCondition',
            
            'numDevices': 'numDevices',
            
            'retryCount': 'retryCount',
            
            'discoveryType': 'discoveryType',
            
            'ipAddressList': 'ipAddressList',
            
            'timeOut': 'timeOut',
            
            'id': 'id',
            
            'discoveryStatus': 'discoveryStatus',
            
            'snmpMode': 'snmpMode',
            
            'deviceIds': 'deviceIds',
            
            'snmpUserName': 'snmpUserName',
            
            'attributeInfo': 'attributeInfo'
            
        }       

        
        #Name for the discovery
        
        self.name = None # str
        
        #To get the list of global credential of the discovery
        
        self.globalCredentialIdList = None # list[str]
        
        #IP addresses of the devices to be filtered
        
        self.ipFilterList = None # str
        
        #Password of the devices to be discovered
        
        self.passwordList = None # str
        
        #Enable Password of the devices to be discovered
        
        self.enablePasswordList = None # str
        
        
        self.snmpAuthPassphrase = None # str
        
        
        self.snmpPrivPassphrase = None # str
        
        
        self.snmpPrivProtocol = None # str
        
        
        self.snmpAuthProtocol = None # str
        
        #Username of the devices to be discovered
        
        self.userNameList = None # str
        
        #Flag to mention if CDP discovery or not
        
        self.isAutoCdp = None # bool
        
        #Parent Discovery Id from which the discovery initiated
        
        self.parentDiscoveryId = None # str
        
        #CDP level to which neighbor devices to be discovered
        
        self.cdpLevel = None # int
        
        #Snmp RO community of the devices to be discovered
        
        self.snmpRoCommunity = None # str
        
        #Snmp RW community of the devices to be discovered
        
        self.snmpRwCommunity = None # str
        
        #Order of protocol in which device connection establishment to be tried
        
        self.protocolOrder = None # str
        
        #To indicate the discovery status. Available options: Complete or In Progress
        
        self.discoveryCondition = None # str
        
        #Number of devices discovered in a discovery
        
        self.numDevices = None # int
        
        #Number of times to try establishing connection to device
        
        self.retryCount = None # int
        
        #Available types are: single, auto cdp discovery, range, multi range
        
        self.discoveryType = None # str
        
        #Ip address of the device to be discovered
        
        self.ipAddressList = None # str
        
        #Time to wait for device response.
        
        self.timeOut = None # int
        
        #Unique identifier for discovery
        
        self.id = None # str
        
        #Available options are: active, inactive
        
        self.discoveryStatus = None # str
        
        
        self.snmpMode = None # str
        
        #Ids of the devices discovered in a discovery
        
        self.deviceIds = None # str
        
        
        self.snmpUserName = None # str
        
        
        self.attributeInfo = None # object
        
