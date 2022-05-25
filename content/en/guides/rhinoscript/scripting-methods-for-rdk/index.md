+++
authors = [ "andy" ]
categories = [ "RDK" ]
description = "This guide enumerates the RhinoScript methods for accessing the RDK."
keywords = [ "RDK", "Rhino", "Renderer", "Scripting" ]
languages = [ "C/C++", "RhinoScript" ]
sdk = [ "C/C++", "RhinoScript" ]
title = "Scripting Methods for RDK (Windows)"
type = "guides"
weight = 2

[admin]
TODO = "needs cleanup and formatting work and to be added to rhinoscript guides"
origin = "http://wiki.mcneel.com/developer/rdkrhinoscripting"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Overview

To get a scripting object for the Rhino RDK, use the following code:

```vbnet
Dim rdk
Set rdk = Rhino.GetPlugInObject("Renderer Development Kit")
```

Then use the RDK object to access the functions below...

## Functions

`FactoryList();`
Return a list of RDK's content factory collection.

**Returns:** Array of strings identifying the factory.

`ContentList(strContentType)`
Returns a list of contents for a certain type: material, texture, environment.

**Parameters:** strContentType = Required. String. Type of content: material, texture or environment.
**Returns:** Array of strings identifying the content. NULL in error conditions.

`DeleteFactory(strFactoryId)`
Deletes a content factory by its identifier.

**Parameters:** strFactoryId = Required. String. The identifier of the factory to delete.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`FactoryKind(strFactoryId)`
Returns the kind of the content.

**Parameters:** strFactoryId = Required. String. The identifier of the factory.
**Returns:** String of the kind of the factory. NULL in error conditions.

`FactoryNewContent(strFactoryId, strParentId)`
Create a new content of the specified type.

**Parameters:**
strFactoryId = Required. String. The identifier of the factory.
strParentId = Optional. String. The identifier of the parent content.
**Returns:** String which identifies new content.   NULL in error conditions.

`FactoryContentTypeId(strFactoryId)`
Returns the identifier of the content type.

**Parameters:** strFactoryId = Required. String. The identifier of the factory.
**Returns:** String which identifies the factory. NULL in error conditions.

`FactoryContentInternalName(strFactoryId)`
Returns the internal name of the content created by specified factory.

**Parameters:** strFactoryId = Required. String. The identifier of the factory.
**Returns:** String which is the internal name of the factory. NULL in error conditions.

`FactoryRenderEngineId(strFactoryId)`
Returns the render engine id of the content that this factory produces.

**Parameters:** strFactoryId = Required. String. The identifier of the factory.
**Returns:** String which is the identifier of the render engine. NULL in error conditions.

`FactoryPlugInId(strFactoryId)`
Returns the plugin id of the plugin that created this factory.

**Parameters:** strFactoryId = Required. String. The identifier of the factory.
**Returns:** String which is the identifier of the plugin. NULL in error conditions.

`FactoryRebuildCache(strFactoryId)`
Rebuild the factory cache. This forces a refresh of cached data such as the factory name.

