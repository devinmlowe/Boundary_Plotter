'@Folder("Angles")
Option Explicit

Function ParseBearingToDecimal(bearing As String) As Double
    '''
    'Requires that com_server.py is registered
    'in the system registry
    '''
    Dim parser As Object
    Dim result As Double

    On Error GoTo ErrorHandler

    ' Create COM object
    Set parser = CreateObject("BearingParser.Application")

    ' Call the COM method and parse the bearing
    result = parser.ParseBearing(bearing)

    ' Return the parsed result
    ParseBearingToDecimal = result
    Exit Function

ErrorHandler:
    ' Handle errors and return a default value
    ' Debug.Print "An error occurred: " & Err.Description, vbCritical, "Error"
    ParseBearingToDecimal = na()
End Function

