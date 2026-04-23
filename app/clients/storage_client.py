from abc import ABC, abstractmethod


class StorageClient(ABC):

    @abstractmethod
    def save(self, data: str) -> str:
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        pass
