#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class VlanDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'mask': 'int',
            
            
            'prefix': 'str',
            
            
            'vlanType': 'str',
            
            
            'vlanNumber': 'int',
            
            
            'interfaceName': 'str',
            
            
            'numberOfIPs': 'int',
            
            
            'ipAddress': 'str',
            
            
            'networkAddress': 'str'
            
        }

        self.attributeMap = {
            
            'mask': 'mask',
            
            'prefix': 'prefix',
            
            'vlanType': 'vlanType',
            
            'vlanNumber': 'vlanNumber',
            
            'interfaceName': 'interfaceName',
            
            'numberOfIPs': 'numberOfIPs',
            
            'ipAddress': 'ipAddress',
            
            'networkAddress': 'networkAddress'
            
        }       

        
        
        self.mask = None # int
        
        
        self.prefix = None # str
        
        
        self.vlanType = None # str
        
        
        self.vlanNumber = None # int
        
        
        self.interfaceName = None # str
        
        
        self.numberOfIPs = None # int
        
        
        self.ipAddress = None # str
        
        
        self.networkAddress = None # str
        
