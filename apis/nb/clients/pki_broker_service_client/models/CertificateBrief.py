#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CertificateBrief(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'issuer': 'str',
            
            
            'commonName': 'str',
            
            
            'serialNumber': 'str',
            
            
            'proxyEnabled': 'str',
            
            
            'selfSigned': 'str',
            
            
            'gvSerialId': 'str',
            
            
            'expiry': 'str',
            
            
            'filePath': 'str',
            
            
            'lastCertFilePath': 'str',
            
            
            'attributeInfo': 'object',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'issuer': 'issuer',
            
            'commonName': 'commonName',
            
            'serialNumber': 'serialNumber',
            
            'proxyEnabled': 'proxyEnabled',
            
            'selfSigned': 'selfSigned',
            
            'gvSerialId': 'gvSerialId',
            
            'expiry': 'expiry',
            
            'filePath': 'filePath',
            
            'lastCertFilePath': 'lastCertFilePath',
            
            'attributeInfo': 'attributeInfo',
            
            'id': 'id'
            
        }       

        
        
        self.issuer = None # str
        
        
        self.commonName = None # str
        
        
        self.serialNumber = None # str
        
        
        self.proxyEnabled = None # str
        
        
        self.selfSigned = None # str
        
        
        self.gvSerialId = None # str
        
        
        self.expiry = None # str
        
        
        self.filePath = None # str
        
        
        self.lastCertFilePath = None # str
        
        
        self.attributeInfo = None # object
        
        
        self.id = None # str
        