**Parameters:** strFactoryId = Required. String. The identifier of the factory.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentRenderEngineId(strContentInstanceID)`
Return Render engine identifier.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the render engine. NULL in error conditions.

`ContentPlugInId(strContentInstanceID)`
Return The plugin id of the plugin that defines this content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the plugin. NULL in error conditions.

`ContentTypeId(strContentInstanceID)`
Return The unique id of the content type.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the content type. NULL in error conditions.

`ContentInternalName(strContentInstanceID)`
Return the internal name of the content type.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the internal name of the content. NULL in error conditions.

`ContentTypeName(strContentInstanceID)`
Return the name of the content type.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the name of the content type. NULL in error conditions.

`ContentTypeDescription(strContentInstanceID)`
Return the description of the content type.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the description of the content type. NULL in error conditions.

`ContentCategory(strContentInstanceID)`
Return the category of the content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the category of the content. NULL in error conditions.

`ContentKind(strContentInstanceID)`
Return return a string uniquely identifying the kind of the content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the uniquely identifying the kind of the content. NULL in error conditions.

`ContentLibraryFileExtension(strContentInstanceID)`
Return the library file extension of the content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the library file extension of the content. NULL in error conditions.

`CurrentContent(strContentInstanceID)`
Returns if content is currently selected in thumbnail display.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating if content is selected. NULL in error conditions.

`ContentInstanceName(strContentInstanceID, strName)`
Return content's name.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strName = Optional. String. Use to set content name.
**Returns:** String which is the current name of the content. NULL in error conditions.
`ContentNotes(strContentInstanceID, strNotes, strSendEvent)`
Return the content's notes.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strNotes = Optional. Use to set notes.
bSendEvent = Optional. Use to update UI.
**Returns:** String which are the current notes. NULL in error conditions.

`ContentOpenInThumbnailEditor(strContentInstanceID)`
Call this method to open the content in the relevant thumbnail editor and select it.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.
`ContentParameter(strContentInstanceID, strName, varValue)`
Returns or modifies a content parameter.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strName = Optional. String. Name of the parameter.
varValue = Optional. New value of the parameter.
**Returns:** Array of strings which are the available paramter names when strName not specified. Variant with current value of parameter if strName is specified. NULL in error conditions.

`UngroupContent(strContentInstanceID)`
Remove this content tree from any instance group it may be a member of.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentGroupId(strContentInstanceID)`
Returns the group id which this content is a member of.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the group. NULL in error conditions.

`DeleteContent(strContentInstanceID)`
Delete the content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.
`DuplicateContent(strContentInstanceID)`
Duplicate the content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the new content. NULL in error conditions.

`ContentParent(strContentInstanceID)`
Return parent content or empty string if this is the top level object.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of parent or empty string if this is the top level object. NULL in error conditions.

`ContentFirstChild(strContentInstanceID)`
Return first child of this content or NULL if none.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the child. NULL in error conditions or if no child.

`ContentNextSibling(strContentInstanceID)`
Return first sibling of this content or NULL if none.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the first sibling. NULL in error conditions or if no sibling.

`ContentTopLevelParent(strContentInstanceID)`
Return identifier of top level parent of this content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the top level parent. NULL in error conditions.

`ContentReplaceChild(VARIANT vaContentInstance, strOldChild, strNewChild)`
Replace a child content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strOldChild = Required. The identifier of the old child.
strNewChild = Required. The identifier of the new child.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentAddChild(strContentInstanceID, strContent)`
Adds another content as a child of this content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strContent = Required. String. The identifier of the child content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentChildSlotName(strContentInstanceID, strChildSlotName)`
Return the child-slot-name of this content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
varChildSlotName = Optional. String. The new child slot name
**Returns:** String which is current child slot name. NULL in error conditions.

`ContentChildSlotNameFromParamName(strContentInstanceID, strParamName)`
Return the child-slot-name corresponding to a parameter name.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strParamName = Required. String. The parameter name of the slot name.
**Returns:** String which is the current child slot name. NULL in error conditions.

`ContentParamNameFromChildSlotName(strContentInstanceID, strChildSlotName)`
Return the parameter name corresponding to a child-slot-name.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strChildSlotName = Required. String. The child slot name.
**Returns:** String which is the current parameter name of the child slot. NULL in error conditions.

