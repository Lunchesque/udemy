import pytest

def test_add_location(app):
    old_locs = app.get_locations()
    app.add_location()
    new_locs = app.get_locations()
    assert len(old_locs) + 1 == len(new_locs)
