"""Tools to Parse Bearing and Distance Calls into Vectors, Coordinates, and Lines."""
import re
from math import radians,degrees,floor


class Angle:
    """
    A representation of an angle  
   # Attributes:  
   1. `azimuth_bearing (str)` - `32°17'10"` - Degree/Minute/Seconds clockwise from True North
   2. `quad_bearing (str)` - `N32°17'10"E` - Degree/Minute/Seconds with Departure (N/S) and Latitude (E/W)
   3. `decimal_degree (float)` - `32.286111...` - Degrees as decimal clockwise from True North
   3. `radian (float)` - 
   
    """
    def __init__(self, azimuth_bearing: str = None,
                 quad_bearing: str = None,
                 decimal_degree: float = None,
                 radian: float = None):

        self.azimuth_bearing = azimuth_bearing
        self.quad_bearing = quad_bearing
        self.decimal_degree = decimal_degree
        self.radian = radian

    @property
    def azimuth_bearing(self):
        """returns bearing call as degrees, minutes, seconds clockwise from true north """
        return self.azimuth_bearing

    @azimuth_bearing.setter
    def azimuth_bearing(self, bearing_call:str = None):
        """Sets the Azimuth value then recalculates the other formats"""
        self.decimal_degree = parse_bearing(bearing_call)
        self.radian = radians(self.decimal_degree)
        self.azimuth_bearing = decimal_degree_to_azimuth(self.decimal_degree)
        self.quad_bearing = decimal_degree_to_quad_bearing(self.decimal_degree)

    @azimuth_bearing.deleter
    def azimuth_bearing(self):
        """if the azimuth bearing value is deleted, all other values are also deleted"""
        self.__del_all_attr()

    @property
    def quad_bearing(self):
        """
        Returns bearing call string as:  
            - Departure (North or South)  
            - Degrees  
            - Minutes  
            - Seconds  
            - Latitude (East or West)  
        ie: `N32°10'17"S`
        """
        return self.quad_bearing

    @quad_bearing.setter
    def set_quad_bearing(self,bearing_call: str):
        """Sets the Quadrant Bearing value then recalculates the other formats"""
        self.decimal_degree = parse_bearing(bearing_call)
        self.radian = radians(self.decimal_degree)
        self.azimuth_bearing = decimal_degree_to_azimuth(self.decimal_degree)
        self.quad_bearing = decimal_degree_to_quad_bearing(self.decimal_degree)

    @quad_bearing.deleter
    def quad_bearing(self):
        """if the quadrant bearing value is deleted, all other values are also deleted"""
        self.__del_all_attr()

    @property
    def decimal_degree(self):
        """Returns a float value that represents the decimal degrees clockwise from true north"""
        return self.decimal_degree

    @decimal_degree.setter
    def decimal_degree(self,decimal_degree: float):
        """Sets the Decimal Degree value then recalculates the other formats"""
        self.decimal_degree = decimal_degree
        self.radian = radians(self.decimal_degree)
        self.azimuth_bearing = decimal_degree_to_azimuth(self.decimal_degree)
        self.quad_bearing = decimal_degree_to_quad_bearing(self.decimal_degree)

    @decimal_degree.deleter
    def decimal_degree(self):
        """if the decimal degree value is deleted, all other values are also deleted"""
        self.__del_all_attr()

    @property
    def radian(self):
        """Returns the Radian value calculated clockwise from True North"""
        return self.radian

    @radian.setter
    def radian(self,radian: float):
        """Sets the Radian Degree value then recalculates the other formats"""
        self.radian = radian
        self.decimal_degree = degrees(self.radian)
        self.azimuth_bearing = decimal_degree_to_azimuth(self.decimal_degree)
        self.quad_bearing = decimal_degree_to_quad_bearing(self.decimal_degree)

    @radian.deleter
    def radian(self):
        """if the Radian value is deleted, all other values are also deleted"""
        self.__del_all_attr()

    def __del_all_attr(self):
        """Clears out all attribute values"""
        self.decimal_degree = None
        self.radian = None
        self.azimuth_bearing = None
        self.quad_bearing = None


def parse_bearing(bearing: str) -> float:
    """
    Parses a bearing call into decimal degrees.
    Supports formats like "N45°30'25\"E" or "45°30'25\"".
    
        # Examples:
    
        # Output should be valid when a Quadrant (ie. "NE") is supplied:
        >>> round(parse_bearing("N32°10'32\"E"),6)
        32.175556

        # Output should be valid when a Quadrant (ie. "NE") is *not* supplied:

        >>> round(parse_bearing("32°10'32\""),6)
        32.175556

        # Output should be valid when * is substituted for the ° symbol:
        >>> round(parse_bearing("N60*45'10\"W"),6)
        299.247222

        # In the Southeast Quadrant, the azimuth is equal to 180° less the Bearing:
        >>> parse_bearing("S70°E")
        110.0
     
        # In the Southwest Quadrant, the azimuth is equal to 180° plus the bearing:
        >>> round(parse_bearing("S45°32'W"),6)
        225.533333

        # In the Northwest Quadrant, the azimuth is qual to 360° less the Bearing:
        >>> round(parse_bearing("N60°45'10\"W"),6)
        299.247222
    """
    # bearing = bearing.replace("*", "°")
    match = re.match("([NS])?([0-9]+)([[:punct:]]+)([0-9]+([[:punct:]]+))?([0-9]+([[:punct:]]+))?([EW])?", bearing)
    if not match:
        raise ValueError(f"Invalid bearing format: {bearing}")

    departure, degrees, minutes, seconds, latitude = match.groups()
    degrees = int(degrees) + int(minutes) / 60 + int(seconds) / 3600

    if departure == "S":
        degrees = 180 - degrees if latitude == "E" else 180 + degrees
    elif departure == "N" and latitude == "W":
        degrees = 360 - degrees

    return degrees


