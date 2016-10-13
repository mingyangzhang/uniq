#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyInterruptDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int',
            
            
            'policyScope': 'str',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'action': 'str'
            
        }

        self.attributeMap = {
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime',
            
            'policyScope': 'policyScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'action': 'action'
            
        }       

        
        
        self.lastUpdateTime = None # int
        
        
        self.createTime = None # int
        
        
        self.policyScope = None # str
        
        
        self.scopeWirelessSegment = None # str
        
        
        self.action = None # str
        
