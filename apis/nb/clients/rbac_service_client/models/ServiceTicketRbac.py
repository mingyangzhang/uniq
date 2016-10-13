#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ServiceTicketRbac(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'idleTimeout': 'int',
            
            
            'serviceTicket': 'str',
            
            
            'sessionTimeout': 'int'
            
        }

        self.attributeMap = {
            
            'idleTimeout': 'idleTimeout',
            
            'serviceTicket': 'serviceTicket',
            
            'sessionTimeout': 'sessionTimeout'
            
        }       

        
        
        self.idleTimeout = None # int
        
        #Service Ticket to be used as authentication Ticket
        
        self.serviceTicket = None # str
        
        
        self.sessionTimeout = None # int
        
