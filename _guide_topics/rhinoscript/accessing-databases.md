---
title: Accessing Databases
description: This guide demonstrates how to access databases from VBScript using RhinoScript.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Interoperability', 'Databases', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/database
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Overview

Probably the most popular use for VBScript is connecting to databases.  It's incredibly useful and surprisingly easy.

The first thing you need is the database, of course.  A variety of programs can be used to create it, but probably the most popular is Microsoft Access.  You can also use FoxPro or create it directly in an SQL Server using whichever utilities are supplied with the server.

In this example, we will connect to a simple Microsoft Access database. You can download the database used in this demonstration [here]({{site.baseurl}}/files/test_access_mdb.zip).

Most VBScript developers use Microsoft's ADO (ActiveX database objects) to get data from database.  ADODB is comprised of 3 main objects: Connection, RecordSet, and Command.  We will demonstrate the first two objects.

## Connecting to a Database

The Datasource is essentially a connection from the server or workstation to a database, which can either be on a dedicated machine running SQL server or a database file sitting somewhere on the web server.

To specify what database you would like to use, you need to add a DSN. That is short for Data Source Name.  Data Source Name provides connectivity to a database through an ODBC driver.  The DSN contains database name, directory, database driver, UserID, password, and other information.  Once you create a DSN for a particular database, you can use the DSN in an application to call information from the database.

There are essentially two types of Datasources (DSN's):

1. **System DSN** - A datasource created on the web server by the administrator of the server. T he most popular type of DSN and generally a lot more reliable.
2. **File DSN** - Essentially a connection that your script makes itself each time access to the database is required, specifying the path to and name of the database.  The database must reside on the server in a directory that your script can access for this to work.

The code below is designed around a System DSN named “test” that points to the above database.  You can create System DSNs using the Data Sources (OBDC) applet found in Control Panel.  In Windows, the shortcut to the ODBC control panel can be found in the following location:

*Start* > *Control Panels* > *Administrative Tools* > *Data Sources (ODBC)*

## Working with Recordsets

In order to read information from a Datasource, you need to open a 'Recordset' - a set of database records based on some type of criteria, either all of the records in a table or those matching some condition or set of conditions.

## Sample

The following example RhinoScript code demonstrates how to connect to a system DSN named “test” and read point coordinate records from a table named “points.”

```vbnet
Sub Test
   Const adOpenStatic = 3
   Const adLockOptimistic = 3
   Const adUseClient = 3

   Dim objConnection, objRecordset
   Set objConnection = CreateObject("ADODB.Connection")
   Set objRecordset = CreateObject("ADODB.Recordset")

   objConnection.Open "DSN=test;"
   objRecordset.CursorLocation = adUseClient
   objRecordset.Open "SELECT * FROM points" , objConnection, adOpenStatic, adLockOptimistic

   objRecordSet.MoveFirst

   Dim x, y, z
   Do Until objRecordset.EOF
    x = objRecordset.Fields.Item("x")
    y = objRecordset.Fields.Item("y")
    z = objRecordset.Fields.Item("z")
    Rhino.AddPoint Array(x,y,z)
    objRecordset.MoveNext
   Loop

   objRecordset.Close
   objConnection.Close

 End Sub
```
