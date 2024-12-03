"""Tools to Parse Bearing and Distance Calls into Vectors, Coordinates, and Lines."""

def parse_bearing(bearing):
    r"""
    Parses a Bearing call (e.g., `N45°30'25"E` or `45°30'25"`) and returns a decimal azimuth degree

    # Args:
        `bearing: (str)` 
            - The bearing string to be parsed
            - Can be supplied with or without the `Departure` (N/S) and `Latitude` (E/W)
            - If `Departure` and `Latitude` are not supplied, the function assumes an north azimuth 

    # Returns:
        `Degree: (float)` The converted Bearing as a decimal degree value rounded to the 6th decimal
    
    # Examples:
    
        # Output should be valid when a Quadrant (ie. "NE") is supplied:
        >>> parse_bearing("N32°10'32\"E")
        32.175556

        # Output should be valid when a Quadrant (ie. "NE") is *not* supplied:

        >>> parse_bearing("32°10'32\"")
        32.175556

        # Output should be valid when * is substituted for the ° symbol:
        >>> parse_bearing("N60*45'10\"W")
        299.247222

        # In the Southeast Quadrant, the azimuth is equal to 180° less the Bearing:
        >>> parse_bearing("S70°E")
        110.0
     
        # In the Southwest Quadrant, the azimuth is equal to 180° plus the bearing:
        >>> parse_bearing("S45°32'W")
        225.533333

        # In the Northwest Quadrant, the azimuth is qual to 360° less the Bearing:
        >>> parse_bearing("N60°45'10\"W")
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

    return round(adjusted_degree,6)

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
