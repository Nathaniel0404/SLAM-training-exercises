
import pytest
from dataclasses import is_dataclass, fields

from slam.models import (
    Pose2D,
    Landmark,
    OdomMsg,
    PerceptionMsg,
)


@pytest.mark.parametrize(
    "model, expected_fields",
    [
        (Pose2D, ["x", "y", "theta"]),
        (Landmark, ["x", "y"]),
        (OdomMsg, ["dx", "dy", "dtheta"]),
        (PerceptionMsg, ["dx", "dy"]),
    ],
)
def test_dataclass_fields(model, expected_fields):
    assert is_dataclass(model)
    actual_fields = [field.name for field in fields(model)]
    assert actual_fields == expected_fields


def test_pose_creation():
    pose = Pose2D(x=1.0, y=2.0, theta=0.5)

    assert pose.x == pytest.approx(1.0)
    assert pose.y == pytest.approx(2.0)
    assert pose.theta == pytest.approx(0.5)


def test_landmark_creation():
    landmark = Landmark(x=5.0, y=3.0)

    assert landmark.x == pytest.approx(5.0)
    assert landmark.y == pytest.approx(3.0)


def test_odom_creation():
    odom = OdomMsg(dx=1.0, dy=0.5, dtheta=0.1)

    assert odom.dx == pytest.approx(1.0)
    assert odom.dy == pytest.approx(0.5)
    assert odom.dtheta == pytest.approx(0.1)


def test_perception_creation():
    perception = PerceptionMsg(dx=2.0, dy=1.5)

    assert perception.dx == pytest.approx(2.0)
    assert perception.dy == pytest.approx(1.5)

