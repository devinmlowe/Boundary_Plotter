# COGOpro Feature Replication TODO

This document identifies the functions and tools available in SGSS COGOpro (COGO+ Pro)
and tracks progress toward replicating them in Boundary_Plotter.

**Reference:** [SGSS COGO+ Pro](https://sgss.ca/hpprime.html) |
[COGO+ v4.10 Reference Manual](https://sgss.ca/files/COGO+_Version_4.pdf) |
[Feature Comparison](https://sgss.ca/files/COGO+_Comparisons.pdf)

---

## Legend

- [x] Already implemented in Boundary_Plotter
- [ ] Not yet implemented — needs to be built

---

## 1. Settings / Configuration

- [ ] **Angle Unit Modes** — Support DMS (degrees/minutes/seconds), decimal degrees (DEG), and gradians/gons (GRD)
- [x] **Bearing/Azimuth Modes** — Support North Azimuth (AZ) and Quadrant Bearings (QB)
- [ ] **South Azimuth Mode** — Support South Azimuth (SA) bearing format
- [ ] **Distance Units** — Support metres and feet (with conversion between them)
- [ ] **Coordinate Order** — Configurable as N,E (Northing/Easting), E,N (Easting/Northing), or X,Y
- [ ] **Geodetic Settings** — Coordinate system selection with pre-defined projection parameters for grid↔geodetic conversions

---

## 2. COGO Menu

### 2.1 Point Traverse

- [ ] **Point Traverse (Standard Mode)** — Enter bearing/azimuth and distance to compute the next point's coordinates from a known starting point
- [ ] **Point Traverse (Sideshot Mode)** — Compute a point from an occupied point without advancing the traverse (observation-only point)
- [ ] **Curve Traverse** — Traverse along a curve (arc) segment, computing the endpoint from arc parameters (radius, delta angle, chord bearing, etc.)

### 2.2 Inverse

- [ ] **Inverse (Point to Point)** — Compute the bearing and distance between two known coordinate points
- [ ] **Inverse Curve (Three Point)** — Compute curve parameters (radius, delta, arc length, chord) from three points on a curve; supports CW/CCW direction
- [ ] **Inverse Angle** — Compute the angle at a point formed by two lines (backsight-instrument-foresight)
- [ ] **Inverse Point to Line** — Compute the perpendicular offset distance and station of a point relative to a defined line
- [ ] **Inverse Point to Alignment** — Compute station, offset, and cut/fill values for points relative to a centreline alignment

### 2.3 Intersections

- [ ] **Bearing-Bearing Intersection** — Find the point where two bearing lines (from two known points) intersect
- [ ] **Bearing-Distance Intersection** — Find the point(s) where a bearing line from one point intersects a circle of given radius around another point (may yield 2 solutions)
- [ ] **Distance-Bearing Intersection** — Same as above with reversed input order
- [ ] **Distance-Distance Intersection** — Find the point(s) where two circles (defined by centre points and radii) intersect (may yield 2 solutions)

### 2.4 Area

- [ ] **Area by Points (Straight Segments)** — Compute the area enclosed by a polygon defined by coordinate points connected by straight lines
- [ ] **Area by Points (Curved Segments)** — Compute the area enclosed by a polygon that includes arc/curve segments between some points

### 2.5 Fit Points

- [ ] **Fit Points — Best-Fit Straight Line** — Compute the best-fit straight line through a set of points (least squares)
- [ ] **Fit Points — Best-Fit Curve** — Compute the best-fit curve (arc) through a set of points
- [ ] **Fit Points — Double Proportion** — Re-establish a lost corner using the double proportion method from adjacent found corners

---

## 3. Adjustments Menu

### 3.1 Traverse Adjustments

- [ ] **Compass Rule (Bowditch) — Closed Figure** — Distribute linear misclose proportionally through each leg of a traverse that returns to its starting point
- [ ] **Compass Rule (Bowditch) — Close to Fixed Point** — Distribute linear misclose for a traverse that ends on a known control point

### 3.2 Coordinate Transformations

- [ ] **Rotate** — Rotate a set of points about a given centre by a specified angle
- [ ] **Mirror** — Mirror/reflect a set of points about a given axis
- [ ] **Shift** — Translate/shift a set of points by given northing and easting offsets
- [ ] **Average** — Compute average coordinates from multiple observations of the same points
- [ ] **Scale** — Scale coordinates from a fixed point by a given scale factor
- [ ] **Helmert Transformation** — 4-parameter similarity transformation (scale, rotation, translation) computed via least squares from a minimum of two common control points in two coordinate systems

---

## 4. Surveying Menu (Pro Features)

### 4.1 Traverse Plus (3D Traverse)

- [ ] **Setup** — Instrument setup with height of instrument (HI) and occupied/backsight point management
- [ ] **Enter and Record** — Record horizontal angle, vertical angle, and slope distance observations; compute 3D coordinates
- [ ] **Stake Points** — Compute the horizontal angle turn and distance from the current setup to stake (layout) a target point
- [ ] **Stake Alignment** — Compute stake-out data to layout points along a defined alignment (centreline with offsets)

### 4.2 Levelling

- [ ] **Levelling Job Manager** — Manage levelling observation data (benchmarks, turning points, intermediate shots)
- [ ] **Level Notes Entry** — Enter rod readings (backsight, intermediate, foresight) and compute elevations with misclose

### 4.3 Alignments

- [ ] **Horizontal Alignment Definition** — Define a horizontal alignment as a series of tangent and curve segments (PI stations, curve data)
- [ ] **Vertical Alignment Definition** — Define a vertical profile with VPIs (vertical points of intersection) and vertical curves
- [ ] **3D Alignment Computation** — Compute station, offset, and elevation for points along the combined horizontal/vertical alignment

### 4.4 Inaccessible Point

- [ ] **Inaccessible Point Calculation** — Compute the coordinates of an inaccessible point by observing angles from two or more known setup positions

---

## 5. Tools Menu

### 5.1 Solvers

- [ ] **Triangle Solver** — Solve a triangle given any valid combination of sides and angles (SSS, SAS, ASA, AAS, SSA); compute all unknown sides, angles, and area
- [ ] **Horizontal Curve Solver** — Solve circular curve parameters (radius, delta angle, arc length, tangent length, chord, mid-ordinate, external distance, degree of curve); solve sub-chords by station or interval
- [ ] **Vertical Curve Solver** — Solve vertical parabolic curve parameters (PVI elevation, grade in/out, length, high/low point, elevations at stations)

### 5.2 Calculator & Utilities

- [ ] **RPN Calculator** — Surveyor-focused RPN calculator with unit conversions, stack manipulation, and 2D/3D vector entry/editing
- [ ] **Coordinate Converter** — Convert between grid coordinates, geodetic coordinates (latitude/longitude), and cartesian (ECEF) coordinates across many global coordinate systems

---

## 6. Points Database / Management

- [ ] **Point Storage** — Store and recall 3D coordinates (Northing, Easting, Elevation) with point numbers
- [ ] **Point Editing** — Edit existing point coordinates and descriptions
- [ ] **Point Deletion** — Delete individual or ranges of points
- [ ] **Point Renumbering** — Renumber points or ranges of points
- [ ] **Point Plotting** — Plot/visualize stored points on a coordinate display

---

## 7. Data Exchange / Import-Export

- [ ] **CSV Import/Export** — Import and export coordinate data in CSV format
- [ ] **KML Export** — Export points to KML files for Google Earth visualization
- [ ] **DXF Export** — Export points and figures to DXF files for CAD software
- [ ] **LandXML Import** — Import alignment data from LandXML format
- [ ] **STAR*NET Export** — Export level observations in STAR*NET format
- [ ] **HTML Reports** — Generate formatted HTML reports for traverse closures and other computations

---

## 8. Existing Boundary_Plotter Features (Already Implemented)

These features from COGOpro are already present in this project:

- [x] **Bearing Parsing** — Parse bearing strings (quadrant and azimuth format) into decimal degrees (`parse_bearing()`)
- [x] **Decimal Degrees → Azimuth** — Convert decimal degrees to DMS azimuth format (`decimal_degree_to_azimuth()`)
- [x] **Decimal Degrees → Quadrant Bearing** — Convert decimal degrees to quadrant bearing format (`decimal_degree_to_quad_bearing()`)
- [x] **Angle Class** — Object with synchronized azimuth, quadrant bearing, decimal degree, and radian representations
- [x] **Interactive CLI** — Command-line interface for running conversions
- [x] **COM Server / Excel Integration** — Windows COM server with VBA macros for Office use

---

## Priority Recommendations

The following implementation order is suggested based on building from foundation to advanced features:

1. **Points Database** (Section 6) — Foundation for all other COGO operations
2. **Point Traverse** (Section 2.1) — Core COGO functionality
3. **Inverse** (Section 2.2) — Essential companion to traverse
4. **Intersections** (Section 2.3) — Core COGO computation
5. **Area Calculation** (Section 2.4) — Common field requirement
6. **Triangle / Curve Solvers** (Section 5.1) — Standalone utility tools
7. **Compass Rule Adjustment** (Section 3.1) — Traverse quality control
8. **Coordinate Transformations** (Section 3.2) — Data manipulation
9. **Data Exchange** (Section 7) — Interoperability (CSV, DXF, KML)
10. **Surveying Menu** (Section 4) — Advanced 3D features
11. **Settings & Configuration** (Section 1) — Unit/format flexibility
12. **Coordinate Converter / Geodetic** (Section 5.2) — Projection handling
