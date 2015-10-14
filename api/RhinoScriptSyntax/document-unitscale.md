---
layout: bootstrap
---

# UnitScale

Return the scale factor for changing between unit systems.
      

### Parameters:

- ***to_system*** = The unit system to convert to. The unit systems are are:
   0 - No unit system
   1 - Microns (1.0e-6 meters)
   2 - Millimeters (1.0e-3 meters)
   3 - Centimeters (1.0e-2 meters)
   4 - Meters
   5 - Kilometers (1.0e+3 meters)
   6 - Microinches (2.54e-8 meters, 1.0e-6 inches)
   7 - Mils (2.54e-5 meters, 0.001 inches)
   8 - Inches (0.0254 meters)
   9 - Feet (0.3408 meters, 12 inches)
  10 - Miles (1609.344 meters, 5280 feet)
  11 - *Reserved for custom Unit System*
  12 - Angstroms (1.0e-10 meters)
  13 - Nanometers (1.0e-9 meters)
  14 - Decimeters (1.0e-1 meters)
  15 - Dekameters (1.0e+1 meters)
  16 - Hectometers (1.0e+2 meters)
  17 - Megameters (1.0e+6 meters)
  18 - Gigameters (1.0e+9 meters)
  19 - Yards (0.9144  meters, 36 inches)
  20 - Printer point (1/72 inches, computer points)
  21 - Printer pica (1/6 inches, (computer picas)
  22 - Nautical mile (1852 meters)
  23 - Astronomical (1.4959787e+11)
  24 - Lightyears (9.46073e+15 meters)
  25 - Parsecs (3.08567758e+16)
from_system [opt] = the unit system to convert from (see above). If omitted,
    the document's current unit system is used
      

### Returns:


scale factor for changing between unit systems
      
