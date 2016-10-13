#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyInterruptInput(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'action': 'str',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'policyScope': 'str'
            
        }

        self.attributeMap = {
            
            'action': 'action',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'policyScope': 'policyScope'
            
        }       

        
        
        self.action = None # str
        
        
        self.scopeWirelessSegment = None # str
        
        
        self.policyScope = None # str
        
