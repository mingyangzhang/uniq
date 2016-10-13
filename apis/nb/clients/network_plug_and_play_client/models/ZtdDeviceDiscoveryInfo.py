#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ZtdDeviceDiscoveryInfo(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'timeout': 'int',


            'name': 'str',


            'enablePasswordList': 'list[str]',


            'ipFilterList': 'list[str]',


            'snmpVersion': 'str',


            'cdpLevel': 'int',


            'passwordList': 'list[str]',


            'protocolOrder': 'str',


            'reDiscovery': 'bool',


            'retry': 'int',


            'snmpAuthPassphrase': 'str',


            'snmpAuthProtocol': 'str',


            'snmpPrivPassphrase': 'str',


            'snmpPrivProtocol': 'str',


            'snmpROCommunity': 'str',


            'snmpRWCommunity': 'str',


            'snmpUserName': 'str',


            'userNameList': 'list[str]',


            'snmpMode': 'str',


            'discoveryType': 'str',


            'ipAddressList': 'str',


            'globalCredentialIdList': 'list[str]'

        }

        self.attributeMap = {

            'timeout': 'timeout',

            'name': 'name',

            'enablePasswordList': 'enablePasswordList',

            'ipFilterList': 'ipFilterList',

            'snmpVersion': 'snmpVersion',

            'cdpLevel': 'cdpLevel',

            'passwordList': 'passwordList',

            'protocolOrder': 'protocolOrder',

            'reDiscovery': 'reDiscovery',

            'retry': 'retry',

            'snmpAuthPassphrase': 'snmpAuthPassphrase',

            'snmpAuthProtocol': 'snmpAuthProtocol',

            'snmpPrivPassphrase': 'snmpPrivPassphrase',

            'snmpPrivProtocol': 'snmpPrivProtocol',

            'snmpROCommunity': 'snmpROCommunity',

            'snmpRWCommunity': 'snmpRWCommunity',

            'snmpUserName': 'snmpUserName',

            'userNameList': 'userNameList',

            'snmpMode': 'snmpMode',

            'discoveryType': 'discoveryType',

            'ipAddressList': 'ipAddressList',

            'globalCredentialIdList': 'globalCredentialIdList'

        }


        #Time to wait for device response in seconds

        self.timeout = None # int

        #Name for discovery

        self.name = None # str

        #Enable Password of the devices to be discovered

        self.enablePasswordList = None # list[str]

        #Username of the devices to be discovered

        self.ipFilterList = None # list[str]

        #Version of SNMP. Can be v2 or v3

        self.snmpVersion = None # str

        #CDP level to which neighbor devices to be discovered

        self.cdpLevel = None # int

        #Password of the devices to be discovered

        self.passwordList = None # list[str]

        #Order of protocol in which device connection establishment to be tried

        self.protocolOrder = None # str

        #Flag to indicate is rediscovery or not

        self.reDiscovery = None # bool

        #Number of times to try establishing connection to device

        self.retry = None # int

        #Auth Pass phrase for SNMP

        self.snmpAuthPassphrase = None # str

        #SNMP auth protocol. Available values:&#39;SHA&#39; or &#39;MD5&#39;

        self.snmpAuthProtocol = None # str

        #Pass phrase for SNMP privacy

        self.snmpPrivPassphrase = None # str

        #SNMP privacy protocol. Available values:&#39;DES&#39; or &#39;AES128&#39;

        self.snmpPrivProtocol = None # str

        #Snmp RO community of the devices to be discovered

        self.snmpROCommunity = None # str

        #Snmp RW community of the devices to be discovered

        self.snmpRWCommunity = None # str

        #SNMP username of the device

        self.snmpUserName = None # str

        #Username of the devices to be discovered

        self.userNameList = None # list[str]

        #Mode of SNMP. Available values:&#39;AUTHPRIV&#39; or &#39;AUTHNOPRIV&#39; or &#39;NOAUTHNOPRIV&#39;

        self.snmpMode = None # str

        #Available types are: single, auto cdp discovery, range, multi range

        self.discoveryType = None # str

        #Ip address of the device to be discovered

        self.ipAddressList = None # str

        #List of global credential ids to be used

        self.globalCredentialIdList = None # list[str]

