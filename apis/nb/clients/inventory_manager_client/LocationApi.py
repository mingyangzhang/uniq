#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class LocationApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def getAllLocation(self, **kwargs):
        """Retrieves all locations

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: LocationNIOListResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location'
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

        responseObject = self.apiClient.deserialize(response, 'LocationNIOListResult')
        return responseObject




    def updateLocation(self, **kwargs):
        """Updates location

        Args:

            locationNIO, LocationNIO: Attributes of a location (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['locationNIO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location'
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







        if ('locationNIO' in params):
            bodyParam = params['locationNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def addLocation(self, **kwargs):
        """Creates location

        Args:

            locationNIO, LocationNIO: Attributes of a location (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['locationNIO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method addLocation" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location'
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







        if ('locationNIO' in params):
            bodyParam = params['locationNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getLocationCount(self, **kwargs):
        """Retrieves location count

        Args:

            scope, str: Authorization Scope for RBAC (required)



        Returns: CountResult
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationCount" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/count'
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




    def getLocationByName(self, **kwargs):
        """Retrieves location by location name

        Args:

            locationName, str: Location name (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: LocationNIOResult
        """

        allParams = ['locationName', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationByName" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/location-name/{locationName}'
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



        if ('locationName' in params):
            replacement = str(self.apiClient.toPathValue(params['locationName']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'locationName' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'LocationNIOResult')
        return responseObject




    def updateLocationTag(self, **kwargs):
        """Associate a tag to a location

        Args:

            tagNIO, TagNIO: TagNIO with tag ID and location ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['tagNIO', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method updateLocationTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/tag'
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







        if ('tagNIO' in params):
            bodyParam = params['tagNIO']


        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TaskIdResult')
        return responseObject




    def getLocationById(self, **kwargs):
        """Retrieves location by ID

        Args:

            id, str: Location ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: LocationNIOResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'LocationNIOResult')
        return responseObject




    def deleteLocationById(self, **kwargs):
        """Deletes location by ID

        Args:

            id, str: Location ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: TaskIdResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteLocationById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{id}'
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




    def getLocationByRange(self, **kwargs):
        """Retrieves location range

        Args:

            startIndex, int: Start index (required)


            recordsToReturn, int: Number of records to return (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: LocationNIOListResult
        """

        allParams = ['startIndex', 'recordsToReturn', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationByRange" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{startIndex}/{recordsToReturn}'
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

        responseObject = self.apiClient.deserialize(response, 'LocationNIOListResult')
        return responseObject




    def getLocationByTag(self, **kwargs):
        """Retrieves location by tag

        Args:

            tagId, str: Tag ID (required)


            scope, str: Authorization Scope for RBAC (required)



        Returns: LocationNIOListResult
        """

        allParams = ['tagId', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getLocationByTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/tag/{tagId}/location'
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



        if ('tagId' in params):
            replacement = str(self.apiClient.toPathValue(params['tagId']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'tagId' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'LocationNIOListResult')
        return responseObject
            
        
        
    
    def deleteLocationTag(self, **kwargs):
        """Deletes location tag by location ID

        Args:
            
            id, str: Location ID (required)
            
            
            scope, str: Authorization Scope for RBAC (required)
            
            
        
        Returns: TaskIdResult
        """

        allParams = ['id', 'scope']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method deleteLocationTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/location/{id}/tag'
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






