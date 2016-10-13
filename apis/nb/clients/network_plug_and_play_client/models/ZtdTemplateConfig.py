#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdTemplateConfig(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'description': 'str',


            'id': 'str',


            'configId': 'str',


            'templateId': 'str',


            'configProperty': 'dict',


            'configIdTimestamp': 'str',


            'configPropertyTimestamp': 'str',


            'generate': 'bool',


            'name': 'str'
        }

        self.attributeMap = {

            'description': 'description',

            'id': 'id',

            'configId': 'configId',

            'templateId': 'templateId',

            'configProperty': 'configProperty',

            'configIdTimestamp': 'configIdTimestamp',

            'configPropertyTimestamp': 'configPropertyTimestamp',

            'generate': 'generate',

            'name': 'name'
        }


        #Template config description

        self.description = None # str

        #Template config ID

        self.id = None # str


        self.configId = None # str

        #Template ID

        self.templateId = None # str

        #Template varialble key-value pairs

        self.configProperty = None # dict


        self.configIdTimestamp = None # str


        self.configPropertyTimestamp = None # str

        #True to generate template

        self.generate = None # bool

        #Template config name

        self.name = None # str
