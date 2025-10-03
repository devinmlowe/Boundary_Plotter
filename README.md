
# **Survey Bearing Conversion Tool**

## **Overview**

This project is a Python-based library for parsing and converting survey bearings into different formats, designed to simplify handling and visualizing survey data. These tools are foundational components for a future system to output vectors and distances in for visualization in other more full-featured tools such as **FreeCAD**, **Matplotlib**, **Excel**, **AutoCAD**, and **IfcOpenShell**.

---

## **Features**

- **Bearing Parsing**:
  - Convert quadrant bearings (e.g., `N32°10'32"E`) into decimal degrees.
  - Parse azimuths and hybrid formats into machine-readable data.
- **Format Conversions**:
  - Convert decimal degrees into azimuth bearings or quadrant bearings.
  - Normalize degree values and handle alternative symbols (e.g., `*` for `°`).
- **Support for Survey Conventions**:
  - Adjust degrees based on quadrants (e.g., Southeast, Southwest).
  - Handle missing quadrant information gracefully.

---

## **Modules**

### **`angles.py`**

Core functionality for parsing and converting survey data.

- **Key Classes**:
  - `Angle`: A representation of an angle supporting multiple formats (azimuth, quadrant, decimal degrees, radians). Automatically updates all formats when one is changed.

- **Key Functions**:
  - `parse_bearing(bearing: str) -> float`: Converts a bearing string into decimal degrees.
  - `decimal_degree_to_azimuth(decimal_degree: float) -> str`: Converts decimal degrees into azimuth bearings (e.g., `32°10'32"`).
  - `decimal_degree_to_quad_bearing(decimal_degree: float) -> str`: Converts decimal degrees into quadrant bearings (e.g., `N32°10'32"E`).

---

## **Tests**

Comprehensive test coverage is provided using `pytest` in the `test_angles.py` module. Key test cases include:

- **Bearing Parsing**:
  - With or without quadrant information.
  - Adjustments for Southeast, Southwest, and Northwest quadrants.
  - Substitution of `*` for `°`.
- **Conversions**:
  - Decimal degrees to azimuth bearings.
  - Decimal degrees to quadrant bearings for all quadrants.
- **Edge Cases**:
  - Missing minutes/seconds.
  - Validation of normalized degree values.

Run the tests:

```bash
pytest test_angles.py
```

---

## **Examples**

### Parsing Bearings

```python
from angles import parse_bearing

# Parse quadrant bearing
bearing = parse_bearing("N32°10'32"E")
print(bearing)  # Output: 32.175556

# Parse azimuth without quadrant
bearing = parse_bearing("32°10'32"")
print(bearing)  # Output: 32.175556
```

### Converting Bearings

```python
from angles import decimal_degree_to_azimuth, decimal_degree_to_quad_bearing

# Decimal degrees to azimuth
azimuth = decimal_degree_to_azimuth(32.175556)
print(azimuth)  # Output: '32°10\'32"'

# Decimal degrees to quadrant
quad_bearing = decimal_degree_to_quad_bearing(110.000000)
print(quad_bearing)  # Output: 'S70°00\'00"E'
```

---

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/survey-bearing-conversion.git
   cd survey-bearing-conversion
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## **Planned Features**

- **Vector Conversion**:
  - Generate coordinate vectors from bearings and distances.
- **Integration**:
  - Export to FreeCAD, AutoCAD, and Excel.
  - Visualize in Matplotlib.
- **Enhanced Parsing**:
  - Handle custom survey formats.
  - Robust error handling.

---

## **License**

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

## **Contributing**

Contributions are welcome! Please open issues or submit pull requests with improvements or bug fixes.
