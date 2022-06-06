+++
aliases = ["/5/guides/rhinocommon/cloudzoo/cloudzoo-modify-plugin-licensing-code/", "/6/guides/rhinocommon/cloudzoo/cloudzoo-modify-plugin-licensing-code/", "/7/guides/rhinocommon/cloudzoo/cloudzoo-modify-plugin-licensing-code/", "/wip/guides/rhinocommon/cloudzoo/cloudzoo-modify-plugin-licensing-code/"]
authors = [ "aj" ]
categories = [ "CloudZoo" ]
description = "This guide discusses all the steps needed to have a Plug-In support Cloud Zoo."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Modify Plug-In licensing code to support Cloud Zoo"
type = "guides"
weight = 5
override_last_modified = "2019-06-25T11:12:09Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Important Information

Supporting Cloud Zoo within your plugin's code is easy, but it is important to understand that Cloud Zoo licensing behaves differently from other licensing methods in Rhino. With Cloud Zoo, your plugin (and Rhino itself) will _not_ receive a license key entered by the user or a local Zoo server, but rather a cryptographically verified token called a _License Lease_. The License Lease is authored by Cloud Zoo and handed to Rhino when a license for your plugin is first requested, and at regular intervals thereafter. A License Lease expires every few weeks, so Rhino will automatically negotiate a new lease with Cloud Zoo and hand it to your plugin so that the lease is always a few weeks from expiring.

In addition, note that expiration is not the only way a license lease can voided. Rhino can inform your plugin that a lease has been voided for a variety of reasons (For example, the license was removed from Cloud Zoo by the user or the user starting Rhino on a different computer). 

## Required Steps

To support Cloud Zoo in your plugin, the following must be done in your plugin's code:

1. Implement `OnLeaseChangedDelegate` method.
2. Call `GetLicense` within your plugin.
3. [Digitally sign your plugin](/guides/rhinocommon/digitally-signing-plugins-for-zoo).


## Implement OnLeaseChangedDelegate

This method is called by Rhino after a license lease changes. This can happen in the following situations:
- A license lease is successfully negotiated after you call `GetLicense`.
- A new license lease is negotiated automatically by Rhino to keep it from expiring.
- The current license lease expires (The lease received is null).
- The current license lease is voided by Cloud Zoo (The lease received is null).

When `LicenseLeaseChangedEventArgs.Lease` is null, you should assume the user does not have a valid license and disable functionality accordingly.

### Example:

```c#
	/// <summary>
	/// Called by Rhino to signal that a lease from Cloud Zoo has changed. 
	/// If LicenseLeaseChangedEventArgs.Lease is null, then the server has signaled
	/// that this product is no longer licensed. Your plug-in must change behavior 
	/// to behave appropriately.
	/// </summary>
	/// <param name="args">Data passed by Rhino when the lease changes</param>
	/// <param name="icon">Icon to be displayed in Tools > Options > Licenses for this lease.</param>
	private static void OnLeaseChanged(LicenseLeaseChangedEventArgs args, out System.Drawing.Icon icon)
	{
	  icon = ProductIcon;
	
	  // This sample does not support Rhino accounts.
	
	  if (null == args.Lease)
	  {
	    // Lease has been voided; this product should behave as if it has no
	    // license. It is up to the plug-in to determine what that looks like.
	  }
	
	  // Verify that args.Lease.ProductId is correct
	  // Verify that args.Lease.ProductEdition is correct
	  // Verify that args.Lease.ProductVersion is correct
	  // Verify thatargs.Lease.IsExpired() is false
	}
```

[See an example in GitHub](https://github.com/mcneel/rhino-developer-samples/blob/e24bb79e8e3954952826111185db4ce7f96ecd65/rhinocommon/cs/SampleCsWithLicense/SampleCsWithLicensePlugIn.cs#L166)


## Call GetLicense

Like other licensing methods, you should call `GetLicense` when your plugin is loaded. The only difference is that you must pass the `OnLeaseChanged` delegate you implemented in the previous step and add `SupportsRhinoAccounts` to the `LicenseCapabilities` argument so that Rhino can know that you support Cloud Zoo and so that Rhino can know which delegate to call when a license lease change occurs.