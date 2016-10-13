#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class NetworkdeviceApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getAllNetworkDevice(self, **kwargs):
        """Retrieves the network devices by filters

        Args:

            scope, str: Authorization Scope for RBAC (required)


        #changed this manually from 'object' to 'NetworkDeviceListResult'
        Returns: NetworkDeviceListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllNetworkDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        #changed this manually from 'object' to 'NetworkDeviceListResult'
        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceListResult')
        return responseObject




    def updateNetworkDevice(self, **kwargs):
        """Updates network device role

        Args:

            networkDeviceBriefNIO, NetworkDeviceBriefNIO: networkDeviceBriefNIO (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['networkDeviceBriefNIO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateNetworkDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/brief'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('networkDeviceBriefNIO' in params):
            bodyParam = params['networkDeviceBriefNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getRunningConfig(self, **kwargs):
        """Retrieves device config list

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: RawCliInfoNIOListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getRunningConfig" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/config'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'RawCliInfoNIOListResult')
        return responseObject




    def getNetworkConfigCount(self, **kwargs):
        """Retrieves config count

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkConfigCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/config/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getNetworkDeviceCount(self, **kwargs):
        """Retrieves network device count by filters

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getNetworkDeviceByIp(self, **kwargs):
        """Retrieves network device by IP address

        Args:

            ipAddress, str: Device IP address (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceResult
        """

        allParams = ['ipAddress', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceByIp" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/ip-address/{ipAddress}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('ipAddress' in params):
            replacement = str(self.apiClient.toPathValue(params['ipAddress']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'ipAddress' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceResult')
        return responseObject




    def getNetworkDeviceLocation(self, **kwargs):
        """Retrieves device location

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceListResult')
        return responseObject




    def addNetworkDeviceLocation(self, **kwargs):
        """Associates location with device

        Args:

            networkDeviceNIO, NetworkDeviceNIO: networkDeviceNIO (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['networkDeviceNIO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addNetworkDeviceLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']







        if ('networkDeviceNIO' in params):
            bodyParam = params['networkDeviceNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getNetworkDeviceByLocationId(self, **kwargs):
        """Retrieves network device by location ID

        Args:

            locationId, str: Location ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceListResult
        """

        allParams = ['locationId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceByLocationId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/location/{locationId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('locationId' in params):
            replacement = str(self.apiClient.toPathValue(params['locationId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'locationId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceListResult')
        return responseObject




    def getNetworkDeviceByLocationByRange(self, **kwargs):
        """Retrieves network devices with location by range

        Args:

            locationId, str: Location ID (required)


            startIndex, int: Start index (required)


            recordsToReturn, int: Number of records to return (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceListResult
        """

        allParams = ['locationId', 'startIndex', 'recordsToReturn', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceByLocationByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/location/{locationId}/{startIndex}/{recordsToReturn}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('locationId' in params):
            replacement = str(self.apiClient.toPathValue(params['locationId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'locationId' + '}',
                                                replacement)

        if ('startIndex' in params):
            replacement = str(self.apiClient.toPathValue(params['startIndex']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'startIndex' + '}',
                                                replacement)

        if ('recordsToReturn' in params):
            replacement = str(self.apiClient.toPathValue(params['recordsToReturn']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'recordsToReturn' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceListResult')
        return responseObject




    def getNetworkDeviceLocationByRange(self, **kwargs):
        """Retrieves device location range

        Args:

            startIndex, int: startIndex (required)


            recordsToReturn, int: recordsToReturn (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceListResult
        """

        allParams = ['startIndex', 'recordsToReturn', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceLocationByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/location/{startIndex}/{recordsToReturn}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('startIndex' in params):
            replacement = str(self.apiClient.toPathValue(params['startIndex']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'startIndex' + '}',
                                                replacement)

        if ('recordsToReturn' in params):
            replacement = str(self.apiClient.toPathValue(params['recordsToReturn']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'recordsToReturn' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceListResult')
        return responseObject




    def getNetworkManagementInfo(self, **kwargs):
        """Get the network management information

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkManagementInfoResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkManagementInfo" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/management-info'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkManagementInfoResult')
        return responseObject




    def getNetworkManagementInfoCount(self, **kwargs):
        """Get the network management information count

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkManagementInfoCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/management-info/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject



    def getModuleByNetworkDeviceId(self, **kwargs):
        """Gives all the modules associated with given device id

        Args:

            deviceId, str: deviceId (required)


            limit, str: limit (required)


            offset, str: offset (required)


            nameList, list[str]: nameList (required)


            equipmentTypeList, list[str]: equipmentTypeList (required)


            serviceStateList, list[str]: serviceStateList (required)


            isPhysicallyPresentList, list[str]: isPhysicallyPresentList (required)


            vendorEquipmentTypeList, list[str]: vendorEquipmentTypeList (required)


            partNumberList, list[str]: partNumberList (required)


            operationalStateCodeList, list[str]: operationalStateCodeList (required)


            filterOperation, str: filterOperation (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ModuleListResult
        """

        allParams = ['deviceId', 'limit', 'offset', 'nameList', 'equipmentTypeList', 'serviceStateList', 'isPhysicallyPresentList', 'vendorEquipmentTypeList', 'partNumberList', 'operationalStateCodeList', 'filterOperation', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getModuleByNetworkDeviceId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/module'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('deviceId' in params):
            queryParams['deviceId'] = self.apiClient.toPathValue(params['deviceId'])

        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])

        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])

        if ('nameList' in params):
            queryParams['nameList'] = self.apiClient.toPathValue(params['nameList'])

        if ('equipmentTypeList' in params):
            queryParams['equipmentTypeList'] = self.apiClient.toPathValue(params['equipmentTypeList'])

        if ('serviceStateList' in params):
            queryParams['serviceStateList'] = self.apiClient.toPathValue(params['serviceStateList'])

        if ('isPhysicallyPresentList' in params):
            queryParams['isPhysicallyPresentList'] = self.apiClient.toPathValue(params['isPhysicallyPresentList'])

        if ('vendorEquipmentTypeList' in params):
            queryParams['vendorEquipmentTypeList'] = self.apiClient.toPathValue(params['vendorEquipmentTypeList'])

        if ('partNumberList' in params):
            queryParams['partNumberList'] = self.apiClient.toPathValue(params['partNumberList'])

        if ('operationalStateCodeList' in params):
            queryParams['operationalStateCodeList'] = self.apiClient.toPathValue(params['operationalStateCodeList'])

        if ('filterOperation' in params):
            queryParams['filterOperation'] = self.apiClient.toPathValue(params['filterOperation'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ModuleListResult')
        return responseObject




    def getModuleCount(self, **kwargs):
        """Gives total number of Modules

        Args:

            deviceId, str: deviceId (required)


            nameList, list[str]: nameList (required)


            equipmentTypeList, list[str]: equipmentTypeList (required)


            serviceStateList, list[str]: serviceStateList (required)


            isPhysicallyPresentList, list[str]: isPhysicallyPresentList (required)


            vendorEquipmentTypeList, list[str]: vendorEquipmentTypeList (required)


            partNumberList, list[str]: partNumberList (required)


            operationalStateCodeList, list[str]: operationalStateCodeList (required)


            filterOperation, str: filterOperation (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['deviceId', 'nameList', 'equipmentTypeList', 'serviceStateList', 'isPhysicallyPresentList', 'vendorEquipmentTypeList', 'partNumberList', 'operationalStateCodeList', 'filterOperation', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getModuleCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/module/count'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'


        if ('deviceId' in params):
            queryParams['deviceId'] = self.apiClient.toPathValue(params['deviceId'])

        if ('nameList' in params):
            queryParams['nameList'] = self.apiClient.toPathValue(params['nameList'])

        if ('equipmentTypeList' in params):
            queryParams['equipmentTypeList'] = self.apiClient.toPathValue(params['equipmentTypeList'])

        if ('serviceStateList' in params):
            queryParams['serviceStateList'] = self.apiClient.toPathValue(params['serviceStateList'])

        if ('isPhysicallyPresentList' in params):
            queryParams['isPhysicallyPresentList'] = self.apiClient.toPathValue(params['isPhysicallyPresentList'])

        if ('vendorEquipmentTypeList' in params):
            queryParams['vendorEquipmentTypeList'] = self.apiClient.toPathValue(params['vendorEquipmentTypeList'])

        if ('partNumberList' in params):
            queryParams['partNumberList'] = self.apiClient.toPathValue(params['partNumberList'])

        if ('operationalStateCodeList' in params):
            queryParams['operationalStateCodeList'] = self.apiClient.toPathValue(params['operationalStateCodeList'])

        if ('filterOperation' in params):
            queryParams['filterOperation'] = self.apiClient.toPathValue(params['filterOperation'])



        if ('scope' in params):
            headerParams['scope'] = params['scope']








        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CountResult')
        return responseObject




    def getModuleById(self, **kwargs):
        """Gives Module info by its id

        Args:

            id, str: id (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: ModuleResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getModuleById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/module/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ModuleResult')
        return responseObject




    def getNetworkDeviceBySerialNumber(self, **kwargs):
        """Retrieves network device by serial number

        Args:

            serialNumber, str: Device serial number (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceResult
        """

        allParams = ['serialNumber', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceBySerialNumber" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/serial-number/{serialNumber}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('serialNumber' in params):
            replacement = str(self.apiClient.toPathValue(params['serialNumber']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'serialNumber' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceResult')
        return responseObject




    def getNetworkDeviceById(self, **kwargs):
        """Retrieves network device by ID

        Args:

            id, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceResult')
        return responseObject




    def deleteDevicebyId(self, **kwargs):
        """Delete network device by ID

        Args:

            id, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteDevicebyId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getNetworkDeviceBrief(self, **kwargs):
        """Retrieves network device brief by ID

        Args:

            id, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceBriefNIOResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceBrief" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{id}/brief'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceBriefNIOResult')
        return responseObject




    def getNetworkDeviceLocationById(self, **kwargs):
        """Retrieves device location by device ID

        Args:

            id, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceLocationById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{id}/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceResult')
        return responseObject




    def deleteNetworkLocationById(self, **kwargs):
        """Removes network device location

        Args:

            id, str: Device ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteNetworkLocationById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{id}/location'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject



    #changed this from getRunningConfig to getRunningConfigById manually
    def getRunningConfigById(self, **kwargs):
        """Retrieves device config by device id

        Args:

            networkDeviceId, str: networkDeviceId (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: SuccessResult
        """

        allParams = ['networkDeviceId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getRunningConfig" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{networkDeviceId}/config'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('networkDeviceId' in params):
            replacement = str(self.apiClient.toPathValue(params['networkDeviceId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'networkDeviceId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SuccessResult')
        return responseObject




    def getNetworkDeviceRange(self, **kwargs):
        """Retrieves network device by range

        Args:

            startIndex, int: Start index (required)


            recordsToReturn, int: Number of records to return (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: NetworkDeviceListResult
        """

        allParams = ['startIndex', 'recordsToReturn', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getNetworkDeviceRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/network-device/{startIndex}/{recordsToReturn}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'




        if ('scope' in params):
            headerParams['scope'] = params['scope']



        if ('startIndex' in params):
            replacement = str(self.apiClient.toPathValue(params['startIndex']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'startIndex' + '}',
                                                replacement)

        if ('recordsToReturn' in params):
            replacement = str(self.apiClient.toPathValue(params['recordsToReturn']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'recordsToReturn' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'NetworkDeviceListResult')
        return responseObject






