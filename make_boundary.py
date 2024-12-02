"""
Tools to Parse Bearing and Distance Calls into Vectors, Coordinates, and Lines
"""

from dataclasses import dataclass
from shapely import *

@dataclass
class boundary:
    """
    Class that represents a closed boundary object.
    """

@dataclass
class line:
    """
    Class that represents a singular line given a bearing and distance.
    """

@dataclass
class bearing:
    """
    class that represents a Survey bearing in various angle formats.
    """
    
def convertBearingToDecimalDegree(self, bearing):
"""
Parse a bearing into an angle
"""
# Replace * for ° for parsing, this allows for the user to more easily type angles form the keyboard without needing to insert special symbols
bearing = bearing.replace("*","°")

# Parse direction components
direction_ns = 1 if bearing[0] == 'N' else -1
direction_ew = 0 if bearing[-1] == 'E' else -1

# Extract dgree, minute, and second values
angle_deg = int(bearing[1:bearing.find("°")])
angle_min = int(bearing[bearing.find("°") + 1:bearing.find("'")])
angle_sec  = int(bearing[bearing.find("'") + 1:bearing.find('"')])

# convert to decimal degrees
angle = angle_deg + (angle_min/60) + (angle_sec/3600)

# Adjust for cardinal direction
if direction_ns == 1: # North
    if direction_ew == 1: # East of North
        angle = 90 - angle
    else: # West of North
        angle = 90 + angle
else: # South
    if direction_ew == 1: # East of South
        angle = 270 + angle
    else: # West of South
        angle = 270 - angle

return angle




