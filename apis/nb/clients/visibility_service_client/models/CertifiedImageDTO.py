#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class CertifiedImageDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'imageId': 'str',
            
            
            'platform': 'str'
            
        }

        self.attributeMap = {
            
            'imageId': 'imageId',
            
            'platform': 'platform'
            
        }       

        
        
        self.imageId = None # str
        
        
        self.platform = None # str
        
