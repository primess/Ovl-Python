from typing import Callable, List
import math

from .direction_monitors.direction_monitor import *
from ..camera.camera_settings import *


class Director:
    """
    Directors are object that extract usable information from the objects that were detected image.
    This information be where they are located in the image relative to the center (directions for a robot),
    how many objects were detected, identifying an object or any other logical usage of the object detection
    rather than raw image processing or computer vision.
    This is the final step before sending/using the data.

    Director.direct works in the following way:
    - if the amount of contours is less than target amount then set directions to failed_detection
    - else it passes only target_amount of contours to the direction function
    - The final result (direction function or failed_detection) is passed to the direction monitors
    - each monitor is applied to the result and its result is passed to the next one
    - then the final result is returned



    """

    def __init__(self, directing_function: Callable, failed_detection: Any = None, target_amount: int = 1,
                 direction_monitors: List[DirectionMonitor] = None):
        """
        :param directing_function: the function that performs the initial direction calculation
        :param failed_detection: The value returned on a failed detection
        :param target_amount: the target amount to find, if the value is 0
                              the target amount (minimum amount) removed and is infinite
        :param direction_monitors: list of DirectionMonitor objects that alter the directions to be sent
        """
        self.directions = directing_function
        if not isinstance(target_amount, int):
            raise ValueError("Target amount must be an integer, got {} of type {}.".format(target_amount,
                                                                                           type(target_amount)))
        self.target_amount = target_amount if target_amount != 0 else math.inf
        self.direction_monitors = direction_monitors
        self.failed_detection = failed_detection

    def direct(self, contours: List[np.ndarray], image: np.ndarray, camera_settings=None, sorter=None) -> Any:
        """
        Returns the directions using the vision.director for the given contours using the image and camera settings (if
        given).

        Director.direct works in the following way:
            - if the amount of contours is less than target amount then set directions to failed_detection
            - else it passes only target_amount of contours to the direction function
            - The final result (direction function or failed_detection) is passed to the direction monitors
            - each monitor is applied to the result and its result is passed to the next one
            - then the final result is returned

        :param contours: the list of contours (numpy ndarrays) from which to extrapolate target direction
        :param image: the image from which the contours were taken
        :param camera_settings: The Camera settings, including position and calibration
        :param sorter: A sorter function to be applied on the contours, or None to not apply one
        :return: Depends on the directing function and the direction monitors,
                 usually a number or a string
        """
        if not len(contours) >= self.target_amount:
            directions = self.failed_detection
        else:
            if sorter is not None:
                contours = sorter(contours)
            if math.isfinite(self.target_amount):
                contours = contours[:self.target_amount]
            directions = self.directions(contours, image)

        return self.apply_direction_monitors(directions, contours, image, camera_settings)

    def apply_direction_monitors(self, directions: Any, contours: List[np.ndarray],
                                 image: np.ndarray, camera_settings: CameraSettings) -> Any:
        """
        Applies the list of direction monitors one after the other

        Direction monitors are functions that receive directions contours image and camera settings
        and change it some way, like applying a PID feedback loop, returning a "stop" value based on some condition
        (like getting close enough to the target)

        :param directions: the raw directions returned from the directions function
        :param contours: the list of contours that passed all filters
        :param image: the image from which the contours were found
        :param camera_settings: settings related to the camera, like position or calibration
        :return: the final direction result
        """
        if self.direction_monitors:
            for direction_monitor in self.direction_monitors:
                directions = direction_monitor.monitor(directions, contours, image, camera_settings)
                if direction_monitor.priority:
                    return directions
        return directions
