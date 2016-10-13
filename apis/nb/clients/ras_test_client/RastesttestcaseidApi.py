#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class RastesttestcaseidApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient



    def executeTestCase(self, **kwargs):
        """Returns testcase result

        Args:

            test-case-id, str: The test case identifier (required)



        Returns: TestCaseResult
        """

        allParams = ['test-case-id']

        params = locals()
        for (key, val) in list(params['kwargs'].items()):
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method executeTestCase" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/ras-test/{test-case-id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'






        if ('test-case-id' in params):
            replacement = str(self.apiClient.toPathValue(params['test-case-id']))
            replacement = urllib.parse.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'test-case-id' + '}',
                                                replacement)






        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)


        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TestCaseResult')
        return responseObject






