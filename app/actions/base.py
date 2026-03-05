from abc import ABC, abstractmethod


class BaseAction(ABC):

    @abstractmethod
    def execute(self, workflow_id: int):
        pass
