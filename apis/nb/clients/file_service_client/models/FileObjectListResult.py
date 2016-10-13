#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class FileObjectListResult(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'response': 'list[FileObject]',
            
            
            'version': 'str'
            
        }

        self.attributeMap = {
            
            'response': 'response',
            
            'version': 'version'
            
        }       

        
        
        self.response = None # list[FileObject]
        
        
        self.version = None # str
        
