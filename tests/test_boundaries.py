"""
tests for the boundaries.py module
"""

from boundaries import parse_bearing

def test_parse_bearing_with_quad():
    """Tests output with Quadrant Supplied"""
    input_bearing ="N32°10'32\"E"
    result = parse_bearing(bearing=input_bearing)
    assert result == 32.175556

def test_parse_bearing_without_quad():
    """Tests output without Quadrant Supplied"""
    input_bearing ="32°10'32\""
    result = parse_bearing(bearing=input_bearing)
    assert result == 32.175556

def test_parse_bearing_southeast():
    """Tests for adjustment of degree value based on SouthEast Quadrant"""
    input_bearing ="S70°E"
    result = parse_bearing(bearing=input_bearing)
    assert result == 110.000000

def test_parse_bearing_southwest():
    """Tests for adjustment of degree value based on Southwest Quadrant"""
    input_bearing ="S45°32'W"
    result = parse_bearing(bearing=input_bearing)
    assert result == 225.533333

def test_parse_bearing_northwest():
    """Tests for adjustment of degree value based on Northwest Quadrant"""
    input_bearing ="N60°45'10\"W"
    result = parse_bearing(bearing=input_bearing)
    assert result == 299.247222

def test_parse_bearing_asterisk():
    """Tests for successful substitution of * with °"""
    input_bearing ="N60*45'10\"W"
    result = parse_bearing(bearing=input_bearing)
    assert result == 299.247222
    