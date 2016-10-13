#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Policy(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'policyScope': 'str',
            
            
            'resource': 'PolicyResource',
            
            
            'id': 'str',
            
            
            'state': 'str',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'policyName': 'str',
            
            
            'actionProperty': 'ActionProperty',
            
            
            'taskId': 'str',
            
            
            'policyPriority': 'int',
            
            
            'actions': 'list[str]',
            
            
            'networkUser': 'NetworkUser',
            
            
            'policyOwner': 'str'
            
        }

        self.attributeMap = {
            
            'policyScope': 'policyScope',
            
            'resource': 'resource',
            
            'id': 'id',
            
            'state': 'state',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'instanceUuid': 'instanceUuid',
            
            'policyName': 'policyName',
            
            'actionProperty': 'actionProperty',
            
            'taskId': 'taskId',
            
            'policyPriority': 'policyPriority',
            
            'actions': 'actions',
            
            'networkUser': 'networkUser',
            
            'policyOwner': 'policyOwner'
            
        }       

        
        #policyScope
        
        self.policyScope = None # str
        
        #Resource
        
        self.resource = None # PolicyResource
        
        #id
        
        self.id = None # str
        
        
        self.state = None # str
        
        
        self.scopeWirelessSegment = None # str
        
        #
        
        self.instanceUuid = None # str
        
        #name of the policy
        
        self.policyName = None # str
        
        #ActionProperty
        
        self.actionProperty = None # ActionProperty
        
        #Task ID
        
        self.taskId = None # str
        
        #Policy Priority
        
        self.policyPriority = None # int
        
        #Action Set
        
        self.actions = None # list[str]
        
        #Network User
        
        self.networkUser = None # NetworkUser
        
        #Policy Owner
        
        self.policyOwner = None # str
        
