"""
Tools to Parse Bearing and Distance Calls into Vectors, Coordinates, and Lines.
"""

from .angles import decimal_degree_to_azimuth, parse_bearing, decimal_degree_to_quad_bearing, Angle
__all__ = ['angle','decimal_degree_to_azimuth','parse_bearing','decimal_degree_to_quad_bearing']
