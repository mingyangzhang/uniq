#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AclAce(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'ace': 'str',
            
            
            'matchingPorts': 'list[AclMatchingPorts]',
            
            
            'result': 'str'
            
        }

        self.attributeMap = {
            
            'ace': 'ace',
            
            'matchingPorts': 'matchingPorts',
            
            'result': 'result'
            
        }       

        
        
        self.ace = None # str
        
        
        self.matchingPorts = None # list[AclMatchingPorts]
        
        
        self.result = None # str
        
