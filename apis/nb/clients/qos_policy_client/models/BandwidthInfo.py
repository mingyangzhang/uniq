#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.
class BandwidthInfo(object):
    def __init__(self):
        self.swaggerTypes = {
            'serviceClass': 'str',
            'dscp': 'str',
            'bandwidthPercent': 'int'
        }

        self.attributeMap = {
            'serviceClass': 'class',
            'dscp': 'dscp',
            'bandwidthPercent': 'bandwidthPercent'
        }

        self.serviceClass = None # str
        self.dscp = None  # str
        self.bandwidthPercent = None  # int
