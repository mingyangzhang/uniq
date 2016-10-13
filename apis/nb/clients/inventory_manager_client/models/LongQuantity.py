#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LongQuantity(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'longAmount': 'int',


            'units': 'str',


            'instanceId': 'int',


            'instanceUuid': 'str',


            'instanceVersion': 'int'

        }

        self.attributeMap = {

            'longAmount': 'longAmount',

            'units': 'units',

            'instanceId': 'instanceId',

            'instanceUuid': 'instanceUuid',

            'instanceVersion': 'instanceVersion'

        }



        self.longAmount = None # int


        self.units = None # str


        self.instanceId = None # int


        self.instanceUuid = None # str


        self.instanceVersion = None # int