def parse_bearing_deprecated(bearing):
    r"""
    Parses a Bearing call (e.g., `N45°30'25"E` or `45°30'25"`) and returns a decimal azimuth degree

    # Args:
        `bearing: (str)` 
            - The bearing string to be parsed
            - Can be supplied with or without the `Departure` (N/S) and `Latitude` (E/W)
            - If `Departure` and `Latitude` are not supplied, the function assumes an north azimuth 

    # Returns:
        `Degree: (float)` The converted Bearing as a decimal degree value
    
    # Examples:
    
        # Output should be valid when a Quadrant (ie. "NE") is supplied:
        >>> round(parse_bearing("N32°10'32\"E"),6)
        32.175556

        # Output should be valid when a Quadrant (ie. "NE") is *not* supplied:

        >>> round(parse_bearing("32°10'32\""),6)
        32.175556

        # Output should be valid when * is substituted for the ° symbol:
        >>> round(parse_bearing("N60*45'10\"W"),6)
        299.247222

        # In the Southeast Quadrant, the azimuth is equal to 180° less the Bearing:
        >>> parse_bearing("S70°E")
        110.0
     
        # In the Southwest Quadrant, the azimuth is equal to 180° plus the bearing:
        >>> round(parse_bearing("S45°32'W"),6)
        225.533333

        # In the Northwest Quadrant, the azimuth is qual to 360° less the Bearing:
        >>> round(parse_bearing("N60°45'10\"W"),6)
        299.247222

    """

    # Replace * with °
    bearing = bearing.replace("*", "°")

    # Check for quadrant indicators (N/S and E/W)
    quad = None
    if len(bearing) > 1 and bearing[0] in "NS" and bearing[-1] in "EW":
        quad = bearing[0] + bearing[-1]
        bearing = bearing[1:-1]  # Remove quadrant indicators from the string

    # Extract degrees
    try:
        deg = int(bearing[:bearing.find("°")])
    except ValueError:
        deg = 0

    # Extract minutes, only if they exist
    min_index = bearing.find("°")+1
    if min_index < len(bearing) and "\'" in bearing:

        try:
            deg_min = int(bearing[bearing.find("°") + 1:bearing.find("'")])
        except ValueError:
            deg_min = 0
    else:
        deg_min = 0

    # Extract seconds, only if they exist
    sec_index = bearing.find("'") + 1
    if sec_index < len(bearing) and '"' in bearing:
        try:
            deg_sec = int(bearing[sec_index:bearing.find('"')])
        except ValueError:
            deg_sec = 0
    else:
        deg_sec = 0

    decimal_degree: float = deg + (deg_min/60) + (deg_sec/3600)

    if quad == "SE":
        adjusted_degree: float = 180 - decimal_degree
    elif quad == "SW":
        adjusted_degree: float = 180 + decimal_degree
    elif quad == "NW":
        adjusted_degree: float = 360 - decimal_degree
    else:
        adjusted_degree: float = decimal_degree

    return adjusted_degree

def decimal_degree_to_azimuth(decimal_degree:float = 0):
    r"""
    converts decimal degrees to azimuth
    
    # Args:
        `decimal_degree: float` Decimal Degrees clockwise from true North.
        
    # Returns:
        `bearing: str` calculated Degrees, Minutes, and Seconds clockwise from true North
        
    # Examples:

        >>> decimal_degree_to_azimuth(32.175556)
        '32°10\'32"'
        
        >>> decimal_degree_to_azimuth(110)
        '110°00\'00"'

    """
    deg: int = floor(decimal_degree)
    deg_min: float = (decimal_degree-deg)*60
    deg_min_normalized: int = floor(deg_min)
    deg_sec: float = (deg_min-deg_min_normalized)*60
    deg_sec_normalized: int = int(round(deg_sec,0))
    if deg_sec_normalized == 60:
        deg_sec_normalized = 0
        deg_min_normalized = deg_min_normalized + 1

    return f"{deg:02}°{deg_min_normalized:02}'{deg_sec_normalized:02}\""

def decimal_degree_to_quad_bearing(decimal_degree):
    r"""
    Converts a decimal degree value into a quadrant bearing with departure and latitude
    
    # Examples:
    
        # No Adjustment for Northeast Quadrant
        >>> decimal_degree_to_quad_bearing(32.175556)
        'N32°10\'32"E'
        
        # Rotation Adjustment for Southeast Quadrant
        >>> decimal_degree_to_quad_bearing(110.000000)
        'S70°00\'00"E'
        
        # Rotatation Adjustment for Southwest Quadrant
        >>> decimal_degree_to_quad_bearing(225.533333)
        'S45°32\'00"W'
        
        # Rotation Adjustment for Northwest Quadrant
        >>> decimal_degree_to_quad_bearing(299.247222)
        'N60°45\'10"W'
    """
    bearing_call: str = None

    if decimal_degree <= 90:
        bearing_call = f"N{decimal_degree_to_azimuth(decimal_degree)}E"
    elif decimal_degree > 90 and decimal_degree <= 180:
        bearing_call = f"S{decimal_degree_to_azimuth(180 - decimal_degree)}E"
    elif decimal_degree > 180 and decimal_degree <= 270:
        bearing_call = f"S{decimal_degree_to_azimuth(decimal_degree-180)}W"
    elif decimal_degree > 270 and decimal_degree <= 360:
        bearing_call = f"N{decimal_degree_to_azimuth(360 - decimal_degree)}W"

    return bearing_call

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True,report=True)
