"""
Types for OpenCV.
"""

from numpy import ndarray
import typing


def cvtColor(image: ndarray, code: typing.Any) -> ndarray:
    ...


def GaussianBlur(image: ndarray, ksize: typing.Tuple[int, int],
                 sigmaX: float) -> ndarray:
    ...


def Canny(image: ndarray, threshold1: float, threshold2: float,
          L2gradient: bool, edges: int) -> ndarray:
    ...


def findContours(image: ndarray, mode: typing.Any,
                 method: typing.Any) -> typing.Any:
    ...


def imread(path: str) -> ndarray:
    ...


def threshold(image: ndarray, thresh: int, maxval: int,
              type: typing.Any) -> ndarray:
    ...


def dilate(image: ndarray, kernel: ndarray, iterations: int) -> ndarray:
    ...


THRESH_BINARY: int
THRESH_OTSU: int
CHAIN_APPROX_SIMPLE: int
RETR_TREE: int
COLOR_BGR2GRAY: int