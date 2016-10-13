#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FlowDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'protocol': 'str',
            
            
            'status': 'str',
            
            
            'codec': 'str',
            
            
            'applicationName': 'str',
            
            
            'flowType': 'str',
            
            
            'sourcePort': 'str',
            
            
            'destPort': 'str',
            
            
            'interfaceId': 'str',
            
            
            'interfaceName': 'str',
            
            
            'sourceIP': 'str',
            
            
            'destIP': 'str',
            
            
            'matchDSCP': 'str',
            
            
            'detailedFlowType': 'str',
            
            
            'averageBandwidth': 'str',
            
            
            'peakBandwidth': 'str',
            
            
            'clientReference': 'str',
            
            
            'networkDeviceId': 'str',
            
            
            'networkDeviceName': 'str',
            
            
            'failureReason': 'str'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'protocol': 'protocol',
            
            'status': 'status',
            
            'codec': 'codec',
            
            'applicationName': 'applicationName',
            
            'flowType': 'flowType',
            
            'sourcePort': 'sourcePort',
            
            'destPort': 'destPort',
            
            'interfaceId': 'interfaceId',
            
            'interfaceName': 'interfaceName',
            
            'sourceIP': 'sourceIP',
            
            'destIP': 'destIP',
            
            'matchDSCP': 'matchDSCP',
            
            'detailedFlowType': 'detailedFlowType',
            
            'averageBandwidth': 'averageBandwidth',
            
            'peakBandwidth': 'peakBandwidth',
            
            'clientReference': 'clientReference',
            
            'networkDeviceId': 'networkDeviceId',
            
            'networkDeviceName': 'networkDeviceName',
            
            'failureReason': 'failureReason'
            
        }       

        
        #id
        
        self.id = None # str
        
        #protocol
        
        self.protocol = None # str
        
        
        self.status = None # str
        
        #codec
        
        self.codec = None # str
        
        #APIC-EM application name
        
        self.applicationName = None # str
        
        #flowType
        
        self.flowType = None # str
        
        #sourcePort
        
        self.sourcePort = None # str
        
        #destPort
        
        self.destPort = None # str
        
        #interfaceId
        
        self.interfaceId = None # str
        
        #interfaceName
        
        self.interfaceName = None # str
        
        #sourceIP
        
        self.sourceIP = None # str
        
        #destIP
        
        self.destIP = None # str
        
        #DSCP of the flow
        
        self.matchDSCP = None # str
        
        #detailedFlowType (more detailed classification than flowType)
        
        self.detailedFlowType = None # str
        
        #averageBandwidth in kbps (min: 0, max: 2147483647 kbps)
        
        self.averageBandwidth = None # str
        
        #peakBandwidth in kbps (min: 0, max: 2147483647 kbps)
        
        self.peakBandwidth = None # str
        
        #clientReference (can be used by the client as a reference to this resource
        
        self.clientReference = None # str
        
        #networkDeviceId
        
        self.networkDeviceId = None # str
        
        #networkDeviceName
        
        self.networkDeviceName = None # str
        
        
        self.failureReason = None # str
        
