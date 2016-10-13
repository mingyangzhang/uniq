#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IpAddressGlobalDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'numberOfSPs': 'str',
            
            
            'numberOfSites': 'str'
            
        }

        self.attributeMap = {
            
            'numberOfSPs': 'numberOfSPs',
            
            'numberOfSites': 'numberOfSites'
            
        }       

        
        
        self.numberOfSPs = None # str
        
        
        self.numberOfSites = None # str
        