`ContentFindChild(strContentInstanceID, strChildSlotName)`
Return the immediate child that has the specified child-slot-name or NULL if none.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strChildSlotName = required. String. The child slot name.
**Returns:** String which is the identifier of child content. NULL in error conditions.
`IsContentTypeAcceptableAsChild(strContentInstanceID, strType, strChildSlotName)`
Return true only if content type can be accepted as a child in the specified child slot.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strType = Required. String. The identifier of a content type.
strChildSlotName = Required. String. Name of the child slot.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`IsTypeAcceptableAsChild(strContentInstanceID, strFactory, strChildSlotName)`
Return true only if content produced by pFactory can be accepted as a child in the specified child slot.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strFactory = Required. The identifier of the factory.
strChildSlotName = Required. The name of the child slot.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentGetChildren(strContentInstanceID)`
Return all the children of this content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Array of strings which are the identifier of the child content. NULL in error conditions.

`ContentGetChildSlots(strContentInstanceID)`
Return all child slots.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Array of strings of child slot names. NULL in error conditions.

`ContentFactory(strContentInstanceID)`
Return the factory that creates this type of content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is the identifier of the factory. NULL in error conditions.

`FindContentInstance(strContentInstanceID, strInstance)`
Searches for the content with the specified instance id.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strInstance = Required. String. The identifier of the instance to search for.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentDestroyChildContent(strContentInstanceID, strPlugIn)`
Unlink and destroy all child contents belonging to the specified plugin.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strPlugIn = Required. String. The identifier of the plug-In.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`IsContentCompatible(strContentInstanceID, strRenderEngine)`
A content is compatible with a render engine when its RenderEngineId() matches the id of the render engine.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strRenderEngine = Required. String. The identifier of the render engine.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`IsContentUniversal(strContentInstanceID)`
A content is universal if it is meant to be used with any render engine.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`IsContentPrivate(strContentInstanceID)`
A content is private if it is not intended to show in any editor.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.
`ContentSaveToFile(strContentInstanceID, strFullPath)`
Save the content to a library file.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strFullPath = Required. String. The full path to the library file to be created.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentLoadFromFile(VARIANT vaFullPath)`
Load content from a library file.

**Parameters:** strFullPath = Required. String. The full path to the library file to be created.
**Returns:** String which is the identifier of the content. NULL in error conditions.

`IsContentInDocument(strContentInstanceID)`
Query whether or not the content is in the document.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentEmbeddedFiles(strContentInstanceID)`
Return a semicolon-delimited string of full paths to files used by the content.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
**Returns:** String which is a semicolon-delimited string of full paths. NULL in error conditions.

`ContentSupportsCommand(strContentInstanceID, strCommand)`
Indicates whether or not the content supports a particular command.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strCommand = Required. String. Command identifier.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentExecuteCommand(strContentInstanceID, strCommand)`
Executes a command.

**Parameters:** strContentInstanceID = Required. String. The identifier of the content.
strCommand = Required. String. Command identifier.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`SunEnableAllowed([optional] VARIANT vaAllowed)`
Returns or modifies the sun enable allowed value.

**Parameters:** bAllowed = Optional. Boolean. Use to enable/disable this option.
**Returns:** Boolean which is the current value. NULL in error conditions.

`SunEnableOn(bOn)`
Returns or modifies the sun ON value.

**Parameters:** bOn = Optional. Boolean. Use to enable/disable this option.
**Returns:** Boolean which is the current value. NULL in error conditions.

`SunManualControlAllowed(bAllowed)`
Returns or modifies the ManualControlAllowed value.

**Parameters:** bAllowed = Optional. Boolean. Use to enable/disable this option.
**Returns:** Boolean which is the current value. NULL in error conditions.

`SunManualControlOn(bManual)`
Returns or modifies the ManualControlOn value.

**Parameters:** bManual = Optional. Boolean. Use to enable/disable this option.
**Returns:** Boolean which is the current value. NULL in error conditions.

`SunNorth(dblNorth)`
Returns or modifies the azimuth corresponding to North.

**Parameters:** dblNorth = Optional. Use to set/get north.
**Returns:** Array which is the current value. NULL in error conditions.

`SunVector(vVector)`
Return the sun's direction vector in world space.

**Parameters:** vVector = Optional. Array. 3D-Vector
**Returns:** Array which is the current value. NULL in error conditions.

`SunAzimuth(dblAzimuth)`
Return the azimuth of the sun in degrees.

**Parameters:** dblAzimuth = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunAltitude(dblAltitude)`
Return the altitude of the sun in degrees.

