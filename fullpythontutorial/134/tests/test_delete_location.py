import pytest

def test_delete_location(app):
    old_locs = app.get_locations()
    app.delete_location()
    new_locs = app.get_locations()
    assert len(old_locs) - 1 == len(new_locs)
