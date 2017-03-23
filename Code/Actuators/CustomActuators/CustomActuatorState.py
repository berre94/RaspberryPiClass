from abc import ABCMeta
from Actuators.ActuatorState import ActuatorState


class CustomActuatorState(ActuatorState):
    __metaclass__ = ABCMeta

    def __init__(self, base_actuator, duration=-1, returning_state=None):
        super(CustomActuatorState, self).__init__(base_actuator, duration, returning_state)