#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IdentityAuthFileInfoDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'fileId': 'str',
            
            
            'fileType': 'str',
            
            
            'id': 'str',
            
            
            'fileName': 'str'
            
        }

        self.attributeMap = {
            
            'fileId': 'fileId',
            
            'fileType': 'fileType',
            
            'id': 'id',
            
            'fileName': 'fileName'
            
        }       

        
        #fileId
        
        self.fileId = None # str
        
        #fileType
        
        self.fileType = None # str
        
        #id
        
        self.id = None # str
        
        #fileName
        
        self.fileName = None # str
        
