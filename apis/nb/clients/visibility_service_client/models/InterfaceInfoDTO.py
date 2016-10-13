#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InterfaceInfoDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'subnetMask': 'str',
            
            
            'networkAddress': 'str',
            
            
            'ipAddress': 'str',
            
            
            'interfaceName': 'str',
            
            
            'nextHop': 'str',
            
            
            'trunkPort': 'bool',
            
            
            'switchPort': 'bool'
            
        }

        self.attributeMap = {
            
            'subnetMask': 'subnetMask',
            
            'networkAddress': 'networkAddress',
            
            'ipAddress': 'ipAddress',
            
            'interfaceName': 'interfaceName',
            
            'nextHop': 'nextHop',
            
            'trunkPort': 'trunkPort',
            
            'switchPort': 'switchPort'
            
        }       

        
        
        self.subnetMask = None # str
        
        
        self.networkAddress = None # str
        
        
        self.ipAddress = None # str
        
        
        self.interfaceName = None # str
        
        
        self.nextHop = None # str
        
        
        self.trunkPort = None # bool
        
        
        self.switchPort = None # bool
        
