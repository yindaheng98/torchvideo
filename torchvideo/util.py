import abc
import numpy as np


class VideoDataset(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def valid(self) -> bool:
        pass

    @abc.abstractmethod
    def read_images(self, paths: [str]) -> [np.ndarray]:
        pass

    @abc.abstractmethod
    def list_images(self) -> [str]:
        pass

    @abc.abstractmethod
    def list_videos(self) -> [[str]]:
        pass
