#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class IdRef(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'type': 'str',


            'id': 'int',


            'url': 'str',


            'longType': 'Class«object»'

        }

        self.attributeMap = {

            'type': 'type',

            'id': 'id',

            'url': 'url',

            'longType': 'longType'

        }



        self.type = None # str


        self.id = None # int


        self.url = None # str


        self.longType = None # Class«object»

