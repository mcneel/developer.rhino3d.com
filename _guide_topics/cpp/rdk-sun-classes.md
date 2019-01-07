---
title: RDK Sun classes
description: This document describes how to use the RDK sun classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin']
layout: toc-guide-page
---

### IRhRdkSun
<a name="IRhRdkSun"></a>
_IRhRdkSun_ is an abstract sun interface. It provides access to all the properties of a sun. It can be used to modify the RDK Document Sun or any temporary 'working' sun you might have access to.

### CRhRdkSun
<a name="CRhRdkSun"></a>
_CRhRdkSun_ is a simple sun object that can be placed on the stack or used as a class member. It can be used as a temporary 'working' sun and it provides access to an underlying implementation of IRhRdkSun. You can use this to do sun angle calculations without affecting the document sun. This might be useful, for example, to create an ephemeris or some other table of sun information. The following is a test command that uses CRhRdkSun to generate a display of the monthly sun position for the year 2025 at Seattle, Washington, USA.
```cpp
static class CTestSunEphemeris : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = { your_uuid_here } }; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"TestSunEphemeris"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theTestSunEphemerisCmd;

CRhinoCommand::result CTestSunEphemeris::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	// Make a temporary sun and set some properties.
	CRhRdkSun s;
	auto& sun = s.Sun();
	sun.SetManualControlOn(false);

	// Set the observer's location to Seattle, Washington, USA.
	sun.SetLatitude(47.606);
	sun.SetLongitude(-122.331);
	sun.SetTimeZone(-8.0);

	static const wchar_t* aMonth[12] =
		{ L"Jan", L"Feb", L"Mar", L"Apr", L"May", L"Jun",
		  L"Jul", L"Aug", L"Sep", L"Oct", L"Nov", L"Dec" };

	// Display sun horizon coordinates for Seattle at noon on the first day
	// of each month of 2025 and add a light to show the direction.
	int day = 1, year = 2025;
	for (int i = 0; i < 12; i++)
	{
		// Set the date and time. Disregard daylight saving time.
		const int month = i + 1;
		sun.SetLocalDateTime(year, month, day, 12.0);

		RhinoApp().Print(L"Date: %04u.%02u.%02u - Sun Azimuth: %.1f, Sun Altitude: %.1f\n",
		                 year, month, day, sun.Azimuth(), sun.Altitude());

		// Add a light to the document to show the position.
		auto light = sun.Light();
		const double angle = 2.0 * ON_PI * (2 - i) / 12.0;
		light.Translate(ON_3dVector(10.0 * cos(angle), 10.0 * sin(angle), 0.0));
		pDoc->m_light_table.AddLight(light);

		// Add text for the month.
		const auto point = ON_3dPoint(14.0 * cos(angle) - 1.3, 14.0 * sin(angle) + 0.5, 0.0)
		pDoc->AddTextObject(aMonth[i], ON_Plane(), point);
	}

	pDoc->DeferredRedraw();

	return success;
}
```
### CRhRdkSunDialog
<a name="CRhRdkSunDialog"></a>
_CRhRdkSunDialog_ is a wrapper around a sun UI. TODO: data source.

<a name="DocumentSun"></a>
### The RDK Document Sun
The _RDK Document Sun_ is a document-resident sun which affects viewports and renderings. If you have a Rhino document, you can read and write that document's sun through the document's IRhRdkSun interface. Any changes you make will appear in the main sun UI and will also be stored in the 3dm file. Getting the sun from a document always returns a const reference. To write to the sun, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system.
```cpp
  // Read some information from the document sun.
  const auto& sun = pDoc->Sun();
  const bool b = sun.EnableOn();
  ... // Read other properties here.

  // Change some properties of the document sun.
  auto& write_sun = sun.BeginChange(RhRdkChangeContext::Program);
  write_sun.SetEnableOn(true);
  ... // Set other properties here.
  write_sun.EndChange();
```
