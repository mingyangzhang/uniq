#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class DiscoveryJobNIO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'snmpStatus': 'str',


            'cliStatus': 'str',


            'pingStatus': 'str',


            'inventoryReachabilityStatus': 'str',


            'startTime': 'str',


            'endTime': 'str',


            'jobStatus': 'str',


            'inventoryCollectionStatus': 'str',


            'taskId': 'str',


            'ipAddress': 'str',


            'discoveryStatus': 'str',


            'name': 'str',


            'id': 'str',


            'attributeInfo': 'object'

        }

        self.attributeMap = {

            'snmpStatus': 'snmpStatus',

            'cliStatus': 'cliStatus',

            'pingStatus': 'pingStatus',

            'inventoryReachabilityStatus': 'inventoryReachabilityStatus',

            'startTime': 'startTime',

            'endTime': 'endTime',

            'jobStatus': 'jobStatus',

            'inventoryCollectionStatus': 'inventoryCollectionStatus',

            'taskId': 'taskId',

            'ipAddress': 'ipAddress',

            'discoveryStatus': 'discoveryStatus',

            'name': 'name',

            'id': 'id',

            'attributeInfo': 'attributeInfo'

        }


        #SNMP status for the IP during this job run

        self.snmpStatus = None # str

        #CLI status for the IP during this job run

        self.cliStatus = None # str

        #Ping status for the IP during this job run

        self.pingStatus = None # str

        #Last known reachabilty status of the device

        self.inventoryReachabilityStatus = None # str

        #Discovery job start time

        self.startTime = None # str


        self.endTime = None # str


        self.jobStatus = None # str

        #Last known inventory collection status of the device

        self.inventoryCollectionStatus = None # str

        #Discovery job task id

        self.taskId = None # str

        #IP Address

        self.ipAddress = None # str

        #Discovery status for the IP

        self.discoveryStatus = None # str

        #Discovery job name

        self.name = None # str


        self.id = None # str


        self.attributeInfo = None # object

