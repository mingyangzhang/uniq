#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class GlobalCredentialDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'comments': 'str',
            
            
            'description': 'str',
            
            
            'credentialType': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str',

            'username': 'str' # added this manually
            
        }

        self.attributeMap = {
            
            'comments': 'comments',
            
            'description': 'description',
            
            'credentialType': 'credentialType',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id',

            'username': 'username' # added this manually
            
        }       

        #Added line 66-69 manually
        #CLI username or SNMP user name

        self.username = None # str

        #Comments to identify the credential
        
        self.comments = None # str
        
        #Description of the credential
        
        self.description = None # str
        
        #Credential type to identify the application that uses the credential
        
        self.credentialType = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
