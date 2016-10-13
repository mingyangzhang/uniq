#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NodeWrapper(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'role': 'str',
            
            
            'order': 'int',
            
            
            'id': 'str',
            
            
            'label': 'str',
            
            
            'roleSource': 'str',
            
            
            'customParam': 'NodeWrapperCustom',
            
            
            'greyOut': 'bool',
            
            
            'deviceType': 'str',
            
            
            'ip': 'str',
            
            
            'softwareVersion': 'str',
            
            
            'nodeType': 'str',
            
            
            'family': 'str',
            
            
            'platformId': 'str',
            
            
            'tags': 'list[str]',
            
            
            'userId': 'str',
            
            
            'osType': 'str',
            
            
            'vlanId': 'str',
            
            
            'networkType': 'str',
            
            
            'y': 'int',
            
            
            'x': 'int',
            
            
            'dataPathId': 'str',
            
            
            'upperNode': 'str',
            
            
            'fixed': 'bool',
            
            
            'aclApplied': 'bool'
            
        }

        self.attributeMap = {
            
            'role': 'role',
            
            'order': 'order',
            
            'id': 'id',
            
            'label': 'label',
            
            'roleSource': 'roleSource',
            
            'customParam': 'customParam',
            
            'greyOut': 'greyOut',
            
            'deviceType': 'deviceType',
            
            'ip': 'ip',
            
            'softwareVersion': 'softwareVersion',
            
            'nodeType': 'nodeType',
            
            'family': 'family',
            
            'platformId': 'platformId',
            
            'tags': 'tags',
            
            'userId': 'userId',
            
            'osType': 'osType',
            
            'vlanId': 'vlanId',
            
            'networkType': 'networkType',
            
            'y': 'y',
            
            'x': 'x',
            
            'dataPathId': 'dataPathId',
            
            'upperNode': 'upperNode',
            
            'fixed': 'fixed',
            
            'aclApplied': 'aclApplied'
            
        }       

        
        #Role of the device
        
        self.role = None # str
        
        #Device order by link number
        
        self.order = None # int
        
        #Unique identifier for device
        
        self.id = None # str
        
        #Hostname of the device
        
        self.label = None # str
        
        #Indicates whether role is assigned manually or automatically
        
        self.roleSource = None # str
        
        #Device custom parameters
        
        self.customParam = None # NodeWrapperCustom
        
        #Indicates if the device is active for this topology view
        
        self.greyOut = None # bool
        
        #Type of the device
        
        self.deviceType = None # str
        
        #IP address of the device
        
        self.ip = None # str
        
        #Device OS version
        
        self.softwareVersion = None # str
        
        #Host or device
        
        self.nodeType = None # str
        
        #Product family which is part of the product identifier
        
        self.family = None # str
        
        #Device platform description
        
        self.platformId = None # str
        
        #List of tags applied on this device
        
        self.tags = None # list[str]
        
        #ID of the host 
        
        self.userId = None # str
        
        #OS type of the device
        
        self.osType = None # str
        
        #VLan id
        
        self.vlanId = None # str
        
        #Type of network
        
        self.networkType = None # str
        
        #Y position of the device on the displayed topology view
        
        self.y = None # int
        
        #X position of the device on the displayed topology view
        
        self.x = None # int
        
        #ID of the path between devices
        
        self.dataPathId = None # str
        
        #Start node ID
        
        self.upperNode = None # str
        
        #Indication of whether the position is fixed or will use auto layout 
        
        self.fixed = None # bool
        
        #Indicates if the ACL that is applied on the device
        
        self.aclApplied = None # bool
        
