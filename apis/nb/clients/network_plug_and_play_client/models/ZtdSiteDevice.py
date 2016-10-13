#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdSiteDevice(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'authStatus': 'DeviceAuthState',
            
            
            'deviceId': 'str',
            
            
            'lastStateTransitionTime': 'str',
            
            
            'lastContact': 'str',
            
            
            'stateDisplay': 'str',
            
            
            'state': 'str',
            
            
            'serialNumber': 'str',
            
            
            'tag': 'str',
            
            
            'aliases': 'list[str]',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'site': 'str',
            
            
            'configId': 'str',
            
            
            'pkiEnabled': 'bool',
            
            
            'imageId': 'str',
            
            
            'memberDetail': 'list[ZtdMemberDetail]',
            
            
            'deviceDiscoveryInfo': 'ZtdDeviceDiscoveryInfo',
            
            
            'bootStrapId': 'str',
            
            
            'licenseString': 'str',
            
            
            'apCount': 'str',
            
            
            'isMobilityController': 'str',
            
            
            'sudiRequired': 'bool',
            
            
            'memberCount': 'int',
            
            
            'licenseLevel': 'str',
            
            
            'eulaAccepted': 'bool',
            
            
            'connectedToDeviceId': 'str',
            
            
            'connectedToPortId': 'str',
            
            
            'templateConfigId': 'str',
            
            
            'imagePreference': 'str',
            
            
            'connetedToLocationGeoAddr': 'str',
            
            
            'configPreference': 'str',
            
            
            'connectedToPortName': 'str',
            
            
            'connectedToDeviceHostName': 'str',
            
            
            'connetedToLocationCivicAddr': 'str',
            
            
            'hostName': 'str'
        }

        self.attributeMap = {
            
            'authStatus': 'authStatus',
            
            'deviceId': 'deviceId',
            
            'lastStateTransitionTime': 'lastStateTransitionTime',
            
            'lastContact': 'lastContact',
            
            'stateDisplay': 'stateDisplay',
            
            'state': 'state',
            
            'serialNumber': 'serialNumber',
            
            'tag': 'tag',
            
            'aliases': 'aliases',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'site': 'site',
            
            'configId': 'configId',
            
            'pkiEnabled': 'pkiEnabled',
            
            'imageId': 'imageId',
            
            'memberDetail': 'memberDetail',
            
            'deviceDiscoveryInfo': 'deviceDiscoveryInfo',
            
            'bootStrapId': 'bootStrapId',
            
            'licenseString': 'licenseString',
            
            'apCount': 'apCount',
            
            'isMobilityController': 'isMobilityController',
            
            'sudiRequired': 'sudiRequired',
            
            'memberCount': 'memberCount',
            
            'licenseLevel': 'licenseLevel',
            
            'eulaAccepted': 'eulaAccepted',
            
            'connectedToDeviceId': 'connectedToDeviceId',
            
            'connectedToPortId': 'connectedToPortId',
            
            'templateConfigId': 'templateConfigId',
            
            'imagePreference': 'imagePreference',
            
            'connetedToLocationGeoAddr': 'connetedToLocationGeoAddr',
            
            'configPreference': 'configPreference',
            
            'connectedToPortName': 'connectedToPortName',
            
            'connectedToDeviceHostName': 'connectedToDeviceHostName',
            
            'connetedToLocationCivicAddr': 'connetedToLocationCivicAddr',
            
            'hostName': 'hostName'            
        }       

        
        
        self.authStatus = None # DeviceAuthState
        
        
        self.deviceId = None # str
        
        
        self.lastStateTransitionTime = None # str
        
        
        self.lastContact = None # str
        
        
        self.stateDisplay = None # str
        
        
        self.state = None # str
        
        #Serial number
        
        self.serialNumber = None # str
        
        #Tag of device
        
        self.tag = None # str
        
        
        self.aliases = None # list[str]
        
        #ID of device
        
        self.id = None # str
        
        #Platform ID
        
        self.platformId = None # str
        
        #Site to which device belongs if auto-provisioned
        
        self.site = None # str
        
        #Configuration file id
        
        self.configId = None # str
        
        #Configure PKCS#12 trust point during PNP workflow if true
        
        self.pkiEnabled = None # bool
        
        #Image file ID
        
        self.imageId = None # str
        
        
        self.memberDetail = None # list[ZtdMemberDetail]
        
        #Device discovery info
        
        self.deviceDiscoveryInfo = None # ZtdDeviceDiscoveryInfo
        
        #Bootstrap file id
        
        self.bootStrapId = None # str
        
        #License string
        
        self.licenseString = None # str
        
        #Wireless AP count
        
        self.apCount = None # str
        
        #Specify if device is a wireless mobility controller
        
        self.isMobilityController = None # str
        
        
        self.sudiRequired = None # bool
        
        #Count of members in a stack switch excluding master
        
        self.memberCount = None # int
        
        #CLI execution license level
        
        self.licenseLevel = None # str
        
        #CLI execution EULA accepted or not
        
        self.eulaAccepted = None # bool
        
        
        self.connectedToDeviceId = None # str
        
        
        self.connectedToPortId = None # str
        
        #Template config ID
        
        self.templateConfigId = None # str
        
        
        self.imagePreference = None # str
        
        
        self.connetedToLocationGeoAddr = None # str
        
        
        self.configPreference = None # str
        
        
        self.connectedToPortName = None # str
        
        
        self.connectedToDeviceHostName = None # str
        
        
        self.connetedToLocationCivicAddr = None # str
        
        #Host name
        
        self.hostName = None # str        
