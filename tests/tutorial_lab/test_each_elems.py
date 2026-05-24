from coala import Lab
import pytest


@pytest.fixture(scope="module")
def lab_name() -> str:
    return "tutorial_lab"


def test_lab_load(lab: Lab):
    """assert lab fixture is loaded without any error"""
    assert isinstance(lab, Lab)
    assert lab.lab_name == "tutorial_lab"


def test_lab_integrity(lab: Lab):
    """Verifies that all recipes in the lab are structurally sound and fusable."""
    lab.assert_is_fusable()


def test_fuse_fire_and_water(lab: Lab):
    result = lab.fuse("fire", "water")
    assert result == "steam"

def test_fuse_fire_and_wind(lab: Lab):
    result = lab.fuse("fire", "wind")
    assert result == "spark"

def test_fuse_fire_and_earth(lab: Lab):
    result = lab.fuse("fire", "earth")
    assert result == "magma"


# @pytest.mark.asyncio
# async def test_fusing_fire_earth(tutorial_lab: Lab):
#     assert await tutorial_lab.fuse("fire", "earth") == "lava"