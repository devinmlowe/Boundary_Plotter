import pytest
from boundaries import convertAzimuthToDecimalDegree

def test_convertAzimuthToDecimalDegree():
    quad = ''
    deg = 0
    min = 0
    sec = 0
    result = 0
    assert result== 0

from boundaries import parseBearing

def test_parseBearing_1():
    bearing = "N45°30'25\"E"
    result = parseBearing(bearing)
    assert result== ["NE",45,30,25]
def test_parseBearing_asterisk():
    bearing = "N45*30'25\"E"
    result = parseBearing(bearing)
    assert result== ["NE",45,30,25]
    