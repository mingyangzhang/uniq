#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyPreviewDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'state': 'str',
            
            
            'policies': 'list[Policy]',
            
            
            'networkDeviceIds': 'list[str]',
            
            
            'deviceConfigs': 'list[PolicyPreviewDeviceConfigDTO]',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'state': 'state',
            
            'policies': 'policies',
            
            'networkDeviceIds': 'networkDeviceIds',
            
            'deviceConfigs': 'deviceConfigs',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        #state
        
        self.state = None # str
        
        #list of policies
        
        self.policies = None # list[Policy]
        
        #list of network device ids
        
        self.networkDeviceIds = None # list[str]
        
        #list of preview device configs
        
        self.deviceConfigs = None # list[PolicyPreviewDeviceConfigDTO]
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
