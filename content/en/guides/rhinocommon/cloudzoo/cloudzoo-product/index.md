+++
aliases = ["/5/guides/rhinocommon/cloudzoo/cloudzoo-product/", "/6/guides/rhinocommon/cloudzoo/cloudzoo-product/", "/7/guides/rhinocommon/cloudzoo/cloudzoo-product/", "/wip/guides/rhinocommon/cloudzoo/cloudzoo-product/"]
authors = [ "aj" ]
categories = [ "CloudZooDoc" ]
description = "A Product is a JSON object that represents a a product for a specific issuer in Cloud Zoo. A product's id should be correlated with your Plug-In's id. All licenses in the system are related to a specific product."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "Cloud Zoo Product Object"
type = "guides"
weight = 1
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

## Structure

    {
        "id": "06eb1079-5a56-47a1-aw6d-0b4518fd894b",
	    "creationDate": 1559928168,
	    "iss": "mcneel",
	    "format": {
	        "length": {
	            "min": 24,
	            "max": 24
	        },
	        "prefix": "RMA7-",
	        "example": "RMA7-XXXX-XXXX-XXXX-XXXX-XXXX",
	        "regexFilter": "[A-Za-z0-9]"
	    },
	    "version": "6",
	    "platforms": [
	        "Windows"
	    ],
	    "picture": "https://elisapi.mcneel.com/media/2",
	    "downloadUrl": "https://www.rhino3d.com/download/rhino-for-mac/6/wip",
	    "titles": {
	        "en": "Rhino WIP"
	    },
	}

## Description

-   `id` (_readonly_) - A GUID that uniquely describes each product. This GUI must be unique in the entire system.
-   `creationDate` (_readonly_) - A unix timestamp in seconds representing the date the product was added to Cloud Zoo. 
-  ` iss` (_readonly_) - The id of the issuer as registered with Cloud Zoo.
-   `format` - A [License Format object](/guides/rhinocommon/cloudzoo/cloudzoo-licenseformat). Cloud Zoo will send all requests to add a license to the system to the issuer of the product whose license format matches the given license key.
-   `version` - The version of the product that this license represents. This string is user facing and will be used in Rhino as well as in the Licenses Portal.
- `platforms` - An array of supported platforms for this license. Currently, only `Windows` and `Mac` are supported.
- `picture`  - A url where an icon for this product may be found. The icon must not be larger than 1MP.
- `downloadUrl`  - A url where the actual software the product represents may be downloaded. This link will be publicly available to users.
-   `titles` - A dictionary of localized product names. Each key represents an ISO 639-1 language code. You may specify a two letter country code after the language with a dash or an underscore (i.e. such as `zh-tw`, case insensitive). If that exact language id is not available for a particular task in the system, the system will attempt to use a more generic language id (i.e. for example, if `es-CO` is not available, then the system will try to use `es`). If the region agnostic language id is also not available, en (English) will be used. At least one key-value pair must be present, preferably in English.





	