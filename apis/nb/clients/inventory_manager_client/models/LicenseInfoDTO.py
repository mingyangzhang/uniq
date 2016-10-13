#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class LicenseInfoDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'id': 'str',
            
            
            'deployPending': 'int',
            
            
            'evalPeriodLeft': 'str',
            
            
            'usageCount': 'int',
            
            
            'type': 'str',
            
            
            'isCounted': 'bool',
            
            
            'validityPeriodRemaining': 'int',
            
            
            'attributeInfo': 'object',
            
            
            'storeName': 'str',
            
            
            'validityPeriod': 'int',
            
            
            'storedUsed': 'int',
            
            
            'featureVersion': 'str',
            
            
            'hostId': 'str',
            
            
            'evalPeriodUsed': 'str',
            
            
            'totalCount': 'int',
            
            
            'usageCountRemaining': 'int',
            
            
            'physicalIndex': 'str',
            
            
            'isEulaAccepted': 'bool',
            
            
            'expiredDate': 'str',
            
            
            'description': 'str',
            
            
            'status': 'str',
            
            
            'isEulaApplicable': 'bool',
            
            
            'provisionState': 'int',
            
            
            'parentId': 'int',
            
            
            'maxUsageCount': 'int',
            
            
            'eulaStatus': 'bool',
            
            
            'priority': 'str',
            
            
            'name': 'str',
            
            
            'counted': 'bool',
            
            
            'licenseFileCount': 'int',
            
            
            'isTechnologyLicense': 'bool',
            
            
            'licenseFileName': 'str',
            
            
            'licenseIndex': 'int',
            
            
            'expiredPeriod': 'int'
            
        }

        self.attributeMap = {
            
            'id': 'id',
            
            'deployPending': 'deployPending',
            
            'evalPeriodLeft': 'evalPeriodLeft',
            
            'usageCount': 'usageCount',
            
            'type': 'type',
            
            'isCounted': 'isCounted',
            
            'validityPeriodRemaining': 'validityPeriodRemaining',
            
            'attributeInfo': 'attributeInfo',
            
            'storeName': 'storeName',
            
            'validityPeriod': 'validityPeriod',
            
            'storedUsed': 'storedUsed',
            
            'featureVersion': 'featureVersion',
            
            'hostId': 'hostId',
            
            'evalPeriodUsed': 'evalPeriodUsed',
            
            'totalCount': 'totalCount',
            
            'usageCountRemaining': 'usageCountRemaining',
            
            'physicalIndex': 'physicalIndex',
            
            'isEulaAccepted': 'isEulaAccepted',
            
            'expiredDate': 'expiredDate',
            
            'description': 'description',
            
            'status': 'status',
            
            'isEulaApplicable': 'isEulaApplicable',
            
            'provisionState': 'provisionState',
            
            'parentId': 'parentId',
            
            'maxUsageCount': 'maxUsageCount',
            
            'eulaStatus': 'eulaStatus',
            
            'priority': 'priority',
            
            'name': 'name',
            
            'counted': 'counted',
            
            'licenseFileCount': 'licenseFileCount',
            
            'isTechnologyLicense': 'isTechnologyLicense',
            
            'licenseFileName': 'licenseFileName',
            
            'licenseIndex': 'licenseIndex',
            
            'expiredPeriod': 'expiredPeriod'
            
        }       

        
        #ID of license
        
        self.id = None # str
        
        #Deploy Pending information of license
        
        self.deployPending = None # int
        
        #Number of days remaining in the eval period
        
        self.evalPeriodLeft = None # str
        
        #Usage count of the license feature
        
        self.usageCount = None # int
        
        #License type
        
        self.type = None # str
        
        #If the license is counted as part of license usage
        
        self.isCounted = None # bool
        
        #Remaining validityPeriod
        
        self.validityPeriodRemaining = None # int
        
        
        self.attributeInfo = None # object
        
        #Name of the license Store
        
        self.storeName = None # str
        
        #Validity period the the license
        
        self.validityPeriod = None # int
        
        #License store usage detail
        
        self.storedUsed = None # int
        
        #Version of the license feature
        
        self.featureVersion = None # str
        
        #Device Id/Name of the license info
        
        self.hostId = None # str
        
        #Number of days used in the eval period
        
        self.evalPeriodUsed = None # str
        
        #Number of license installed in the device
        
        self.totalCount = None # int
        
        #Unused license count
        
        self.usageCountRemaining = None # int
        
        #Physical entity index
        
        self.physicalIndex = None # str
        
        #If the EULA is accepted
        
        self.isEulaAccepted = None # bool
        
        #Expired date of the license
        
        self.expiredDate = None # str
        
        #Description about the license
        
        self.description = None # str
        
        #Status of the license
        
        self.status = None # str
        
        #If the EULA is applicable
        
        self.isEulaApplicable = None # bool
        
        #Provision state of the license feature
        
        self.provisionState = None # int
        
        #Parent Id of the license
        
        self.parentId = None # int
        
        #Maximum usage of the license feature
        
        self.maxUsageCount = None # int
        
        #EULA status of the license
        
        self.eulaStatus = None # bool
        
        #License priority
        
        self.priority = None # str
        
        #Name of the license feature
        
        self.name = None # str
        
        #If license feature is counted as part of the license
        
        self.counted = None # bool
        
        #Number of license file
        
        self.licenseFileCount = None # int
        
        #If the license is technology license or not
        
        self.isTechnologyLicense = None # bool
        
        #Name of license file
        
        self.licenseFileName = None # str
        
        #Index of the license
        
        self.licenseIndex = None # int
        
        #License expired period
        
        self.expiredPeriod = None # int
        
