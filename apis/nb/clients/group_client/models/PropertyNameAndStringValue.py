#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PropertyNameAndStringValue(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'stringValue': 'str',
            
            
            'propertyName': 'str',
            
            
            'instanceVersion': 'int',
            
            
            'instanceId': 'int',
            
            
            'instanceUuid': 'str',
            
            
            'description': 'str',
            
            
            'attributeMetadata': 'list[Entry«string,AttributeMetadata»]',
            
            
            'version': 'str'
            
        }

        self.attributeMap = {
            
            'stringValue': 'stringValue',
            
            'propertyName': 'propertyName',
            
            'instanceVersion': 'instanceVersion',
            
            'instanceId': 'instanceId',
            
            'instanceUuid': 'instanceUuid',
            
            'description': 'description',
            
            'attributeMetadata': 'attributeMetadata',
            
            'version': 'version'
            
        }       

        
        
        self.stringValue = None # str
        
        
        self.propertyName = None # str
        
        
        self.instanceVersion = None # int
        
        
        self.instanceId = None # int
        
        
        self.instanceUuid = None # str
        
        
        self.description = None # str
        
        
        self.attributeMetadata = None # list[Entry«string,AttributeMetadata»]
        
        
        self.version = None # str
        
