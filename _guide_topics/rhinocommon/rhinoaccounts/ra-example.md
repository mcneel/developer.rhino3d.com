---
title: Retrieving authentication and authorization tokens
description: This guide gives an example of how to obtain authentication and authorization tokens within Rhino from Rhino Accounts.
authors: ['aj']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['RhinoAccounts']
origin: unset
order: 1
keywords: ['Plugin', 'Rhino Accounts']
layout: toc-guide-page
---

To retrieve an OAuth 2 Token for authorization or an OpenID Connect token to learn about the user's identity, all that is needed is to call one of the different overloads of `GetAuthTokensAsync`. This method will asynchronously ask the user for permission to obtain the tokens, and return them to you so that you can use them as you wish.

By default, a successful call to `GetAuthTokensAsync` will cache the tokens you retrieved in a secure persistent store so that they can later be retrieved using `TryGetAuthTokens` without having to ask the user for permission or wait for potentially lengthy network requests. In most scenarious, it makes sense to call `TryGetAuthTokens` first to see if there are any cached tokens available. If there aren't, you can then call `GetAuthTokensAsync` and ask the user for permission.

**Important Note**: 
Both `GetAuthTokensAsync` and `TryGetAuthTokens` must be executed inside a protected function that is passed to `ExecuteProtectedCodeAsync`. This is done to make sure that only a valid, signed assembly can retrieve auth tokens. Code inside the protected function should be kept as small as possible for performance and security reasons.

Example:

```cs
using McNeel.RhinoAccounts;

...

Tuple<OpenIDConnectToken, OAuth2Token> authTokens = null;

await RhinoAccountsManager.ExecuteProtectedCodeAsync(async (RhinoAccountsManager.SecretKey secretKey) =>
{
	authTokens = RhinoAccountsManager.TryGetAuthTokens("MY_PLUGIN_ID",secretKey);
	
	if (authTokens == null)	
	{
		authTokens = await RhinoAccountsManager.GetAuthTokensAsync(
		    "MY_PLUGIN_ID",
		    "MY_PLUGIN_SECRET",
		    secretKey,
		    CancellationToken.None
		);
	}
}); 
```


For details on all the available options you can specify on the methods described above such as `scope` and `maxage`, please see the [Rhino Accounts Reference](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig).