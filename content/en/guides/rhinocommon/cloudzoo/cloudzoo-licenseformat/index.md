+++
aliases = ["/en/en/5/guides/rhinocommon/cloudzoo/cloudzoo-licenseformat/", "/en/6/guides/rhinocommon/cloudzoo/cloudzoo-licenseformat/", "/en/7/guides/rhinocommon/cloudzoo/cloudzoo-licenseformat/", "/wip/guides/rhinocommon/cloudzoo/cloudzoo-licenseformat/"]
authors = [ "aj" ]
categories = [ "CloudZooDoc" ]
description = "A License Format object defines a pattern for a license key. When a user enters a license key to be added to their account or their team, Cloud Zoo will find a product with a matching license format and notify its issuer about the user's intent to add the license."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "License Format Object"
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

**Note:** Not all format possibilities are described in this document. If your license keys have a format that cannot be accurately defined in the fields below, we might be able to help. Please contact aj@mcneel.com for details.

## Structure

    "format": {
        "length": {
            "min": 24,
            "max": 48
        },
        "prefix": "RMA7-",
        "example": "RMA7-XXXX-XXXX-XXXX-XXXX-XXXX",
        "regexFilter": "[A-Za-z0-9]"
    },

## Description

-   `length` - A range of `min` and `max` integers representing the minimum and maximum characters--inclusive--a license key is expected to contain. To avoid conflicts with other formats, this number should be as specific as possible.
-   `prefix` - A string representing the common prefix a license key is expected to begin with. The prefix should be as specific as possible to avoid conflicts with other formats.
-  ` example` - An example license key that may be shown to the user when entering a license. It should begin with the `prefix` specified.
-   `regexFilter`- (_optional_) - A regular expression defining the allowed characters in the license key. By default, only characters A-Z (both lowercase and uppercase) and numbers 0-9 are allowed. Whitespace, dashes, and slashes will not be considered for a pattern match.




