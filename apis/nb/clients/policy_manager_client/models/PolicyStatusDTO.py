#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PolicyStatusDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'status': 'str',
            
            
            'businessRelevantApplications': 'list[PolicyApplication]',
            
            
            'policyScope': 'str',
            
            
            'scopeWirelessSegment': 'str',
            
            
            'instanceUuid': 'str',
            
            
            'networkDeviceId': 'str',
            
            
            'networkDeviceName': 'str',
            
            
            'failureReason': 'str',
            
            
            'policyVersion': 'str',
            
            
            'lastSuccessfulPolicyVersion': 'str',
            
            
            'lastUpdated': 'str',
            
            
            'outOfScope': 'bool',
            
            
            'businessRelevantConsumerProducerApplications': 'list[PolicyConsumerProducerApplication]',
            
            
            'businessIrrelevantConsumerProducerApplications': 'list[PolicyConsumerProducerApplication]',
            
            
            'businessIrrelevantApplications': 'list[PolicyApplication]',
            
            
            'applicationPolicyCount': 'int',
            
            
            'networkDeviceIp': 'str'
            
        }

        self.attributeMap = {
            
            'status': 'status',
            
            'businessRelevantApplications': 'businessRelevantApplications',
            
            'policyScope': 'policyScope',
            
            'scopeWirelessSegment': 'scopeWirelessSegment',
            
            'instanceUuid': 'instanceUuid',
            
            'networkDeviceId': 'networkDeviceId',
            
            'networkDeviceName': 'networkDeviceName',
            
            'failureReason': 'failureReason',
            
            'policyVersion': 'policyVersion',
            
            'lastSuccessfulPolicyVersion': 'lastSuccessfulPolicyVersion',
            
            'lastUpdated': 'lastUpdated',
            
            'outOfScope': 'outOfScope',
            
            'businessRelevantConsumerProducerApplications': 'businessRelevantConsumerProducerApplications',
            
            'businessIrrelevantConsumerProducerApplications': 'businessIrrelevantConsumerProducerApplications',
            
            'businessIrrelevantApplications': 'businessIrrelevantApplications',
            
            'applicationPolicyCount': 'applicationPolicyCount',
            
            'networkDeviceIp': 'networkDeviceIp'
            
        }       

        
        
        self.status = None # str
        
        
        self.businessRelevantApplications = None # list[PolicyApplication]
        
        
        self.policyScope = None # str
        
        
        self.scopeWirelessSegment = None # str
        
        
        self.instanceUuid = None # str
        
        
        self.networkDeviceId = None # str
        
        
        self.networkDeviceName = None # str
        
        
        self.failureReason = None # str
        
        
        self.policyVersion = None # str
        
        
        self.lastSuccessfulPolicyVersion = None # str
        
        
        self.lastUpdated = None # str
        
        
        self.outOfScope = None # bool
        
        
        self.businessRelevantConsumerProducerApplications = None # list[PolicyConsumerProducerApplication]
        
        
        self.businessIrrelevantConsumerProducerApplications = None # list[PolicyConsumerProducerApplication]
        
        
        self.businessIrrelevantApplications = None # list[PolicyApplication]
        
        
        self.applicationPolicyCount = None # int
        
        
        self.networkDeviceIp = None # str
        
