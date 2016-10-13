#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class InterfaceContainer(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'physicalInterface': 'Interface',
            
            
            'virtualInterface': 'list[Interface]'
            
        }

        self.attributeMap = {
            
            'physicalInterface': 'physicalInterface',
            
            'virtualInterface': 'virtualInterface'
            
        }       

        
        #ID of Physical interface on a device
        
        self.physicalInterface = None # Interface
        
        #A list of Virtual interface IDs on a device
        
        self.virtualInterface = None # list[Interface]
        
