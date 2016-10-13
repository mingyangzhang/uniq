#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ScheduleInfoOutput(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'startTime': 'date-time',
            
            
            'endTime': 'date-time',
            
            
            'description': 'str',
            
            
            'origin': 'str',
            
            
            'taskId': 'str',
            
            
            'operation': 'str',
            
            
            'groupName': 'str',
            
            
            'prevTime': 'date-time',
            
            
            'nextTime': 'date-time',
            
            
            'scheduledWorkSpecId': 'str'
            
        }

        self.attributeMap = {
            
            'startTime': 'startTime',
            
            'endTime': 'endTime',
            
            'description': 'description',
            
            'origin': 'origin',
            
            'taskId': 'taskId',
            
            'operation': 'operation',
            
            'groupName': 'groupName',
            
            'prevTime': 'prevTime',
            
            'nextTime': 'nextTime',
            
            'scheduledWorkSpecId': 'scheduledWorkSpecId'
            
        }       

        
        #The time at which the trigger should first fire. If the schedule has fired and will not fire again, this value will be null
        
        self.startTime = None # date-time
        
        #The time at which the trigger should quit repeating
        
        self.endTime = None # date-time
        
        #Simple description to be shown to end-users
        
        self.description = None # str
        
        #Contextual field used to identify work spcifications originating from the same source
        
        self.origin = None # str
        
        #UUID of the Task
        
        self.taskId = None # str
        
        #Contextual field used by the service to identify an operation
        
        self.operation = None # str
        
        #A grouping name that can be specified by the service to allow for filtered work spec retrieval
        
        self.groupName = None # str
        
        #The previous time at which the trigger fired. If the trigger has not yet fired, null will be returned
        
        self.prevTime = None # date-time
        
        #The next time at which the trigger should fire
        
        self.nextTime = None # date-time
        
        #UUID of the ScheduledWorkSpec associated with the scheduled task
        
        self.scheduledWorkSpecId = None # str
        
