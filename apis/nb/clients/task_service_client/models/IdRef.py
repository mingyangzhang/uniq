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

            'url': 'str',


            'id': 'int',


            'type': 'str'#,

            # Manually comment out this attribute
            # 'longType': 'Class«object»'

        }

        self.attributeMap = {

            'url': 'url',

            'id': 'id',

            'type': 'type'#,

            # Manually comment out this attribute
            # 'longType': 'longType'

        }



        self.url = None # str


        self.id = None # int


        self.type = None # str


        # Manually comment out this attribute
        # self.longType = None # Class«object»

