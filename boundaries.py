"""Tools to Parse Bearing and Distance Calls into Vectors, Coordinates, and Lines."""

def convertBearingToDecimalDegree(self, bearing):
    """Parse a bearing into an angle"""

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

    """
    In the Northeast Quadrant, the bearing and azimuth are the same
    In the SouthEast Quadrant, subtract the bearing from 180* to get the azimuth
    In the SouthWest Quadrant, add the bearing to 180* to ge the azimuth
    In the NorthWest Quadrant, subtract the bearing from 360* to get the azimuth
    """
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

def parseBearing(bearing):
    r"""
    Parse a bearing into its constituent degrees, minutes, and seconds.

    The function takes a bearing string (e.g., "N45°30'25\"E") and returns a list 
    containing the quadrant (e.g., "NE"), degrees, minutes, and seconds.

    Args:
        self: The instance of the class (if this is a method of a class).
        bearing (str): The bearing string to parse.

    Returns:
        list: A list containing:
            - Quadrant as a string (e.g., "NE").
            - Degrees as an integer.
            - Minutes as an integer.
            - Seconds as an integer.

    Examples:
        >>> parseBearing("N45°30'25\"E")
        ['NE', 45, 30, 25]

        >>> parseBearing("S10°15'50\"W")
        ['SW', 10, 15, 50]

        >>> parseBearing("N00°00'00\"W")
        ['NW', 0, 0, 0]
        
        Check for * Asterisk substition success:
        >>> parseBearing("N45*30'25\"E")
        ['NE', 45, 30, 25]
        
        Check for empty or missing values:
        >>> parseBearing("N45*E")
        ['NE', 45, 0, 0]
        
        Function will return regular azimuth value if departure and latitude are not supplied:
        >>> parseBearing("45*30'25\"")
        ['', 45, 30, 25]
        
    """
    
    bearing = bearing.replace("*", "°")
    
    quad = bearing[0] + bearing[-1]
    try:    
        deg = int(bearing[1:bearing.find("°")])
    except:
        deg = 0
    try:
        min = int(bearing[bearing.find("°") + 1:bearing.find("'")]) 
    except:
        min = 0
    try: 
        sec = int(bearing[bearing.find("'") + 1:bearing.find('"')])
    except:
        sec = 0
    return [quad, deg, min, sec]
   
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)