import pytest
from boundaries import convertBearingToDecimalDegree

def test_invalid_bearing():
    bearing = "NXX°YY'ZZ\"E"
    with pytest.raises(ValueError):
        convertBearingToDecimalDegree(None, bearing)

from boundaries import parseBearing

def test_parseBearing_1():
    bearing = "N45°30'25\"E"
    result = parseBearing(bearing)
    assert result== ["NE",45,30,25]
def test_parseBearing_asterisk():
    bearing = "N45*30'25\"E"
    result = parseBearing(bearing)
    assert result== ["NE",45,30,25]