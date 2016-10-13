#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyIntentSummaryDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'operations': 'list[str]',
            
            
            'applicationsStale': 'bool',
            
            
            'policyScope': 'str',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'latestPolicyVersion': 'int',
            
            
            'numberOfAssignedApplications': 'int',
            
            
            'numberOfDevices': 'int',
            
            
            'allPoliciesDeleted': 'bool'
            
        }

        self.attributeMap = {
            
            'operations': 'operations',
            
            'applicationsStale': 'applicationsStale',
            
            'policyScope': 'policyScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'latestPolicyVersion': 'latestPolicyVersion',
            
            'numberOfAssignedApplications': 'numberOfAssignedApplications',
            
            'numberOfDevices': 'numberOfDevices',
            
            'allPoliciesDeleted': 'allPoliciesDeleted'
            
        }       

        
        #The operations in that version. (policy-add, policy-update, policy-delete)
        
        self.operations = None # list[str]
        
        #Flag to indicate if applications are stale in the policy
        
        self.applicationsStale = None # bool
        
        #Scope of the policy
        
        self.policyScope = None # str
        
        #Wireless segment of the policy
        
        self.scopeWirelessSegment = None # str
        
        #Last update time of the policy
        
        self.lastUpdateTime = None # int
        
        #Latest version of the policy
        
        self.latestPolicyVersion = None # int
        
        #The number of assigned applications in the policy
        
        self.numberOfAssignedApplications = None # int
        
        #The number of devices in the policy scope
        
        self.numberOfDevices = None # int
        
        #Flag to indicate if all policies are deleted in the policy scope
        
        self.allPoliciesDeleted = None # bool
        
