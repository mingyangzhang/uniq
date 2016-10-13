#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.

class UnprovisionedSite(object):
    """ Class to provision IWAN branch unprovisioned site """


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """

        self.swaggerTypes = {
            'siteName': 'str',
            'siteLocation': 'str',
            'latitude': 'str',
            'longitude': 'str',
            'siteDevice': 'UnclaimedDevice'
        }

        self.attributeMap = {
            'siteName': 'siteName',
            'siteLocation': 'siteLocation',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'siteDevice': 'siteDevice',
        }

        self.siteName = None
        self.siteLocation = None
        self.latitude = None
        self.longitude = None
        self.siteDevice = None
