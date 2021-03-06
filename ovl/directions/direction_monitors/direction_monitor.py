from typing import Union


class DirectionMonitor:
    @property
    def priority(self) -> Union[bool, float]:
        return False

    def monitor(self, directions, targets, image, mask):
        raise NotImplementedError("When inheriting DirectionMonitor you must implement it!")
