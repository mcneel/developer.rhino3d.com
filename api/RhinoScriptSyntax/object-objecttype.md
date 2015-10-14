---
layout: bootstrap
---

# ObjectType

Returns the object type
        

### Parameters:

          object_id = identifier of an object
        Returns:
          see help for values
        
Help on object in module __builtin__

    Supports all classes in the .NET Framework class hierarchy and provides low-level services to derived classes. This is the ultimate base class of all classes in the .NET Framework; it is the root of the type hierarchy.
    
    object()
    
    
Data and other attributes defined here:

    Equals(...)
            Equals(objA: object, objB: object) -> bool
            
                Determines whether the specified object instances are considered equal.
            
                objA: The first object to compare.
                objB: The second object to compare.
                Returns: true if the objects are considered equal; otherwise, false. If both objA and 
                 objB are null, the method returns true.
            
            Equals(self: object, obj: object) -> bool
            
                Determines whether the specified System.Object is equal to the current 
                 System.Object.
            
            
                obj: The object to compare with the current object.
                Returns: true if the specified System.Object is equal to the current System.Object; 
                 otherwise, false.
            
            Equals(self: PythonType_1$1, obj: PythonType_1$1) -> bool
            Equals(self: Object_2$2, obj: Object_2$2) -> bool
            Equals(self: GetObject_3$3, obj: GetObject_3$3) -> bool
            Equals(self: PythonProperty_4$4, obj: PythonProperty_4$4) -> bool
            Equals(self: PythonDictionary_5$5, obj: PythonDictionary_5$5) -> bool
            Equals(self: PythonTuple_6$6, obj: object) -> bool
            Equals(self: _IOBase_7$7, obj: _IOBase_7$7) -> bool
            Equals(self: _RawIOBase_8$8, obj: _RawIOBase_8$8) -> bool
            Equals(self: _BufferedIOBase_9$9, obj: _BufferedIOBase_9$9) -> bool
            Equals(self: _TextIOBase_10$10, obj: _TextIOBase_10$10) -> bool
            
    GetHashCode(...)
            GetHashCode(self: object) -> int
            
                Serves as a hash function for a particular type.
                Returns: A hash code for the current System.Object.
            GetHashCode(self: PythonType_1$1) -> int
            GetHashCode(self: Object_2$2) -> int
            GetHashCode(self: GetObject_3$3) -> int
            GetHashCode(self: PythonProperty_4$4) -> int
            GetHashCode(self: PythonDictionary_5$5) -> int
            GetHashCode(self: PythonTuple_6$6) -> int
            GetHashCode(self: _IOBase_7$7) -> int
            GetHashCode(self: _RawIOBase_8$8) -> int
            GetHashCode(self: _BufferedIOBase_9$9) -> int
            GetHashCode(self: _TextIOBase_10$10) -> int
            
    GetType(...)
            GetType(self: object) -> Type
            
                Gets the System.Type of the current instance.
                Returns: The exact runtime type of the current instance.
            
    MemberwiseClone(...)
            MemberwiseClone(self: object) -> object
            
                Creates a shallow copy of the current System.Object.
                Returns: A shallow copy of the current System.Object.
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
            
    ReferenceEquals(...)
            ReferenceEquals(objA: object, objB: object) -> bool
            
                Determines whether the specified System.Object instances are the same instance.
            
                objA: The first object to compare.
                objB: The second object  to compare.
                Returns: true if objA is the same instance as objB or if both are null; otherwise, false.
            
    ToString(...)
            ToString(self: object) -> str
            
                Returns a string that represents the current object.
                

### Returns:

A string that represents the current object.
           ToString(self: PythonType_1$1) -> str
           ToString(self: Object_2$2) -> str
           ToString(self: GetObject_3$3) -> str
           ToString(self: PythonProperty_4$4) -> str
           ToString(self: PythonDictionary_5$5) -> str
           ToString(self: PythonTuple_6$6) -> str
           ToString(self: _IOBase_7$7) -> str
           ToString(self: _RawIOBase_8$8) -> str
           ToString(self: _BufferedIOBase_9$9) -> str
           ToString(self: _TextIOBase_10$10) -> str
            
   __delattr__(...)
           __delattr__(self: object, name: str)
               Removes an attribute from the provided member
            
   __format__(...)
           __format__(self: object, formatSpec: str) -> str
            
   __getattribute__(...)
           __getattribute__(self: object, name: str) -> object
            
               Gets the specified attribute from the object without running any custom lookup 
                behavior
                       (__getattr__ and __getattribute__)
            
            
   __hash__(...)
           x.__hash__() <==> hash(x)
   __init__(...)
           x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature
   __new__(...)
           __new__(cls: type, **kwargs�: dict, *args�: Array[object]) -> object
           __new__(cls: type, *args�: Array[object]) -> object
            
               Creates a new instance of the type
           __new__(cls: type) -> object
            
               Creates a new instance of the type
            
   __reduce__(...)
           helper for pickle
   __reduce_ex__(...)
           helper for picklehelper for pickle
   __repr__(...)
           __repr__(self: object) -> str
            
               Returns the code representation of the object.  The default implementation 
                returns
                       a string which consists of the type and a unique numerical 
                identifier.
            
            
   __setattr__(...)
           __setattr__(self: object, name: str, value: object)
               Sets an attribute on the object without running any custom object defined 
                behavior.
            
            
   __sizeof__(...)
           __sizeof__(self: object) -> int
            
               Returns the number of bytes of memory required to allocate the object.
            
   __str__(...)
           x.__str__() <==> str(x)
   __subclasshook__(...)
           __subclasshook__(*args: Array[object]) -> NotImplementedType
            
