
import math
import pytest

from slam.models import Pose2D, Landmark, OdomMsg, PerceptionMsg
from slam.estimation import estimate_new_pose, estimate_landmark_pos


# ==========================================
# Exercise 1: Vehicle Pose Estimation
# ==========================================

@pytest.mark.parametrize(
    "old_pose, odom, expected",
    [
        # No movement
        (
            Pose2D(0, 0, 0),
            OdomMsg(0, 0, 0),
            Pose2D(0, 0, 0),
        ),

        # Forward movement, no rotation
        (
            Pose2D(0, 0, 0),
            OdomMsg(2, 0, 0),
            Pose2D(2, 0, 0),
        ),

        # Forward movement with initial 90-degree heading
        (
            Pose2D(0, 0, math.pi / 2),
            OdomMsg(2, 0, 0),
            Pose2D(0, 2, math.pi / 2),
        ),

        # Lateral movement in local frame
        (
            Pose2D(0, 0, math.pi / 2),
            OdomMsg(0, 2, 0),
            Pose2D(-2, 0, math.pi / 2),
        ),

        # Translation and rotation
        (
            Pose2D(1, 2, 0),
            OdomMsg(3, 4, math.pi / 2),
            Pose2D(4, 6, math.pi / 2),
        ),

        # Negative rotation
        (
            Pose2D(0, 0, 0),
            OdomMsg(0, 0, -math.pi / 2),
            Pose2D(0, 0, -math.pi / 2),
        ),

        # Angle wrapping across positive pi
        (
            Pose2D(0, 0, 3 * math.pi / 4),
            OdomMsg(0, 0, math.pi / 2),
            Pose2D(0, 0, -3 * math.pi / 4),
        ),

        # Angle wrapping across negative pi
        (
            Pose2D(0, 0, -3 * math.pi / 4),
            OdomMsg(0, 0, -math.pi / 2),
            Pose2D(0, 0, 3 * math.pi / 4),
        ),
    ],
)
def test_estimate_new_pose(old_pose, odom, expected):
    result = estimate_new_pose(old_pose, odom)

    assert isinstance(result, Pose2D)
    assert result.x == pytest.approx(expected.x)
    assert result.y == pytest.approx(expected.y)
    assert result.theta == pytest.approx(expected.theta)


# ==========================================
# Exercise 2: Landmark Position Estimation
# ==========================================

@pytest.mark.parametrize(
    "pose, perception, expected",
    [
        # Landmark directly ahead at zero heading
        (
            Pose2D(0, 0, 0),
            PerceptionMsg(5, 0),
            Landmark(5, 0),
        ),

        # Landmark with non-zero vehicle position
        (
            Pose2D(2, 3, 0),
            PerceptionMsg(4, 1),
            Landmark(6, 4),
        ),

        # Landmark ahead with 90-degree vehicle heading
        (
            Pose2D(0, 0, math.pi / 2),
            PerceptionMsg(5, 0),
            Landmark(0, 5),
        ),

        # Landmark to the left with 90-degree heading
        (
            Pose2D(0, 0, math.pi / 2),
            PerceptionMsg(0, 3),
            Landmark(-3, 0),
        ),

        # Landmark with 180-degree vehicle heading
        (
            Pose2D(1, 2, math.pi),
            PerceptionMsg(3, 2),
            Landmark(-2, 0),
        ),

        # Landmark with negative heading
        (
            Pose2D(0, 0, -math.pi / 2),
            PerceptionMsg(4, 0),
            Landmark(0, -4),
        ),

        # Landmark at vehicle position
        (
            Pose2D(3, 4, math.pi / 4),
            PerceptionMsg(0, 0),
            Landmark(3, 4),
        ),

        # Non-axis-aligned rotation
        (
            Pose2D(1, 2, math.pi / 4),
            PerceptionMsg(math.sqrt(2), 0),
            Landmark(2, 3),
        ),
    ],
)
def test_estimate_landmark_pos(pose, perception, expected):
    result = estimate_landmark_pos(pose, perception)

    assert isinstance(result, Landmark)
    assert result.x == pytest.approx(expected.x)
    assert result.y == pytest.approx(expected.y)
