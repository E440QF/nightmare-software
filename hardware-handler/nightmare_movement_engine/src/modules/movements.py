import numpy as np
from numpy import sin
import time
from modules.robot_math import abs_pos2ang
from modules.config import DEFAULT_POSE


def sleep(engine):
    engine.angles_array = abs_pos2ang(engine.pose)
