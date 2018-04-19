import pytest
from test.locations import Locations as locs


# def test_add_location():
#     old_locs = locs.get_locations()
#     locs.add_location()
#     new_locs = locs.get_locations()
#     assert len(old_locs) + 1 == len(new_locs)

def test_delete_location():
    old_locs = locs.get_locations()
    locs.delete_location()
    new_locs = locs.get_locations()
    assert len(old_locs) - 1 == len(new_locs)
