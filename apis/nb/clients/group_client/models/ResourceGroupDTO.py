#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ResourceGroupDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'subGroup': 'list[IdRef]',
            
            
            'groupMember': 'list[IdRef]',
            
            
            'groupTypeList': 'list[str]',
            
            
            'additionalInfo': 'list[PropertyNameAndStringValue]',
            
            
            'groupMemberUrl': 'str',
            
            
            'subGroupUrl': 'str',
            
            
            'name': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'subGroup': 'subGroup',
            
            'groupMember': 'groupMember',
            
            'groupTypeList': 'groupTypeList',
            
            'additionalInfo': 'additionalInfo',
            
            'groupMemberUrl': 'groupMemberUrl',
            
            'subGroupUrl': 'subGroupUrl',
            
            'name': 'name',
            
            'instanceUuid': 'instanceUuid',
            
            'id': 'id'
            
        }       

        
        
        self.subGroup = None # list[IdRef]
        
        
        self.groupMember = None # list[IdRef]
        
        
        self.groupTypeList = None # list[str]
        
        
        self.additionalInfo = None # list[PropertyNameAndStringValue]
        
        
        self.groupMemberUrl = None # str
        
        
        self.subGroupUrl = None # str
        
        
        self.name = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.id = None # str
        
