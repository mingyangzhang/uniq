#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class PerfMonitorStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'sourcePort': 'str',
            
            
            'destPort': 'str',
            
            
            'byteRate': 'int',
            
            
            'inputInterface': 'str',
            
            
            'ipv4DSCP': 'str',
            
            
            'ipv4TTL': 'int',
            
            
            'outputInterface': 'str',
            
            
            'packetCount': 'int',
            
            
            'packetLoss': 'int',
            
            
            'packetLossPercentage': 'float',
            
            
            'refreshedAt': 'int',
            
            
            'rtpJitterMean': 'int',
            
            
            'rtpJitterMax': 'int',
            
            
            'sourceIpAddress': 'str',
            
            
            'destIpAddress': 'str',
            
            
            'rtpJitterMin': 'int',
            
            
            'packetBytes': 'int',
            
            
            'protocol': 'str'
            
        }

        self.attributeMap = {
            
            'sourcePort': 'sourcePort',
            
            'destPort': 'destPort',
            
            'byteRate': 'byteRate',
            
            'inputInterface': 'inputInterface',
            
            'ipv4DSCP': 'ipv4DSCP',
            
            'ipv4TTL': 'ipv4TTL',
            
            'outputInterface': 'outputInterface',
            
            'packetCount': 'packetCount',
            
            'packetLoss': 'packetLoss',
            
            'packetLossPercentage': 'packetLossPercentage',
            
            'refreshedAt': 'refreshedAt',
            
            'rtpJitterMean': 'rtpJitterMean',
            
            'rtpJitterMax': 'rtpJitterMax',
            
            'sourceIpAddress': 'sourceIpAddress',
            
            'destIpAddress': 'destIpAddress',
            
            'rtpJitterMin': 'rtpJitterMin',
            
            'packetBytes': 'packetBytes',
            
            'protocol': 'protocol'
            
        }       

        
        
        self.sourcePort = None # str
        
        
        self.destPort = None # str
        
        
        self.byteRate = None # int
        
        
        self.inputInterface = None # str
        
        
        self.ipv4DSCP = None # str
        
        
        self.ipv4TTL = None # int
        
        
        self.outputInterface = None # str
        
        
        self.packetCount = None # int
        
        
        self.packetLoss = None # int
        
        
        self.packetLossPercentage = None # float
        
        
        self.refreshedAt = None # int
        
        
        self.rtpJitterMean = None # int
        
        
        self.rtpJitterMax = None # int
        
        
        self.sourceIpAddress = None # str
        
        
        self.destIpAddress = None # str
        
        
        self.rtpJitterMin = None # int
        
        
        self.packetBytes = None # int
        
        
        self.protocol = None # str
        
