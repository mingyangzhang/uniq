#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CpuStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'refreshedAt': 'int',
            
            
            'fiveMinUsageInPercentage': 'float',
            
            
            'fiveSecsUsageInPercentage': 'float',
            
            
            'oneMinUsageInPercentage': 'float'
            
        }

        self.attributeMap = {
            
            'refreshedAt': 'refreshedAt',
            
            'fiveMinUsageInPercentage': 'fiveMinUsageInPercentage',
            
            'fiveSecsUsageInPercentage': 'fiveSecsUsageInPercentage',
            
            'oneMinUsageInPercentage': 'oneMinUsageInPercentage'
            
        }       

        
        
        self.refreshedAt = None # int
        
        
        self.fiveMinUsageInPercentage = None # float
        
        
        self.fiveSecsUsageInPercentage = None # float
        
        
        self.oneMinUsageInPercentage = None # float
        
