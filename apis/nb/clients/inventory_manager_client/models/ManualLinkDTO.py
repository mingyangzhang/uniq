#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ManualLinkDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'isAManaged': 'bool',
            
            
            'isBManaged': 'bool',
            
            
            'type': 'str',
            
            
            'category': 'str',
            
            
            'linkStatus': 'str',
            
            
            'compositeType': 'str',
            
            
            'isManuallyAdded': 'bool',
            
            
            'linkCapacity': 'LongQuantity',
            
            
            'virSwitchUuid': 'str',
            
            
            'aggregatedLinks': 'list[IdRef]',
            
            
            'aggregatingLink': 'IdRef',
            
            
            'composingNetworkClouds': 'list[IdRef]',
            
            
            'forwardingRelationships': 'list[IdRef]',
            
            
            'linkTerminationPoints': 'list[IdRef]',
            
            
            'aggregatedLinksUrl': 'str',
            
            
            'aggregatingLinkUrl': 'str',
            
            
            'composingNetworkCloudsUrl': 'str',
            
            
            'forwardingRelationshipsUrl': 'str',
            
            
            'linkTerminationPointsUrl': 'str',
            
            
            'name': 'str',
            
            
            'description': 'str',
            
            
            'owningEntityId': 'str',
            
            
            'instanceUuid': 'str'
            
        }

        self.attributeMap = {
            
            'isAManaged': 'isAManaged',
            
            'isBManaged': 'isBManaged',
            
            'type': 'type',
            
            'category': 'category',
            
            'linkStatus': 'linkStatus',
            
            'compositeType': 'compositeType',
            
            'isManuallyAdded': 'isManuallyAdded',
            
            'linkCapacity': 'linkCapacity',
            
            'virSwitchUuid': 'virSwitchUuid',
            
            'aggregatedLinks': 'aggregatedLinks',
            
            'aggregatingLink': 'aggregatingLink',
            
            'composingNetworkClouds': 'composingNetworkClouds',
            
            'forwardingRelationships': 'forwardingRelationships',
            
            'linkTerminationPoints': 'linkTerminationPoints',
            
            'aggregatedLinksUrl': 'aggregatedLinksUrl',
            
            'aggregatingLinkUrl': 'aggregatingLinkUrl',
            
            'composingNetworkCloudsUrl': 'composingNetworkCloudsUrl',
            
            'forwardingRelationshipsUrl': 'forwardingRelationshipsUrl',
            
            'linkTerminationPointsUrl': 'linkTerminationPointsUrl',
            
            'name': 'name',
            
            'description': 'description',
            
            'owningEntityId': 'owningEntityId',
            
            'instanceUuid': 'instanceUuid'
            
        }       

        
        
        self.isAManaged = None # bool
        
        
        self.isBManaged = None # bool
        
        
        self.type = None # str
        
        
        self.category = None # str
        
        
        self.linkStatus = None # str
        
        
        self.compositeType = None # str
        
        
        self.isManuallyAdded = None # bool
        
        
        self.linkCapacity = None # LongQuantity
        
        
        self.virSwitchUuid = None # str
        
        
        self.aggregatedLinks = None # list[IdRef]
        
        
        self.aggregatingLink = None # IdRef
        
        
        self.composingNetworkClouds = None # list[IdRef]
        
        
        self.forwardingRelationships = None # list[IdRef]
        
        
        self.linkTerminationPoints = None # list[IdRef]
        
        
        self.aggregatedLinksUrl = None # str
        
        
        self.aggregatingLinkUrl = None # str
        
        
        self.composingNetworkCloudsUrl = None # str
        
        
        self.forwardingRelationshipsUrl = None # str
        
        
        self.linkTerminationPointsUrl = None # str
        
        
        self.name = None # str
        
        
        self.description = None # str
        
        
        self.owningEntityId = None # str
        
        
        self.instanceUuid = None # str
        
