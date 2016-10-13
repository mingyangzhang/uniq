#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class SiteManagementInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'description': 'str',


            'deviceIds': 'list[str]',


            'name': 'str',


            'location': 'str',

            #changed this manually from 'object' to 'dict'
            'properties': 'dict',


            'id': 'str'

        }

        self.attributeMap = {

            'description': 'description',

            'deviceIds': 'deviceIds',

            'name': 'name',

            'location': 'location',

            'properties': 'properties',

            'id': 'id'

        }


        #Description of site

        self.description = None # str

        #Unique identifier of devices that are associated with site

        self.deviceIds = None # list[str]

        #Name of site

        self.name = None # str

        #Location of site

        self.location = None # str

        #Properties of site

        self.properties = None # dict #changed this manually from 'object' to 'dict'

        #Unique identifier of site

        self.id = None # str

