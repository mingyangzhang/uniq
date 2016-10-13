#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class TestCaseResponse(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {

            'testExecutionTimeInMillis': 'int',


            'testCaseError': 'str',


            'testCaseExecutionResult': 'str',


            'testCaseId': 'str'

        }

        self.attributeMap = {

            'testExecutionTimeInMillis': 'testExecutionTimeInMillis',

            'testCaseError': 'testCaseError',

            'testCaseExecutionResult': 'testCaseExecutionResult',

            'testCaseId': 'testCaseId'

        }


        #the test case exeuction time in milliseconds

        self.testExecutionTimeInMillis = None # int

        #the error details in case test failure

        self.testCaseError = None # str

        #the test case result. success or failure

        self.testCaseExecutionResult = None # str

        #the test case identifier

        self.testCaseId = None # str

