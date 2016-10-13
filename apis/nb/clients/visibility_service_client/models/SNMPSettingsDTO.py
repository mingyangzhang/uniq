#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SNMPSettingsDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'mode': 'str',
            
            
            'timeout': 'str',
            
            
            'version': 'str',
            
            
            'username': 'str',
            
            
            'authPwd': 'str',
            
            
            'privacyPwd': 'str',
            
            
            'readCommunity': 'str',
            
            
            'writeCommunity': 'str',
            
            
            'authType': 'str',
            
            
            'privacyType': 'str',
            
            
            'retry': 'str',
            
            
            'trapReflectionDestIp': 'str'
            
        }

        self.attributeMap = {
            
            'mode': 'mode',
            
            'timeout': 'timeout',
            
            'version': 'version',
            
            'username': 'username',
            
            'authPwd': 'authPwd',
            
            'privacyPwd': 'privacyPwd',
            
            'readCommunity': 'readCommunity',
            
            'writeCommunity': 'writeCommunity',
            
            'authType': 'authType',
            
            'privacyType': 'privacyType',
            
            'retry': 'retry',
            
            'trapReflectionDestIp': 'trapReflectionDestIp'
            
        }       

        
        
        self.mode = None # str
        
        
        self.timeout = None # str
        
        
        self.version = None # str
        
        
        self.username = None # str
        
        
        self.authPwd = None # str
        
        
        self.privacyPwd = None # str
        
        
        self.readCommunity = None # str
        
        
        self.writeCommunity = None # str
        
        
        self.authType = None # str
        
        
        self.privacyType = None # str
        
        
        self.retry = None # str
        
        
        self.trapReflectionDestIp = None # str
        
