#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkElementInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'role': 'str',
            
            
            'ip': 'str',
            
            
            'linkInformationSource': 'str',
            
            
            'tunnels': 'list[str]',
            
            
            'accuracyList': 'list[Accuracy]',
            
            
            'perfMonCollection': 'str',
            
            
            'egressInterface': 'InterfaceContainer',
            
            
            'ingressInterface': 'InterfaceContainer',
            
            
            'deviceStatistics': 'DeviceStatistics',
            
            
            'perfMonCollectionFailureReason': 'str',
            
            
            'deviceStatsCollection': 'str',
            
            
            'deviceStatsCollectionFailureReason': 'str',
            
            
            'detailedStatus': 'DetailedStatus',
            
            
            'perfMonitorStatistics': 'list[PerfMonitorStatistics]',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'type': 'str'
            
        }

        self.attributeMap = {
            
            'role': 'role',
            
            'ip': 'ip',
            
            'linkInformationSource': 'linkInformationSource',
            
            'tunnels': 'tunnels',
            
            'accuracyList': 'accuracyList',
            
            'perfMonCollection': 'perfMonCollection',
            
            'egressInterface': 'egressInterface',
            
            'ingressInterface': 'ingressInterface',
            
            'deviceStatistics': 'deviceStatistics',
            
            'perfMonCollectionFailureReason': 'perfMonCollectionFailureReason',
            
            'deviceStatsCollection': 'deviceStatsCollection',
            
            'deviceStatsCollectionFailureReason': 'deviceStatsCollectionFailureReason',
            
            'detailedStatus': 'detailedStatus',
            
            'perfMonitorStatistics': 'perfMonitorStatistics',
            
            'name': 'name',
            
            'id': 'id',
            
            'type': 'type'
            
        }       

        
        #Role of device in network(can be access,core,distribution or border router)
        
        self.role = None # str
        
        #Network Device IP
        
        self.ip = None # str
        
        #The source of the link information to the next hop
        
        self.linkInformationSource = None # str
        
        #Tunnels this network element is in
        
        self.tunnels = None # list[str]
        
        
        self.accuracyList = None # list[Accuracy]
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.perfMonCollection = None # str
        
        #Egress interface of the network device
        
        self.egressInterface = None # InterfaceContainer
        
        #Ingress interface of the network device
        
        self.ingressInterface = None # InterfaceContainer
        
        #Device statistics
        
        self.deviceStatistics = None # DeviceStatistics
        
        
        self.perfMonCollectionFailureReason = None # str
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.deviceStatsCollection = None # str
        
        
        self.deviceStatsCollectionFailureReason = None # str
        
        
        self.detailedStatus = None # DetailedStatus
        
        #perf mon statistics on the device for give flow
        
        self.perfMonitorStatistics = None # list[PerfMonitorStatistics]
        
        #Network Device name
        
        self.name = None # str
        
        #Network Device ID
        
        self.id = None # str
        
        #Network Device Type(can be switch,router,wired host or wireless host)
        
        self.type = None # str
        
