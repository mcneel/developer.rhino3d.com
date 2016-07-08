---
title: Localizing Plugin Toolbars
description: This guide covers the localization of plugin toolbars.
author: dale@mcneel.com
apis: ['RhinoCommon', 'C/C++']
languages: ['C#', 'C/C++']
platforms: ['Windows']
categories: ['Advanced']
order: 1
keywords: ['RhinoCommon', 'C/C++', 'Rhino', 'Toolbar', 'Plugin']
layout: toc-guide-page
TODO: 'xml code block formatting needs attention'
---

# {{ page.title }}

{{ page.description }}

## Question

What is the best way to prepare a Rhino toolbar for multi-language support?

## Answer

If you want to create Rhino-style toolbars, then use Rhino's **Toolbar** command. You can save your custom toolbars in your own Rhino User Interface (RUI) file. For details on creating toolbars, see the Rhino help file.

An RUI file is an XML file that can be viewed and edited in an ordinary text editor.

If you open an RUI file, that contains a toolbar that contains a button, you might see a block of XML that looks similar to the following:

```xml
<macro_item guid="some_unique_guid" bitmap_id="some_unique_guid">
  <text>
    <locale_1033>RenderSettings</locale_1033>
  </text>
  <tooltip>
    <locale_1033>Render settings</locale_1033>
  </tooltip>
  <button_text>
    <locale_1033>Render</locale_1033>
  </button_text>
  <script>_DocumentPropertiesPage _Render</script>
</macro_item>
```

Notice the ```<locale_1033>``` tag, which denotes the text used by Rhino when configured for English (United States).

It is possible to add additional locale tags for supported language.

```xml
<macro_item guid="some_unique_guid" bitmap_id="some_unique_guid">
  <text>
    <locale_1033>RenderSettings</locale_1033>
    <locale_1031>Rendereinstellungen</locale_1031>
    <locale_1034>RenderizadoOpciones</locale_1034>
    <locale_1036>ParamètresRendu</locale_1036>
    <locale_1040>RenderingImpostazioni</locale_1040>
    <locale_1042>렌더링_설정</locale_1042>
    <locale_2052>渲染设置</locale_2052>
    <locale_1028>彩現設定</locale_1028>
  </text>
  <tooltip>
    <locale_1033>Render settings</locale_1033>
    <locale_1031>Rendereinstellungen</locale_1031>
    <locale_1034>Opciones de renderizado</locale_1034>
    <locale_1036>Paramètres du rendu</locale_1036>
    <locale_1040>Impostazioni rendering</locale_1040>
    <locale_1041>ﾚﾝﾀﾞﾘﾝｸﾞ設定</locale_1041>
    <locale_1042>렌더링 설정</locale_1042>
    <locale_2052>渲染设置</locale_2052>
    <locale_1028>彩現設定</locale_1028>
  </tooltip>
  <button_text>
    <locale_1033>Render</locale_1033>
    <locale_1031>Rendern</locale_1031>
    <locale_1034>Renderizar</locale_1034>
    <locale_1036>Rendu</locale_1036>
    <locale_1040>Rendering</locale_1040>
    <locale_1041>ﾚﾝﾀﾞﾘﾝｸﾞ</locale_1041>
    <locale_1042>렌더링</locale_1042>
    <locale_2052>渲染</locale_2052>
    <locale_1028>彩現</locale_1028>
  </button_text>
  <script>_DocumentPropertiesPage _Render</script>
</macro_item>
```

Note, it is not possible to localize toolbar bitmaps.
