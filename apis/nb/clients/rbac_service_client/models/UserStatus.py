#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class UserStatus(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'username': 'str',
            
            
            'accountLocked': 'bool',
            
            
            'lockExpiration': 'int',
            
            
            'lockedAt': 'str'
            
        }

        self.attributeMap = {
            
            'username': 'username',
            
            'accountLocked': 'accountLocked',
            
            'lockExpiration': 'lockExpiration',
            
            'lockedAt': 'lockedAt'
            
        }       

        
        
        self.username = None # str
        
        
        self.accountLocked = None # bool
        
        
        self.lockExpiration = None # int
        
        
        self.lockedAt = None # str
        
