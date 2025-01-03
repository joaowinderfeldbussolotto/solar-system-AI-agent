
from abc import ABC, abstractmethod
from typing import Dict, Any, Callable

class Action(ABC):
    @abstractmethod
    def execute(self, params: str) -> str:
        pass

class CalculateAction(Action):
    def execute(self, expression: str) -> str:
        result = eval(expression)
        return str(result)
    
class FinalAnswer(Action):
    def execute(self, answer: str) -> str:
        return answer
    
class PlanetMassAction(Action):
    def __init__(self):
        self.masses = {
            "Mercury": 0.33011,
            "Venus": 4.8675,
            "Earth": 5.972,
            "Mars": 0.64171,
            "Jupiter": 1898.19,
            "Saturn": 568.34,
            "Uranus": 86.813,
            "Neptune": 102.413,
        }
    
    def execute(self, planet: str) -> str:
        return f"{planet} possui uma massa de {self.masses[planet]} × 10^24 kg."

class ActionRegistry:
    _actions: Dict[str, Action] = {}
    
    @classmethod
    def register(cls, name: str, action: Action) -> None:
        cls._actions[name] = action
    
    @classmethod
    def get_action(cls, name: str) -> Action:
        if name not in cls._actions:
            raise ValueError(f"Action {name} not found")
        return cls._actions[name]
    
    @classmethod
    def execute_action(cls, name: str, params: str) -> str:
        action = cls.get_action(name)
        result = action.execute(params)
        return result

# Register default actions
ActionRegistry.register("calculate", CalculateAction())
ActionRegistry.register("planet_mass", PlanetMassAction())
ActionRegistry.register("final_answer", FinalAnswer())