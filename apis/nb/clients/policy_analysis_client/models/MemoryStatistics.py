#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class MemoryStatistics(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'memoryUsage': 'int',
            
            
            'refreshedAt': 'int',
            
            
            'totalMemory': 'int'
            
        }

        self.attributeMap = {
            
            'memoryUsage': 'memoryUsage',
            
            'refreshedAt': 'refreshedAt',
            
            'totalMemory': 'totalMemory'
            
        }       

        
        
        self.memoryUsage = None # int
        
        
        self.refreshedAt = None # int
        
        
        self.totalMemory = None # int
        
