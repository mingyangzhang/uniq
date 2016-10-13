#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.
class IWanQosInterfaceBandwidthInfo(object):
    def __init__(self):
        self.swaggerTypes = {
            'interfaceId': 'str',
            'bandwidthAllocations': 'list[BandwidthInfo]',
        }

        self.attributeMap = {
            'interfaceId': 'interfaceId',
            'bandwidthAllocations': 'bandwidthAllocations',
        }

        self.interfaceId = None # str
        self.bandwidthAllocations = None # list[BandwidthInfo]
