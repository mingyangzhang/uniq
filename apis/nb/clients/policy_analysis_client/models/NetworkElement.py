#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class NetworkElement(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'role': 'str',
            
            
            'ip': 'str',
            
            
            'ingressVirtualInterface': 'Interface',
            
            
            'egressVirtualInterface': 'Interface',
            
            
            'ingressPhysicalInterface': 'Interface',
            
            
            'egressPhysicalInterface': 'Interface',
            
            
            'linkInformationSource': 'str',
            
            
            'tunnels': 'list[str]',
            
            
            'accuracyList': 'list[Accuracy]',
            
            
            'perfMonCollection': 'str',
            
            
            'deviceStatistics': 'DeviceStatistics',
            
            
            'perfMonStatistics': 'list[PerfMonitorStatistics]',
            
            
            'perfMonCollectionFailureReason': 'str',
            
            
            'deviceStatsCollection': 'str',
            
            
            'deviceStatsCollectionFailureReason': 'str',
            
            
            'detailedStatus': 'DetailedStatus',
            
            
            'name': 'str',
            
            
            'id': 'str',
            
            
            'type': 'str'
            
        }

        self.attributeMap = {
            
            'role': 'role',
            
            'ip': 'ip',
            
            'ingressVirtualInterface': 'ingressVirtualInterface',
            
            'egressVirtualInterface': 'egressVirtualInterface',
            
            'ingressPhysicalInterface': 'ingressPhysicalInterface',
            
            'egressPhysicalInterface': 'egressPhysicalInterface',
            
            'linkInformationSource': 'linkInformationSource',
            
            'tunnels': 'tunnels',
            
            'accuracyList': 'accuracyList',
            
            'perfMonCollection': 'perfMonCollection',
            
            'deviceStatistics': 'deviceStatistics',
            
            'perfMonStatistics': 'perfMonStatistics',
            
            'perfMonCollectionFailureReason': 'perfMonCollectionFailureReason',
            
            'deviceStatsCollection': 'deviceStatsCollection',
            
            'deviceStatsCollectionFailureReason': 'deviceStatsCollectionFailureReason',
            
            'detailedStatus': 'detailedStatus',
            
            'name': 'name',
            
            'id': 'id',
            
            'type': 'type'
            
        }       

        
        #Role of device in network(can be access,core,distribution or border router)
        
        self.role = None # str
        
        #Network Device IP
        
        self.ip = None # str
        
        #Ingress virtual interface of the network device
        
        self.ingressVirtualInterface = None # Interface
        
        #Egress virtual interface of the network device
        
        self.egressVirtualInterface = None # Interface
        
        #Igress physical interface of the network device
        
        self.ingressPhysicalInterface = None # Interface
        
        #Egress physical interface of the network device
        
        self.egressPhysicalInterface = None # Interface
        
        #The source of the link information to the next hop
        
        self.linkInformationSource = None # str
        
        #Tunnels this network element is in
        
        self.tunnels = None # list[str]
        
        
        self.accuracyList = None # list[Accuracy]
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.perfMonCollection = None # str
        
        
        self.deviceStatistics = None # DeviceStatistics
        
        
        self.perfMonStatistics = None # list[PerfMonitorStatistics]
        
        
        self.perfMonCollectionFailureReason = None # str
        
        #A status value from [ INPROGRESS, SUCCESS, FAILED ] 
        
        self.deviceStatsCollection = None # str
        
        
        self.deviceStatsCollectionFailureReason = None # str
        
        
        self.detailedStatus = None # DetailedStatus
        
        #Network Device name
        
        self.name = None # str
        
        #Network Device ID
        
        self.id = None # str
        
        #Network Device Type(can be switch,router,wired host or wireless host)
        
        self.type = None # str
        
