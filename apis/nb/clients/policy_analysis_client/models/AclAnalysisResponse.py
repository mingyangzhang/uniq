#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AclAnalysisResponse(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'aclName': 'str',
            
            
            'matchingAces': 'list[AclAce]',
            
            
            'result': 'str'
            
        }

        self.attributeMap = {
            
            'aclName': 'aclName',
            
            'matchingAces': 'matchingAces',
            
            'result': 'result'
            
        }       

        
        
        self.aclName = None # str
        
        
        self.matchingAces = None # list[AclAce]
        
        
        self.result = None # str
        
