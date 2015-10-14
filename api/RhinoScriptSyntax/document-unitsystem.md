---
layout: bootstrap
---

# UnitSystem

Return or set the document's unit system. See Rhino's DocumentProperties
        command (Units and Page Units Window) for details
        

### Parameters:

          unit_system = The unit system to set the document to. The unit systems are:
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
          scale [opt] = Scale existing geometry based on the new unit system.
              If not specified, any existing geometry is not scaled (False)
          in_model_units [opt] = Return or modify the document's model units (True)
              or the document's page units (False). The default is True.
        Returns:
          if unit_system is not specified, the current unit system
          if unit_system is specified, the previous unit system
          None on error
        
Help on UnitSystem in module __builtin__

    Provides enumerated values for several unit systems.
    
    enum UnitSystem, values: Angstroms (12), Astronomical (23), Centimeters (3), CustomUnitSystem (11), Decimeters (14), Dekameters (15), Feet (9), Gigameters (18), Hectometers (16), Inches (8), Kilometers (5), Lightyears (24), Megameters (17), Meters (4), Microinches (6), Microns (1), Miles (10), Millimeters (2), Mils (7), Nanometers (13), NauticalMile (22), None (0), Parsecs (25), PrinterPica (21), PrinterPoint (20), Yards (19)
    
    
    
Data and other attributes defined here:

    MemberwiseClone(...)
            MemberwiseClone(self: object) -> object
            
                Creates a shallow copy of the current System.Object.
                

### Returns:

A shallow copy of the current System.Object.
           MemberwiseClone(self: PythonType_1$1) -> object
           MemberwiseClone(self: Object_2$2) -> object
           MemberwiseClone(self: GetObject_3$3) -> object
           MemberwiseClone(self: PythonProperty_4$4) -> object
           MemberwiseClone(self: PythonDictionary_5$5) -> object
           MemberwiseClone(self: PythonTuple_6$6) -> object
           MemberwiseClone(self: _IOBase_7$7) -> object
           MemberwiseClone(self: _RawIOBase_8$8) -> object
           MemberwiseClone(self: _BufferedIOBase_9$9) -> object
           MemberwiseClone(self: _TextIOBase_10$10) -> object
            
   __eq__(...)
           x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y
   __format__(...)
           __format__(formattable: IFormattable, format: str) -> str
            
   __ge__(...)
           __ge__[UnitSystem](y: object, x: UnitSystem) -> object
           __ge__[UnitSystem](x: UnitSystem, y: object) -> object
           __ge__[UnitSystem](x: UnitSystem, y: UnitSystem) -> bool
            
   __gt__(...)
           x.__gt__(y) <==> x>yx.__gt__(y) <==> x>yx.__gt__(y) <==> x>y
   __le__(...)
           __le__[UnitSystem](y: object, x: UnitSystem) -> object
           __le__[UnitSystem](x: UnitSystem, y: object) -> object
           __le__[UnitSystem](x: UnitSystem, y: UnitSystem) -> bool
            
   __lt__(...)
           x.__lt__(y) <==> x<yx.__lt__(y) <==> x<yx.__lt__(y) <==> x<y
   __ne__(...)
           __ne__[UnitSystem](y: object, x: UnitSystem) -> object
           __ne__[UnitSystem](x: UnitSystem, y: object) -> object
           __ne__[UnitSystem](x: UnitSystem, y: UnitSystem) -> bool
            
   __reduce_ex__(...)
           helper for pickle
   __str__(...)
           x.__str__() <==> str(x)
