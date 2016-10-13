#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InetAddress(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'address': 'str',
            
            
            'allZeros': 'bool',
            
            
            'allOnes': 'bool',
            
            
            'octets': 'list[byte]',
            
            
            'paddedAddress': 'str',
            
            
            'addressType': 'str'
            
        }

        self.attributeMap = {
            
            'address': 'address',
            
            'allZeros': 'allZeros',
            
            'allOnes': 'allOnes',
            
            'octets': 'octets',
            
            'paddedAddress': 'paddedAddress',
            
            'addressType': 'addressType'
            
        }       

        
        
        self.address = None # str
        
        
        self.allZeros = None # bool
        
        
        self.allOnes = None # bool
        
        
        self.octets = None # list[byte]
        
        
        self.paddedAddress = None # str
        
        
        self.addressType = None # str
        
