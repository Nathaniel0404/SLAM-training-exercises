from slam.models import Pose2D, Landmark, OdomMsg, PerceptionMsg
import math


# Estimates the new position of the vehicle given a new odom msg
def estimate_new_pose(old_pose: Pose2D, odom_msg: OdomMsg) -> Pose2D:
    # TODO: Implement me!
    pass


# Estimates the position of a landmark the vehicle has detected
def estimate_landmark_pos(curr_pose: Pose2D, perception_msg: PerceptionMsg) -> Landmark:
    # TODO: Implement me!
    pass

# ADDITIONAL TASK: Create a helper function to normalise your angle, and create a test file to check if it is correct
