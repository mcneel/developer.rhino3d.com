---
title: Revoking authorization tokens
description: This guide discusses authorization token revocation within Rhino from Rhino Accounts.
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

[Once you have obtained an OAuth 2 Token]({{ site.baseurl }}/guides/rhinocommon/rhinoaccounts/ra-example), you can use it in any authentication workflow you wish. There may come a time, however, when the token is no longer needed. In such cases, it is highly recommended that your software has a way of revoking the OAuth 2 token. Revoking a token will generate a network request to the Rhino Accounts server which will invalidate the token so that it can no longer be used.

**Important Note**: 
`RevokeTokenAsync` must be executed inside a protected function that is passed to `ExecuteProtectedCodeAsync`. This is done to make sure that only a valid, signed assembly can retrieve auth tokens. Code inside the protected function should be kept as small as possible for performance and security reasons.

```cs
using Rhino.Runtime.RhinoAccounts;

...

await RhinoAccountsManager.ExecuteProtectedCodeAsync(async (SecretKey secretKey) =>
{
	await RhinoAccountsManager.RevokeAuthTokenAsync(oauth2Token, secretKey, CancellationToken.None);			
});
```
