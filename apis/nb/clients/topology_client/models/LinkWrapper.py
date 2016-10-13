#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LinkWrapper(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'source': 'str',
            
            
            'id': 'str',
            
            
            'startPortID': 'str',
            
            
            'endPortID': 'str',
            
            
            'greyOut': 'bool',
            
            
            'linkStatus': 'str',
            
            
            'tag': 'str',
            
            
            'endPortName': 'str',
            
            
            'endPortSpeed': 'str',
            
            
            'startPortName': 'str',
            
            
            'startPortSpeed': 'str',
            
            
            'startPortIpv4Mask': 'str',
            
            
            'endPortIpv4Address': 'str',
            
            
            'endPortIpv4Mask': 'str',
            
            
            'startPortIpv4Address': 'str',
            
            
            'target': 'str'
            
        }

        self.attributeMap = {
            
            'source': 'source',
            
            'id': 'id',
            
            'startPortID': 'startPortID',
            
            'endPortID': 'endPortID',
            
            'greyOut': 'greyOut',
            
            'linkStatus': 'linkStatus',
            
            'tag': 'tag',
            
            'endPortName': 'endPortName',
            
            'endPortSpeed': 'endPortSpeed',
            
            'startPortName': 'startPortName',
            
            'startPortSpeed': 'startPortSpeed',
            
            'startPortIpv4Mask': 'startPortIpv4Mask',
            
            'endPortIpv4Address': 'endPortIpv4Address',
            
            'endPortIpv4Mask': 'endPortIpv4Mask',
            
            'startPortIpv4Address': 'startPortIpv4Address',
            
            'target': 'target'
            
        }       

        
        #Device ID correspondng to the source device 
        
        self.source = None # str
        
        #Unified identifier for device
        
        self.id = None # str
        
        #Device port ID corresponding to start devices
        
        self.startPortID = None # str
        
        #Device port ID corresponding to end devices
        
        self.endPortID = None # str
        
        #Device greyout
        
        self.greyOut = None # bool
        
        #Indicates whether link is working
        
        self.linkStatus = None # str
        
        #Tag for the devices
        
        self.tag = None # str
        
        #Interface port name corresponding to end devices
        
        self.endPortName = None # str
        
        #Interface port speed corresponding to end devices
        
        self.endPortSpeed = None # str
        
        #Interface port name corresponding to start devices
        
        self.startPortName = None # str
        
        #Interface port speed corresponding to start devices
        
        self.startPortSpeed = None # str
        
        #Interface port IPv4 mask corresponding to start devices
        
        self.startPortIpv4Mask = None # str
        
        #Interface port IPv4 address corresponding to end devices
        
        self.endPortIpv4Address = None # str
        
        #Interface port IPv4 mask corresponding to end devices
        
        self.endPortIpv4Mask = None # str
        
        #Interface port IPv4 address corresponding to start devices
        
        self.startPortIpv4Address = None # str
        
        #Device ID corresponding to the target device
        
        self.target = None # str
        
