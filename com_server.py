"""
Deep Integration of Bearing Tools with Microsoft Office

# Requirements:
- `pywin32` - must be registered using `python Scripts/pywin32_postinstall.py -install` with admin privilages
- `com_server.py` - must be registered using `python com_server.py --register`

"""

import pythoncom
from win32com.server import dispatcher
from angles import parse_bearing

class BearingParser:
    _reg_progid_ = "BearingParser.Application"
    _reg_clsid_ = "{b3e0fe4d-050f-4003-8c6c-14921d86df74}"  # Generate a unique GUID
    _public_methods_ = ["ParseBearing"]

    def ParseBearing(self, bearing):
        return parse_bearing(bearing)

if __name__ == "__main__":
    import win32com.server.register
    win32com.server.register.UseCommandLine(BearingParser)
