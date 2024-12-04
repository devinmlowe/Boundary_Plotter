"""
tests for the angles.py module
"""
from pytest import approx
from angles import parse_bearing
from angles import decimal_degree_to_azimuth
from angles import decimal_degree_to_quad_bearing

def test_parse_bearing_with_quad():
    """Tests output with Quadrant Supplied"""
    input_bearing =r'''N32°10'32"E'''
    result = parse_bearing(bearing=input_bearing)
    assert result == approx(32.175556)

def test_parse_bearing_without_quad():
    """Tests output without Quadrant Supplied"""
    input_bearing =r'''32°10'32"'''
    result = parse_bearing(bearing=input_bearing)
    assert result == approx(32.175556)

def test_parse_bearing_southeast():
    """Tests for adjustment of degree value based on SouthEast Quadrant"""
    input_bearing =r'''S70°E'''
    result = parse_bearing(bearing=input_bearing)
    assert result == approx(110.000000)

def test_parse_bearing_southwest():
    """Tests for adjustment of degree value based on Southwest Quadrant"""
    input_bearing =r'''S45°32'W'''
    result = parse_bearing(bearing=input_bearing)
    assert result == approx(225.533333)

def test_parse_bearing_northwest():
    """Tests for adjustment of degree value based on Northwest Quadrant"""
    input_bearing =r'''N60°45'10"W'''
    result = parse_bearing(bearing=input_bearing)
    assert result == approx(299.247222)

def test_parse_bearing_asterisk():
    """Tests for successful substitution of * with °"""
    input_bearing =r'''N60*45'10"W'''
    result = parse_bearing(bearing=input_bearing)
    assert result == approx(299.247222)

def test_decimal_degree_to_azi():
    """Tests that a decimal degree can successfully convert to a bearing call without quads"""
    input_degree = 32.175556
    result = decimal_degree_to_azimuth(input_degree)
    assert result == r'''32°10'32"'''

def test_decimal_degree_to_quad_northeast():
    """Tests that the rotation for the Northeast Quadrant works"""
    input_bearing =  "N32°10'32\"E"
    input_degree = parse_bearing(input_bearing)
    result = decimal_degree_to_quad_bearing(input_degree)
    assert result == input_bearing

def test_decimal_degree_to_quad_southeast():
    """Tests that the rotation for the Southeast Quadrant works"""    
    input_bearing = r'''S70°00'00"E'''
    input_degree = parse_bearing(input_bearing)
    result = decimal_degree_to_quad_bearing(input_degree)
    assert result == input_bearing

def test_decimal_degree_to_quad_southwest():
    """Tests that the rotation for the Southwest Quadrant works"""    
    input_bearing = r'''S45°32'00"W'''
    input_degree = parse_bearing(input_bearing)
    result = decimal_degree_to_quad_bearing(input_degree)
    assert result == input_bearing

def test_decimal_degree_to_quad_northwest():
    """Tests that the rotation for the Northwest Quadrant works"""    
    input_bearing = r'''N60°45'10"W'''
    input_degree = parse_bearing(input_bearing)
    result = decimal_degree_to_quad_bearing(input_degree)
    assert result == input_bearing
    