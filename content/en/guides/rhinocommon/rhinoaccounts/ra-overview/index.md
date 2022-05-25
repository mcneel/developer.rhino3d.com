+++
authors = [ "aj" ]
categories = [ "RhinoAccounts", "Advanced" ]
description = "This guide discusses all the steps needed to interact with Rhino Accounts within Rhino."
keywords = [ "Plugin", "Rhino Accounts" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Interacting with Rhino Accounts"
type = "guides"
weight = 15

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


## Overview

Rhino Accounts is an authentication and authorization system built and supported by Robert McNeel & Associates. It is built on top of the [OpenID Connect protocol](https://openid.net/connect/). 

As a brief summary, the authentication services of Rhino Accounts enables you, the developer, to verify an individual's identity and access (with the user's permission) account information such as their name, email addresses, profile picture, and more. This allows you to tailor your experience for the user or learn more about who is using your product.

The authorization services are based on OAuth 2 Tokens. A token allows you to access any services that use Rhino Accounts for authorization, including your own. For example, your web server might accept certain files to be uploaded and downloaded from your plugin that sync accross different machines. An authorization token can be obtained by your plugin and can be presented to your web server when uploading or downloading files. The web server can check with Rhino Accounts that the token is valid and the individual it belongs to.

For a more thourough overview of Rhino Accounts, please see the [Rhino Accounts Reference](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig).

OpenID Connect is built on top of HTTP. Since Rhino Accounts is an OpenID Connect provider, you can interact with Rhino Accounts using any HTTP client from .NET, JavaScript, Python, etc. However, making raw HTTP calls to Rhino Accounts can be tedious. Handling all the possible outcomes can be time consuming, and future-proofing your code in case the HTTP endpoints change can be frustrating. More importantly, taking into account all the possible security considerations to avoid leaking sensisive user data requires a rigorous review of your code. For all these reasons, we _strongly_ recommend that you use Rhino's built in capabilities to interact with Rhino Accounts described in this guide. It will also greatly simplify your development and make things easier down the road.

Taking advantage of Rhino Accounts within Rhino is simple, and requires the following steps to be implemented.

## Required Steps

To take Advantage of Rhino Accounts within Rhino:
 1. [Contact us](mailto:will@mcneel.com) to obtain a unique client id and secret for Rhino Accounts. This will represent your service within the system.
 2. [Call `GetTokensAsync` or `TryGetAuthTokens` to retrieve authentication and authorization tokens](/guides/rhinocommon/rhinoaccounts/ra-example).
 3. (*Optional*) [Call `RevokeAuthTokenAsync` to invalidate an authorization token when you no longer need it.](/guides/rhinocommon/rhinoaccounts/ra-revoke).

