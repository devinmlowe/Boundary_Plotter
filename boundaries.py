"""Tools to Parse Bearing and Distance Calls into Vectors, Coordinates, and Lines."""

from dataclasses import dataclass


def convertAzimuthToDecimalDegree(quad: str, deg: int, min: int, sec: int):
    """
    The function takes a parsed data from a bearing (e.g., "N45°30'25\"E") and returns the azimuth
    represented as a decimal degree value.

    Args:
        quad (str): Quadrant as a string (e.g., "NE") or None if no quadrant is supplied.
        deg (int): Degrees as an integer.
        min (int): Minutes as an integer.
        sec (int): Seconds as an integer.

    Returns:
        DecimalDegree: The provided Azimuth as a decimal degree, adjusted for quadrant if supplied

    Examples:
        Azimuth with no Quadrant and all zeroes should point to north, or 0° and recieve no additional correction based on Quadrant
        >>> convertAzimuthToDecimalDegree(None,0,0,0)
        0.000000

        Azimuth to North-East Quadrant should be 0.000000
        >>> convertAzimuthToDecimalDegree("NE",0,0,0)
        0.000000

        Azimuth to South-East Quadrant should be 90.000000
        >>> convertAzimuthToDecimalDegree("SE",0,0,0)
        90.000000

        Azimuth to South-West Quadrant should be 180.000000
        >>> convertAzimuthToDecimalDegree("SW",0,0,0)
        180.000000

        Azimuth to North-West Quadrant should be 270.000000
        >>> convertAzimuthToDecimalDegree("NW",0,0,0)
        270.000000
    """

    # Determine adjustment based on Quadrant
    if quad == None:
        """No Adjustment for pure azimuth"""
    if quad == "NE":
        """In the Northeast quadrant the Azimuth and Bearing is the same"""
    if quad == "SE":
        """
        In the Southeast quadrant, subtract the Bearing from 180 degrees to get the Azimuth:
        `180* - S51*25'13"E = AZ 128*34'47"`
        """
    if quad == "SW":
        """
        In the Southwest quadrant, add the Bearing to 180 degrees to get the Azimuth:
        `S46*20'30"W + 180 = AZ 226*20'30"`
        >>>print("test")
        test
        """
    if quad == "NW":
        """
        In the Northwest quadrant, subtract the Bearing from 360 degrees to get the Azimuth:
        `360 - N51*25'41"W = AZ 308*34'19"`
        """

    return None


def parseBearing(bearing):
    r"""
    Parse a bearing into its constituent degrees, minutes, and seconds.

    The function takes a bearing string (e.g., "N45°30'25\"E") and returns a list
    containing the quadrant (e.g., "NE"), degrees, minutes, and seconds.

    Args:
        bearing (str): The bearing string to parse.

    Returns:
        list: A list containing:
            - Quadrant as a string (e.g., "NE") or None if no quadrant is supplied.
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

        Check for * Asterisk substitution success:
        >>> parseBearing("N45*30'25\"E")
        ['NE', 45, 30, 25]

        Check for empty or missing values:
        >>> parseBearing("N45*E")
        ['NE', 45, 0, 0]

        Function will return None for the quadrant if departure and latitude are not supplied:
        >>> parseBearing("45*30'25\"")
        [None, 45, 30, 25]
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
        deg = int(bearing[: bearing.find("°")])
    except ValueError:
        deg = 0

    # Extract minutes, only if they exist
    min_index = bearing.find("°") + 1
    if min_index < len(bearing) and "'" in bearing:
        try:
            min = int(bearing[bearing.find("°") + 1 : bearing.find("'")])
        except ValueError:
            min = 0
    else:
        min = 0

    # Extract seconds, only if they exist
    sec_index = bearing.find("'") + 1
    if sec_index < len(bearing) and '"' in bearing:
        try:
            sec = int(bearing[sec_index : bearing.find('"')])
        except ValueError:
            sec = 0
    else:
        sec = 0

    return [quad, deg, min, sec]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
