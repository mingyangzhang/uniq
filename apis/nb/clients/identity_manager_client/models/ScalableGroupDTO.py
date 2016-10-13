#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScalableGroupDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'createTime': 'int',
            
            
            'scalableGroupExternalHandle': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'applications': 'list[ApplicationV2DTOBrief]',
            
            
            'applicationGroups': 'list[ApplicationGroupDTOBrief]',
            
            
            'parentScalableGroup': 'ScalableGroupBriefDTO',
            
            
            'identitySourceIpAddress': 'str',
            
            
            'identitySourceId': 'str',
            
            
            'identitySourceType': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'state': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'createTime': 'createTime',
            
            'scalableGroupExternalHandle': 'scalableGroupExternalHandle',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'applications': 'applications',
            
            'applicationGroups': 'applicationGroups',
            
            'parentScalableGroup': 'parentScalableGroup',
            
            'identitySourceIpAddress': 'identitySourceIpAddress',
            
            'identitySourceId': 'identitySourceId',
            
            'identitySourceType': 'identitySourceType',
            
            'name': 'name',
            
            'id': 'id',
            
            'state': 'state'
            
        }       

        
        #description
        
        self.description = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #scalableGroupExternalHandle
        
        self.scalableGroupExternalHandle = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #applications that belong to the scalable group.
        
        self.applications = None # list[ApplicationV2DTOBrief]
        
        #applicationGroups that belong to the scalable group.
        
        self.applicationGroups = None # list[ApplicationGroupDTOBrief]
        
        #parentScalableGroup from which user, user groups are inherited.
        
        self.parentScalableGroup = None # ScalableGroupBriefDTO
        
        #identitySourceIpAddress
        
        self.identitySourceIpAddress = None # str
        
        #identitySourceId
        
        self.identitySourceId = None # str
        
        #identitySourceType
        
        self.identitySourceType = None # str
        
        #name
        
        self.name = None # str
        
        #id
        
        self.id = None # str
        
        #state
        
        self.state = None # str
        
