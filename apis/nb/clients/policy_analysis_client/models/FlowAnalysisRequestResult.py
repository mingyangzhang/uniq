#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FlowAnalysisRequestResult(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'url': 'str',
            
            
            'taskId': 'str',
            
            
            'flowAnalysisId': 'str'
            
        }

        self.attributeMap = {
            
            'url': 'url',
            
            'taskId': 'taskId',
            
            'flowAnalysisId': 'flowAnalysisId'
            
        }       

        
        
        self.url = None # str
        
        
        self.taskId = None # str
        
        
        self.flowAnalysisId = None # str
        
