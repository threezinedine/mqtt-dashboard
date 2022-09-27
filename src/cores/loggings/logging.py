from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def info(self, msg:str) -> None:
        pass

    @abstractmethod
    def error(self, msg:str) -> None:
        pass

    @abstractmethod
    def debug(self, msg:str) -> None:
        pass

    @abstractmethod
    def warn(self, msg:str) -> None:
        pass
