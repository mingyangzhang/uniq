#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ServiceProviderProfileDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'name': 'str',
            
            
            'interfaces': 'list[ServiceProviderProfileInterfaceDTO]',
            
            
            'defaultModel': 'bool',
            
            
            'modelType': 'str',
            
            
            'vendor': 'str',
            
            
            'currentVersion': 'int',
            
            
            'classModels': 'list[ClassModelDTO]',
            
            
            'id': 'str',
            
            
            'lastUpdateTime': 'int',
            
            
            'createTime': 'int'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'name': 'name',
            
            'interfaces': 'interfaces',
            
            'defaultModel': 'defaultModel',
            
            'modelType': 'modelType',
            
            'vendor': 'vendor',
            
            'currentVersion': 'currentVersion',
            
            'classModels': 'classModels',
            
            'id': 'id',
            
            'lastUpdateTime': 'lastUpdateTime',
            
            'createTime': 'createTime'
            
        }       

        
        
        self.description = None # str
        
        #unique name for the ServiceProviderProfile
        
        self.name = None # str
        
        
        self.interfaces = None # list[ServiceProviderProfileInterfaceDTO]
        
        #Read only attribute to indicate whether the ServiceProviderProfile is default(&#39;true&#39;) or custom(&#39;false&#39;)
        
        self.defaultModel = None # bool
        
        #Available options are: Three-Class, Four-Class, Five-Class, Six-Class, Eight-Class
        
        self.modelType = None # str
        
        
        self.vendor = None # str
        
        
        self.currentVersion = None # int
        
        #classModels list size should match the modelType
        
        self.classModels = None # list[ClassModelDTO]
        
        #id
        
        self.id = None # str
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
        #createTime
        
        self.createTime = None # int
        
