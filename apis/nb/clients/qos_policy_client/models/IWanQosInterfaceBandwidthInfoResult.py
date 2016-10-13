#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.
class IWanQosInterfaceBandwidthInfoResult(object):
    def __init__(self):
        self.swaggerTypes = {
            'version': 'str',
            'response': 'IWanQosInterfaceBandwidthInfo'
        }

        self.attributeMap = {
            'version': 'version',
            'response': 'response'
        }

        self.version = None # str
        self.response = None # IWanQosInterfaceBandwidthInfo