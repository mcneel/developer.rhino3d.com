//
// Program.cs
// SortYaml
//
// Created by dan (dan@mcneel.com) on 1/4/2016
// Copyright 2016 Robert McNeel & Associates.  All rights reserved.
//
using System;
using System.Collections.Generic;
using System.IO;

namespace SortYaml
{
  class MainClass
  {
    public static void Main (string[] args)
    {
      foreach(string path in args)
      {
        if(File.Exists(path))
        {
          ProcessFile(path);
        }
        else if(Directory.Exists(path))
        {
          ProcessDirectory(path);
        }
        else
        {
          Console.WriteLine("{0} is not a valid file or directory.", path);
        }
      }
    }

    public static void ProcessDirectory(string targetDirectory)
    {
      // Process the list of files found in the directory.
      string [] fileEntries = Directory.GetFiles(targetDirectory, "*.md");
      foreach(string fileName in fileEntries)
        ProcessFile(fileName);

      // Recurse into subdirectories of this directory.
      string [] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
      foreach(string subdirectory in subdirectoryEntries)
        ProcessDirectory(subdirectory);
    }

    public static void ProcessFile(string path)
    {
      string[] lines = System.IO.File.ReadAllLines (path);

      // find the index of the first "---"
      int firstYamlSeparatorIndex = 0;
      for (int i = 0; i < lines.Length; i++) {
        if (lines [i].StartsWith ("---", StringComparison.Ordinal)) {
          firstYamlSeparatorIndex = i;
          break;
        }
      }

      // find the index of the second "---"
      int secondYamlSeparatorIndex = 0;
      for (int j = firstYamlSeparatorIndex+1; j < lines.Length; j++) {
        if (lines [j].StartsWith ("---", StringComparison.Ordinal)) {
          secondYamlSeparatorIndex = j;
          break;
        }
      }

      // each field has an index, which we need to find below...
      int titleIndex = 0;
      int descriptionIndex = 0;
      int authorsIndex = 0;
      int authorContactsIndex = 0;
      int sdkIndex = 0;
      int languagesIndex = 0;
      int platformsIndex = 0;
      int categoriesIndex = 0;
      int originIndex = 0;
      int orderIndex = 0;
      int keywordsIndex = 0;
      int layoutIndex = 0;
      int categoryPageIndex = 0;
      int TODOIndex = 0;

      // find and set the indices, if the fields are present...
      for (int k = firstYamlSeparatorIndex; k < secondYamlSeparatorIndex; k++) {
        if (lines [k].StartsWith ("title:", StringComparison.Ordinal))
          titleIndex = k;
        if (lines [k].StartsWith ("description:", StringComparison.Ordinal))
          descriptionIndex = k;
        if (lines [k].StartsWith ("authors:", StringComparison.Ordinal))
          authorsIndex = k;
        if (lines [k].StartsWith ("author_contacts:", StringComparison.Ordinal))
          authorContactsIndex = k;
        if (lines [k].StartsWith ("sdk:", StringComparison.Ordinal))
          sdkIndex = k;
        if (lines [k].StartsWith ("languages:", StringComparison.Ordinal))
          languagesIndex = k;
        if (lines [k].StartsWith ("platforms:", StringComparison.Ordinal))
          platformsIndex = k;
        if (lines [k].StartsWith ("categories:", StringComparison.Ordinal))
          categoriesIndex = k;
        if (lines [k].StartsWith ("origin:", StringComparison.Ordinal))
          originIndex = k;
        if (lines [k].StartsWith ("order:", StringComparison.Ordinal))
          orderIndex = k;
        if (lines [k].StartsWith ("keywords:", StringComparison.Ordinal))
          keywordsIndex = k;
        if (lines [k].StartsWith ("layout:", StringComparison.Ordinal))
          layoutIndex = k;
        if (lines [k].StartsWith ("category_page:", StringComparison.Ordinal))
          categoryPageIndex = k;
        if (lines [k].StartsWith ("TODO:", StringComparison.Ordinal))
          TODOIndex = k;
      }

      // These are the default values that get set ("stubbed") if the field is NOT present...
      const string stubbedTitleField = "title: Title";
      const string stubbedDescriptionField = "description: unset";
      const string stubbedAuthorsField = "authors: unset";
      const string stubbedAuthorContactsField = "author_contacts: unset";
      const string stubbedSDKField = "sdk: unset";
      const string stubbedLanguagesField = "languages: unset";
      const string stubbedPlatformsField = "platforms: unset";
      const string stubbedCategoriesField = "categories: ['Unsorted']";
      const string stubbedOriginField = "origin: unset";
      const string stubbedOrderField = "order: 1";
      const string stubbedKeywordsField = "keywords: ['rhino', 'developer']";
      const string stubbedLayoutField = "layout: fullwidth-page";

      // create new contents with proper order
      var newLines = new List<string>();

      newLines.Add("---");

      // check to see if the file contains a title: field
      if (titleIndex != 0)
        newLines.Add (lines [titleIndex]);
      else
        newLines.Add (stubbedTitleField);

      // check to see if the file contains a description: field
      if (descriptionIndex != 0)
        newLines.Add (lines [descriptionIndex]);
      else
        newLines.Add (stubbedDescriptionField);

      // check to see if the file contains a authors: field
      if (authorsIndex != 0)
        newLines.Add (lines [authorsIndex]);
      else
        newLines.Add (stubbedAuthorsField);

      // check to see if the file contains a author_contacts: field
      if (authorContactsIndex != 0)
        newLines.Add (lines [authorContactsIndex]);
      else
        newLines.Add (stubbedAuthorContactsField);

      // check to see if the file contains a sdk: field
      if (sdkIndex != 0)
        newLines.Add (lines [sdkIndex]);
      else
        newLines.Add (stubbedSDKField);

      // check to see if the file contains a languages: field
      if (languagesIndex != 0)
        newLines.Add (lines [languagesIndex]);
      else
        newLines.Add (stubbedLanguagesField);

      // check to see if the file contains a platforms: field
      if (platformsIndex != 0)
        newLines.Add (lines [platformsIndex]);
      else
        newLines.Add (stubbedPlatformsField);

      // check to see if the file contains a categories: field
      if (categoriesIndex != 0)
        newLines.Add (lines [categoriesIndex]);
      else
        newLines.Add (stubbedCategoriesField);

      // check to see if the file contains a origin: field
      if (originIndex != 0)
        newLines.Add (lines [originIndex]);
      else
        newLines.Add (stubbedOriginField);

      // check to see if the file contains a order: field
      if (orderIndex != 0)
        newLines.Add (lines [orderIndex]);
      else
        newLines.Add (stubbedOrderField);

      // check to see if the file contains a keywords: field
      if (keywordsIndex != 0)
        newLines.Add (lines [keywordsIndex]);
      else
        newLines.Add (stubbedKeywordsField);

      // check to see if the file contains a layout: field
      if (layoutIndex != 0)
        newLines.Add (lines [layoutIndex]);
      else
        newLines.Add (stubbedLayoutField);

      // Don't add a category_page field if there isn't one already
      if (categoryPageIndex != 0)
        newLines.Add(lines[categoryPageIndex]);

      // Don't add a TODO field if there isn't one already
      if (TODOIndex != 0)
        newLines.Add (lines [TODOIndex]);

      newLines.Add("---");

      // Add the rest of the contents of the original file...
      for (int i = secondYamlSeparatorIndex+1; i < lines.Length; i++)
        newLines.Add (lines [i]);

      // Write it to disk...
      File.WriteAllLines (path, newLines);
    }
  }
}
