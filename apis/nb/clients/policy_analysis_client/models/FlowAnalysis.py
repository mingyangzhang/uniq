#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FlowAnalysis(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'status': 'str',
            
            
            'createTime': 'int',
            
            
            'failureReason': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'id': 'str',
            
            
            'sourceIP': 'str',
            
            
            'destIP': 'str',
            
            
            'sourcePort': 'str',
            
            
            'destPort': 'str',
            
            
            'inclusions': 'list[str]',
            
            
            'periodicRefresh': 'bool',
            
            
            'protocol': 'str'
            
        }

        self.attributeMap = {
            
            'status': 'status',
            
            'createTime': 'createTime',
            
            'failureReason': 'failureReason',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'id': 'id',
            
            'sourceIP': 'sourceIP',
            
            'destIP': 'destIP',
            
            'sourcePort': 'sourcePort',
            
            'destPort': 'destPort',
            
            'inclusions': 'inclusions',
            
            'periodicRefresh': 'periodicRefresh',
            
            'protocol': 'protocol'
            
        }       

        
        #Aggregated status of flow-analysis request. Value from a set of [INPROGRESS, COMPLETED, FAILED] 
        
        self.status = None # str
        
        #Flow analysis request creation time
        
        self.createTime = None # int
        
        
        self.failureReason = None # str
        
        #Flow analysis request last update time
        
        self.lastUpdateTime = None # int
        
        #
        
        self.id = None # str
        
        #Source IP address
        
        self.sourceIP = None # str
        
        #Destination IP address
        
        self.destIP = None # str
        
        #Source Port
        
        self.sourcePort = None # str
        
        #Destination Port
        
        self.destPort = None # str
        
        #Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS, ACL-TRACE}
        
        self.inclusions = None # list[str]
        
        #periodicRefresh of path for every 30 sec
        
        self.periodicRefresh = None # bool
        
        #Protocol
        
        self.protocol = None # str
        
