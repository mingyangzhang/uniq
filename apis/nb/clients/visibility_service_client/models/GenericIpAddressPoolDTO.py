#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class GenericIpAddressPoolDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'address': 'str',
            
            
            'id': 'str',
            
            
            'prefix': 'str',
            
            
            'addressPoolType': 'str',
            
            
            'ipv4Subnet': 'str',
            
            
            'usagePercentage': 'int'
            
        }

        self.attributeMap = {
            
            'address': 'address',
            
            'id': 'id',
            
            'prefix': 'prefix',
            
            'addressPoolType': 'addressPoolType',
            
            'ipv4Subnet': 'ipv4Subnet',
            
            'usagePercentage': 'usagePercentage'
            
        }       

        
        
        self.address = None # str
        
        
        self.id = None # str
        
        
        self.prefix = None # str
        
        
        self.addressPoolType = None # str
        
        
        self.ipv4Subnet = None # str
        
        
        self.usagePercentage = None # int
        
