#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class QosClassMapStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'classMapName': 'str',
            
            
            'refreshedAt': 'int',
            
            
            'queueDepth': 'int',
            
            
            'dropRate': 'int',
            
            
            'numBytes': 'int',
            
            
            'numPackets': 'int',
            
            
            'offeredRate': 'int',
            
            
            'queueBandwidthbps': 'str',
            
            
            'queueNoBufferDrops': 'int',
            
            
            'queueTotalDrops': 'int'
            
        }

        self.attributeMap = {
            
            'classMapName': 'classMapName',
            
            'refreshedAt': 'refreshedAt',
            
            'queueDepth': 'queueDepth',
            
            'dropRate': 'dropRate',
            
            'numBytes': 'numBytes',
            
            'numPackets': 'numPackets',
            
            'offeredRate': 'offeredRate',
            
            'queueBandwidthbps': 'queueBandwidthbps',
            
            'queueNoBufferDrops': 'queueNoBufferDrops',
            
            'queueTotalDrops': 'queueTotalDrops'
            
        }       

        
        
        self.classMapName = None # str
        
        
        self.refreshedAt = None # int
        
        
        self.queueDepth = None # int
        
        
        self.dropRate = None # int
        
        
        self.numBytes = None # int
        
        
        self.numPackets = None # int
        
        
        self.offeredRate = None # int
        
        
        self.queueBandwidthbps = None # str
        
        
        self.queueNoBufferDrops = None # int
        
        
        self.queueTotalDrops = None # int
        
