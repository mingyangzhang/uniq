#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PkiTrustPoint(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'serialNumber': 'str',
            
            
            'entityName': 'str',
            
            
            'id': 'str',
            
            
            'platformId': 'str',
            
            
            'trustProfileName': 'str',
            
            
            'entityType': 'str',
            
            
            'networkDeviceId': 'str',
            
            
            'certificateAuthorityId': 'str',
            
            
            'controllerIpAddress': 'str'
            
        }

        self.attributeMap = {
            
            'serialNumber': 'serialNumber',
            
            'entityName': 'entityName',
            
            'id': 'id',
            
            'platformId': 'platformId',
            
            'trustProfileName': 'trustProfileName',
            
            'entityType': 'entityType',
            
            'networkDeviceId': 'networkDeviceId',
            
            'certificateAuthorityId': 'certificateAuthorityId',
            
            'controllerIpAddress': 'controllerIpAddress'
            
        }       

        
        
        self.serialNumber = None # str
        
        
        self.entityName = None # str
        
        
        self.id = None # str
        
        
        self.platformId = None # str
        
        
        self.trustProfileName = None # str
        
        
        self.entityType = None # str
        
        
        self.networkDeviceId = None # str
        
        
        self.certificateAuthorityId = None # str
        
        
        self.controllerIpAddress = None # str
        
