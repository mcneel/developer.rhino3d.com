---
title: RDK Document Contents
description: This document describes how to use the RDK document contents class in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin', 'Contents']
layout: toc-guide-page
---
The _RDK Document Contents_ is a document-resident object that allows certain operations on document contents. It is particularly useful for attaching contents to a document and finding contents by their instance ids. If you have a Rhino document, you can read and modify that document's contents through the document's [IRhRdkContents]({{ site.baseurl }}/api/cpp/class_i_rh_rdk_contents.html) interface. Any changes you make will appear in the relevant editor and will also be stored in the 3dm file. Getting the contents from a document always returns a const reference. To write to the contents, you must begin a batch of write operations and afterwards end the batch. This is done using the RDK's standard BeginChange / EndChange system. The following is an example of how to access the document contents:
```cpp
static class CTestContents : public CRhinoTestCommand
{
protected:
	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"ContentsExample"); }
	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
}
theContentsExampleCommand;

CRhinoCommand::result CTestContents::RunCommand(const CRhinoCommandContext& context)
{
	auto* pDoc = context.Document();
	if (nullptr == pDoc)
		return failure;

	const auto& contents = pDoc->Contents();

	// Create a new basic material.
	ON_Material mat;
	auto* pMaterial = ::RhRdkNewBasicMaterial(mat, pDoc);
	if (nullptr == pMaterial)
		return failure;

	// Attach it to the document.
	auto& write_contents = contents.BeginChange(RhRdkChangeContext::Program);
	write_contents.Attach(*pMaterial);
	write_contents.EndChange();

	// Find the material in the document.
	const auto* pFound = contents.Find(pMaterial->InstanceId());

	ASSERT((nullptr != pFound) && (pFound->InstanceId() == pMaterial->InstanceId()));

	return success;
}
```
