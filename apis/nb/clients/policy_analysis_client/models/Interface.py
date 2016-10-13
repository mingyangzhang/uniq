#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class Interface(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'vrfName': 'str',
            
            
            'aclAnalysis': 'AclAnalysisResponse',
            
            
            'interfaceStatistics': 'InterfaceStatistics',
            
            
            'qosStatistics': 'list[QosClassMapStatistics]',
            
            
            'interfaceStatsCollection': 'str',
            
            
            'interfaceStatsCollectionFailureReason': 'str',
            
            
            'qosStatsCollection': 'str',
            
            
            'qosStatsCollectionFailureReason': 'str',
            
            
            'name': 'str',
            
            
            'id': 'str'
            
        }

        self.attributeMap = {
            
            'vrfName': 'vrfName',
            
            'aclAnalysis': 'aclAnalysis',
            
            'interfaceStatistics': 'interfaceStatistics',
            
            'qosStatistics': 'qosStatistics',
            
            'interfaceStatsCollection': 'interfaceStatsCollection',
            
            'interfaceStatsCollectionFailureReason': 'interfaceStatsCollectionFailureReason',
            
            'qosStatsCollection': 'qosStatsCollection',
            
            'qosStatsCollectionFailureReason': 'qosStatsCollectionFailureReason',
            
            'name': 'name',
            
            'id': 'id'
            
        }       

        
        #Name of VRF that the interface on a device belongs to
        
        self.vrfName = None # str
        
        #Analysis of ACLs on an interface of a device
        
        self.aclAnalysis = None # AclAnalysisResponse
        
        
        self.interfaceStatistics = None # InterfaceStatistics
        
        
        self.qosStatistics = None # list[QosClassMapStatistics]
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.interfaceStatsCollection = None # str
        
        
        self.interfaceStatsCollectionFailureReason = None # str
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.qosStatsCollection = None # str
        
        
        self.qosStatsCollectionFailureReason = None # str
        
        #Name of interface on a device
        
        self.name = None # str
        
        #ID of interface on a device
        
        self.id = None # str
        
