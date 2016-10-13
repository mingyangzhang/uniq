#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.



import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class InventoryApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient


    def updateDevice(self, **kwargs):
        """Update a device that is in the inventory

        Args:

            discoveredDevice, DiscoveredDevice: discoveredDevice (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['discoveredDevice', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory'
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







        if ('discoveredDevice' in params):
            bodyParam = params['discoveredDevice']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addDevice(self, **kwargs):
        """Adds a discovered device to the inventory

        Args:

            discoveredDevice, DiscoveredDevice: discoveredDevice (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['discoveredDevice', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory'
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







        if ('discoveredDevice' in params):
            bodyParam = params['discoveredDevice']


        postData = (formParams if formParams else bodyParam)


        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def updateDevice(self, **kwargs):
        """Updates devices that is in the inventory

        Args:

            discoveredDevices, list[DiscoveredDevice]: discoveredDevices (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['discoveredDevices', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory/bulk'
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







        if ('discoveredDevices' in params):
            bodyParam = params['discoveredDevices']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject



    #This endpoint is updated to 'addDevices' from 'addDevice' manually.
    def addDevices(self, **kwargs):
        """adds devices to the inventory

        Args:

            discoveredDevices, list[DiscoveredDevice]: discoveredDevices (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['discoveredDevices', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory/bulk'
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







        if ('discoveredDevices' in params):
            bodyParam = params['discoveredDevices']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject



    #This endpoint is updated to 'deleteDevices' from 'deleteDevice' manually.
    def deleteDevices(self, **kwargs):
        """Deletes a device from the inventory

        Args:

            ipAddresses, List: ipAddresses (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['ipAddresses', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory/bulk'
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







        if ('ipAddresses' in params):
            bodyParam = params['ipAddresses']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject


    def updateIpAddress(self, **kwargs):
        """Method to update ip-address

        Args:

            device, NetworkDeviceMgmtIPAddress: device (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['device', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateIpAddress" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory/updateIpAddress'
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







        if ('device' in params):
            bodyParam = params['device']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def deleteDevice(self, **kwargs):
        """Deletes a device from the inventory

        Args:

            ipAddress, str: ipAddress (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['ipAddress', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteDevice" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/inventory/{ipAddress}'
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

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject