#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AlarmDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'causedAlarmsUrl': 'str',


            'causingAlarmUrl': 'str',


            'alarmCreationTime': 'date-time',


            'applicationSpecificAlarmID': 'str',


            'eventCount': 'int',


            'isAcknowledged': 'bool',


            'lastModifiedTimestamp': 'date-time',


            'mayBeAutoCleared': 'bool',


            'ownerID': 'str',


            'previousSeverity': 'str',


            'subclassName': 'str',


            'causedAlarms': 'list[IdRef]',


            'causingAlarm': 'IdRef',


            'severity': 'str',


            'source': 'str',


            'description': 'str',


            'category': 'EventAlarmCategoryEnum',


            'eventAlarmDetailsUrl': 'str',


            'alarmDisplayable': 'bool',


            'applicationCategoryData': 'str',


            'deviceTimestamp': 'date-time',


            'isDeviceMaster': 'bool',


            'notificationDeliveryMechanism': 'str',


            'notificationState': 'int',


            'pendingUntil': 'date-time',


            'reportingEntityAddress': 'InetAddress',


            'sourceMacAddress': 'MacAddress',


            'srcObjectClassId': 'int',


            'srcObjectId': 'int',


            'stability': 'str',


            # 'transientNameValue': 'object',
            'transientNameValue' : 'dict',


            'eventAlarmDetails': 'list[IdRef]',


            'eventType': 'EventTypeEnum',


            'instanceUuid': 'str',


            'id': 'str'

        }

        self.attributeMap = {

            'causedAlarmsUrl': 'causedAlarmsUrl',

            'causingAlarmUrl': 'causingAlarmUrl',

            'alarmCreationTime': 'alarmCreationTime',

            'applicationSpecificAlarmID': 'applicationSpecificAlarmID',

            'eventCount': 'eventCount',

            'isAcknowledged': 'isAcknowledged',

            'lastModifiedTimestamp': 'lastModifiedTimestamp',

            'mayBeAutoCleared': 'mayBeAutoCleared',

            'ownerID': 'ownerID',

            'previousSeverity': 'previousSeverity',

            'subclassName': 'subclassName',

            'causedAlarms': 'causedAlarms',

            'causingAlarm': 'causingAlarm',

            'severity': 'severity',

            'source': 'source',

            'description': 'description',

            'category': 'category',

            'eventAlarmDetailsUrl': 'eventAlarmDetailsUrl',

            'alarmDisplayable': 'alarmDisplayable',

            'applicationCategoryData': 'applicationCategoryData',

            'deviceTimestamp': 'deviceTimestamp',

            'isDeviceMaster': 'isDeviceMaster',

            'notificationDeliveryMechanism': 'notificationDeliveryMechanism',

            'notificationState': 'notificationState',

            'pendingUntil': 'pendingUntil',

            'reportingEntityAddress': 'reportingEntityAddress',

            'sourceMacAddress': 'sourceMacAddress',

            'srcObjectClassId': 'srcObjectClassId',

            'srcObjectId': 'srcObjectId',

            'stability': 'stability',

            'transientNameValue': 'transientNameValue',

            'eventAlarmDetails': 'eventAlarmDetails',

            'eventType': 'eventType',

            'instanceUuid': 'instanceUuid',

            'id': 'id'

        }



        self.causedAlarmsUrl = None # str


        self.causingAlarmUrl = None # str


        self.alarmCreationTime = None # date-time


        self.applicationSpecificAlarmID = None # str


        self.eventCount = None # int


        self.isAcknowledged = None # bool


        self.lastModifiedTimestamp = None # date-time


        self.mayBeAutoCleared = None # bool


        self.ownerID = None # str


        self.previousSeverity = None # str


        self.subclassName = None # str


        self.causedAlarms = None # list[IdRef]


        self.causingAlarm = None # IdRef


        self.severity = None # str


        self.source = None # str


        self.description = None # str


        self.category = None # EventAlarmCategoryEnum


        self.eventAlarmDetailsUrl = None # str


        self.alarmDisplayable = None # bool


        self.applicationCategoryData = None # str


        self.deviceTimestamp = None # date-time


        self.isDeviceMaster = None # bool


        self.notificationDeliveryMechanism = None # str


        self.notificationState = None # int


        self.pendingUntil = None # date-time


        self.reportingEntityAddress = None # InetAddress


        self.sourceMacAddress = None # MacAddress


        self.srcObjectClassId = None # int


        self.srcObjectId = None # int


        self.stability = None # str


        self.transientNameValue = None # object


        self.eventAlarmDetails = None # list[IdRef]


        self.eventType = None # EventTypeEnum


        self.instanceUuid = None # str


        self.id = None # str

