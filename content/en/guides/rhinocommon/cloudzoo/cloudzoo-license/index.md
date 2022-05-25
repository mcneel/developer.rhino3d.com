+++
authors = [ "aj" ]
categories = [ "CloudZooDoc" ]
description = "A License is a JSON object that represents a license for a software product issued by a registered issuer in Cloud Zoo."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "Cloud Zoo License Object"
type = "guides"
weight = 1

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

```json
{
	"id": "6-32403404-3434340-343432",
	"key": "RH60-ABCD-EFGZ-HIJK-LMNO",
	"aud": "4ed9ebbe-c43e-4d4a-9642-e555d727df9f",
	"iss": "mcneel",
	"exp": null,
	"numberOfSeats": 1,
	"editions": {
			"en": "Commercial",
			"es": "Comercial"
	},
	"metadata": OPTIONAL JSON OBJECT SMALLER THAN 10K
}
```

## Description

-   `id` - A string that uniquely describes each license. This string must be unique for all licenses of the same product type. It is also known as the license's serial number.
-   `key` - A string that uniquely describes each license. This string must be unique for all licenses of the same product type. Normally, this string is used to add a license to Cloud Zoo by users.
-   `aud` - A GUID denoting the product id of the plugin. This is how Cloud Zoo knows that this license can be used for your product.
-  ` iss` - The id of the issuer as registered with Cloud Zoo.
-   `exp` - The expiration date of the license, expressed in a JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds. For example, for midnight on March 31, 2019, the value would be `1553990400`. Cloud Zoo will not honor the license as valid for issuing leases after the expiration date has passed. If null, the license is considered perpetual (i.e. never expires).
-   `numberOfSeats` - Denotes how many seats can be concurrently issued, barring any advanced heuristics, for the license. This number must be at least 1. For example, a lab license with a value of `30` would allow 30 team members to use your software concurrently. 
-   `editions` - A dictionary of localized product editions. Each key represents an ISO 639-1 language code. You may specify a two letter country code after the language with a dash or an underscore (i.e. such as `zh-tw`, case insensitive). If that exact language id is not available for a particular task in the system, the system will attempt to use a more generic language id (i.e. for example, if `es-CO` is not available, then the system will try to use `es`). If the region agnostic language id is also not available, en (English) will be used. At least one key-value pair must be present, preferably in English.
-   `metadata` - Any arbitrary data that is to be stored with the license. The issuer will receive this data back on other callbacks, so the issuer can use this field to save state or other arbitrary information. The raw json data must be less than 10KB. This field is optional.


