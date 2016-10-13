#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ApicEmUserDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'hosts': 'list[HostBriefDTO]',
            
            
            'name': 'str'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'hosts': 'hosts',
            
            'name': 'name'
            
        }       

        
        
        self.description = None # str
        
        
        self.hosts = None # list[HostBriefDTO]
        
        
        self.name = None # str
        