**Parameters:** dblAltitude = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunLatitude(dblLatitude)`
Return the latitude of the observer.

**Parameters:** dblLatitude = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunLongitude(dblLongitude)`
Return the longitude of the observer.

**Parameters:** dblLongitude = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunTimeZone(dblHours)`
Return the time zone of the observer in hours.

**Parameters:** dblHours = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunDaylightSavingOn(bOn)`
Return true if daylight saving is on.

**Parameters:** bOn = Optional. Boolean.
**Returns:** Boolean which is the current value. NULL in error conditions.

`SunDaylightSavingMinutes(intMinutes)`
Return the daylight saving of the observer in minutes.

**Parameters:** intMinutes = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.
`SunLocalDate(intDate)`
Retrieves the local date of the observer.

**Parameters:** intDate = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunLocalTime(dblHours)`
Retrieves the local time of the observer.

**Parameters:** dblHours = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunUTCDate(intDate)`
Retrieves the UTC date of the observer.

**Parameters:** intDate = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunUTCTime(dblHours)`
Retrieves the UTC time of the observer.

**Parameters:** dblHours = Optional. Number.
**Returns:** Number which is the current value. NULL in error conditions.

`SunLight()`
Get an ON_Light which represents the sun.

**Returns:** String which is the identifier of the light. NULL in error conditions.

`MaterialInstanceId(intMaterialTableIndex)`
Returns the content instance id for a given index into the Rhino material table

**Parameters:** intMaterialTableIndex = Required. Number. Index in material table.
**Returns:** String which is the identifier of the content. NULL in error conditions.

`SetMaterialInstanceId(strInstanceId, intMaterialTableIndex)`
Assigns a certain content to a material table index.

**Parameters:** strInstanceId = Required. String. Identifier of content.
intMaterialTableIndex = Required. Number. Index in material table.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.
`HSB2RGB(arrColor)`
Converts color

**Parameters:** arrColor = Required. Array. 3D Array of doubles.
**Returns:** Array of Numbers. NULL in error conditions.

`RGB2HSB(arrColor)`
Converts color.

**Parameters:** arrColor = Required. Array. 3D Array of doubles.
**Returns:** Array of Numbers. NULL in error conditions.

`ShowContentChooser(strDefaultType, strDefaultInstance, strAllowedKinds)`
Shows the content chooser to allow the user to select a new or existing content.

**Parameters:** strDefaultType = Required. String. Is the content type that will be initially selected in the 'New' tab.
strDefaultInstance = Required. String. Is the content instance that will be initially selected in the 'Existing' tab.
strAllowedKinds = Required. Array. List of strings of content kinds that will be displayed.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentKindList()`
Returns list of content kinds.

**Returns:** Array of strings of content kinds. NULL in error conditions.

`SelectedContent(strContentType)`
Get the selected content of the specified kind.

**Parameters:** strContentType = Required. String. Content type to look for selection.
**Returns:** String which is the identifier of the selected content. NULL in error conditions.
`OpenFloatingContentPreview(strContentInstanceID, arrPos, arrSize)`
Open content preview window.

**Parameters:** strContentInstanceID = Required. String. Content identifier.
arrPos = Required. Array. 2D array of integers x,y.
arrSize = Required. Array. 2D array of integers width, height.
**Returns:** String which is the identifier of the preview window. NULL in error conditions.

`CloseFloatingContentPreview(strWindowId)`
Close content preview window.

**Parameters:** strWindowId = Required. String. Identifier of preview window.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ContentResetToDefaults(strContentInstanceID)`
Reset content to defaults.

**Parameters:** strContentInstanceID = Required. String. Content identifier.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.

`ChangeContent(strContentInstanceID, strNewContentId, bHarvest)`
Change content.

**Parameters:** strContentInstanceID = Required. String. Content identifier.
strNewContentID = Required. String. Content identifier to change too.
bHarvest = Required. Boolean. Determines whether or not parameter harvesting will be performed.
**Returns:** Boolean True or false indicating success or failure. NULL in error conditions.
