#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class AugmentedAuditResourceDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'instanceUuid': 'str',


            'tag': 'str',


            'hasParent': 'bool',


            'createdDateTime': 'date-time',


            'auditId': 'str',


            'auditParentId': 'str',


            'auditRequestor': 'str',


            'auditDescription': 'str',


            'derivedParentId': 'str',


            'deviceIP': 'str',


            'deviceName': 'str',


            'siteName': 'str',


            'hasChildren': 'bool',


            'auditParameters': 'str',


            'persistDateTime': 'date-time',


            'state': 'str'

        }

        self.attributeMap = {

            'instanceUuid': 'instanceUuid',

            'tag': 'tag',

            'hasParent': 'hasParent',

            'createdDateTime': 'createdDateTime',

            'auditId': 'auditId',

            'auditParentId': 'auditParentId',

            'auditRequestor': 'auditRequestor',

            'auditDescription': 'auditDescription',

            'derivedParentId': 'derivedParentId',

            'deviceIP': 'deviceIP',

            'deviceName': 'deviceName',

            'siteName': 'siteName',

            'hasChildren': 'hasChildren',

            'auditParameters': 'auditParameters',

            'persistDateTime': 'persistDateTime',

            'state': 'state'

        }


        #This field is deprecated. Use &#39;id&#39; instead.

        self.instanceUuid = None # str


        self.tag = None # str


        self.hasParent = None # bool


        self.createdDateTime = None # date-time


        self.auditId = None # str


        self.auditParentId = None # str


        self.auditRequestor = None # str


        self.auditDescription = None # str


        self.derivedParentId = None # str


        self.deviceIP = None # str


        self.deviceName = None # str


        self.siteName = None # str


        self.hasChildren = None # bool


        self.auditParameters = None # str


        self.persistDateTime = None # date-time


        self.state = None # str

