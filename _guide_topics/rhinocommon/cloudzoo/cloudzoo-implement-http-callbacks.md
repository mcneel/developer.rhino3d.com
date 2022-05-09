---
title: Implement HTTPS Callbacks
description: This guide explains all the HTTPS callbacks that need to be implemented by an issuer of Cloud Zoo.
authors: ['aj']
sdk: ['RhinoCommon']
languages: unset
platforms: ['Windows', 'Mac']
categories: ['CloudZoo']
origin: unset
order: 4
keywords: ['Plugin', 'Cloud Zoo']
layout: toc-guide-page
---

As an issuer, you must implement four HTTPS endpoints to answer basic questions Cloud Zoo requires to function. We provide a [ready-to-deploy solution in our Github repository](https://github.com/mcneel/cloudzoo-issuer) you can use as a template to implement these callbacks, or if you're experienced with HTTP rest APIs, you can roll your own from scratch. Regardless of the path you choose, the issuer must answer the following questions:

-   Can a license be added to an entity? The issuer is asked this question when a user tries to add a license to their account or a team. You may request further information from the user, accept the request, or deny the request.
-   Can a license be removed from an entity? The issuer is asked this question when a user tries to remove a license from their account or a team.
-   What are the details of a specific license key? This is used to display the license information to the user.

For each of these questions, you MUST implement the following 3 callbacks:

 1. GET `/get_license`
 2. POST `/add_license`
 3. POST `/remove_license`

Note that all the callbacks listed above follow the conventions listed below.

## Callback Conventions

Unless noted, the following conventions apply to *all* callbacks implemented by an issuer.

### Callback URL

Cloud Zoo will perform a request to the base URL provided when creating an issuer plus the path (i.e. `/add_license`) and method (i.e. `GET` or `POST`). For example, if your issuer's base URL is `https://mydomain.com/cloudzoo`, then the full callback URL for `/add_license` would be `POST https://mydomain.com/cloudzoo/add_license` 

### JSON

All payload to and from callbacks happens in [JSON format](https://www.json.org). To make this explicit, every request to a callback will have the  header `Content-Type: application/json` present in the HTTPS request.

### Localization

In some circumstances, such as when additional input is required from a user when adding a license to an account, a localized response SHOULD be returned by the issuer in the user's locale. To make this possible, every request to a callback will have an `Accept-Language` header present like so:

```
Accept-Language: fr-CH; fr;q=0.9, en;q=0.8, *;q=0.5
```

The header encodes the languages preferred by the user currently interacting with Cloud Zoo. If none of the languages specified in the header are available, English SHOULD be used.

### Authentication

All endpoints in Cloud Zoo or on the issuer use [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) using the issuer’s id and the corresponding secret shared between Cloud Zoo and the respective issuer. You MUST make sure that the secret matches verbatim before processing any callback request on any endpoint to prevent a security breach. For example, on the issuer's end:
	
```python 
from flask import request, Response
	
ISSUER_ID = "issuer_1"
ISSUER_SECRET = "my_secret"

def check_auth(username, password):
    """This function is called to check if a username password combination is valid."""
    return username == ISSUER_ID and password == ISSUER_SECRET

@app.route("/add_license", methods=["POST"])  
def add_license()
	"""See if a license can be added to an entity or whether we should ask more information, 
	or whether we should deny the request."""
	auth = request.authorization
    
	if not auth or not check_auth(auth.username, auth.password):
		return Response(
			'Could not verify your access level for that URL.\n',
			'You have to authenticate with proper credentials', 401,
			{'WWW-Authenticate': 'Basic realm="Credentials Required"'}
		)
	else:
    	pass #Continue processing the request HERE
```
		
### Non-successful responses

If returning a response with an HTTP status code greater or equal to `400`, the issuer SHOULD include the following JSON in the payload as well:

```
{
	"description": "The license cannot be removed from Cloud Zoo because [Marley](https://example.com) says so.",
	"details": "request id 239231203123212"
}
```

 - The `description` field is user facing, and SHOULD be localized.  In addition, the description string may have markdown style links as in the example above. The links can be used to help the user navigate and solve the issue.
 - The `details` field is not user-facing, but may be logged for troubleshooting purposes. You MUST NOT include sensitive data in the details string.

## Callbacks

### GET /get_license

Return information about a specific license so users can see details about the license.

#### Example Request

```
GET /get_license?aud=PRODUCT_ID&key=A_LICENSE_KEY
```

 - `aud`: The product id of the license whose information is to be returned.
 - `key`:  The license key of the license whose information is to be returned.

#### Required Response
The response will vary depending on the issuer’s decision as described below:

A successful response:

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: A [License object]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-license). [See an actual example in our GitHub example](https://github.com/mcneel/cloudzoo-issuer/blob/67d66da0b062ca0f24baa7f04055b8b3841c2de1/app.py#L247)

A non-successful (error) response:

- HTTP Status Code: A code greater or equal to `400 (Bad Request)` 
- Response Payload: [A non-successful response](#non-successful-responses)
 
### POST /add_license

See if a license can be added to an entity or whether an issuer should ask more information, or whether we should  
deny the request. This callback is invoked whenever a license is about to be added to an entity.

#### Example Request

```
POST /add_license
{
	"entityId": "9304194021213-|-Group",
	"entityType": "Group",
	"license": {
			"key": "RH50-ABCD-EFGZ-HIJK-LMNO",
			"aud": "PRODUCT-ID-HERE"
		},
	"userInfo": {
		"sub": "43190412048124",
		"email": "marley_the_dog@mcneel.com",
		"com.rhino3d.accounts.emails": [
			"marley_the_dog@mcneel.com",
			"marleyz121@gmail.com"
		],
		"com.rhino3d.accounts.member_groups": [
			{
				"id": "9304194021213",
				"name": "Marley’s Friends LLC"
			}
		],
		"com.rhino3d.accounts.admin_groups": [],
		"com.rhino3d.accounts.owner_groups": [],
		"name": "Marley",
		"locale": "en-gb",
		"picture": "http://marley.the.dog.com/images/coolpic.png"
		},    
	"precondition": "RH40-ABCD-EFGZ-HIJK-LMNO"
}
```

-   `entityId`: The id of the entity whom the license will be added to. Entities can be individual users or groups as defined in Rhino Accounts.
-  `userInfo`: The decoded JWT representing the user’s OpenID Token who wants to add the license to the specified entity. See [Rhino Accounts OpenID Tokens](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig/edit#heading=h.qctsih4c0ctd) for details. The user is always a privileged member of the entity or is the entity itself in case `entityType` is `User`. Additional fields could be present and MAY be used but SHOULD NOT be assumed to be present.
-   `license`: The license that is to be added. This field is a simplified [License object]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-license) with the license key and product id of the license.
- `precondition`: This field is optional. If provided, it is a string string containing a precondition that was requested by the issuer (see response details below for more details on this field).

#### Required Response
The response will vary depending on the issuer’s decision as described below:

If the license *can* be added to an entity:
 - HTTP Status Code: `200 (OK)` 
 - Response Payload: A [License Cluster object]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-licensecluster) representing the license(s) to be added. See an actual example in our GitHub example [See an actual example in our GitHub example](https://github.com/mcneel/cloudzoo-issuer/blob/67d66da0b062ca0f24baa7f04055b8b3841c2de1/app.py#L124)

If more information (`precondition`) is required: 
- HTTP Status Code: `428 (Precondition Required)`
- Response Payload: [A non-successful response](#non-successful-responses). The `description` field will be used to describe what input is required from the user, such as a previous license key or a secret code. [See an actual example]((https://github.com/mcneel/cloudzoo-issuer/blob/67d66da0b062ca0f24baa7f04055b8b3841c2de1/app.py#L124).

If the additional information (`precondition`) is incorrect:
- HTTP Status Code: `412 (Precondition Failed)`
- Response Payload: [A non-successful response](#non-successful-responses). [See an actual example]((https://github.com/mcneel/cloudzoo-issuer/blob/67d66da0b062ca0f24baa7f04055b8b3841c2de1/app.py#L124).

If the license *cannot* be added to an entity:
- HTTP Status Code: `409 (Conflict)`
- Response Payload: [A non-successful response](#non-successful-responses). [See an actual example]((https://github.com/mcneel/cloudzoo-issuer/blob/67d66da0b062ca0f24baa7f04055b8b3841c2de1/app.py#L124).

#### Remarks

This callback MUST be idempotent, meaning that it MUST consistently return the same result given a set of arguments. This is because the callback may be called more than one time with the same arguments by the system as part of a transaction that could be retried.

### POST /remove_license

See if a license can be removed from an entity. This callback is invoked right before a license is removed from an entity. Issuers SHOULD make sure to note that a license is no longer in the entity. 

#### Example Request

```
POST /remove_license
{
	"entityId": "9304194021213-|-Group",
	"entityType": "Group",
	"userInfo": {
			"sub": "43190412048124",
			"email": "marley_the_dog@mcneel.com",
			"name": "Marley",
			"locale": "en-gb",
			"picture":"http://marley.the.dog.com/images/coolpic.png"
		}
	"licenseCluster": {
		"licenses":[ ONE OR MORE LICENSE OBJECTS ... ]
	}
}
```

 - `entityId`: The id of the entity whom the license will be removed from. Entities can be individual users or groups as defined in [Rhino Accounts](https://accounts.rhino3d.com/help).
 - `entityType`:  Entities can be individual users (`User`) or groups (`Group`) as defined in [Rhino Accounts](https://accounts.rhino3d.com/help).
 - `userInfo`: The decoded JWT representing the user’s OpenID Token who wants to add the license to the specified entity. See [Rhino Accounts OpenID Tokens](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig/edit#heading=h.qctsih4c0ctd) for details. The user is always a privileged member of the entity or is the entity itself in case `entityType` is `User`. Additional fields could be present and MAY be used but SHOULD NOT be assumed to be present.
 - `licenseCluster`: The [License Cluster object]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-licensecluster) to be removed.

#### Required Response
The response will vary depending on the issuer’s decision as described below:

A successful response (The license can be removed):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: Empty. [See an actual example in our GitHub example](https://github.com/mcneel/cloudzoo-issuer/blob/67d66da0b062ca0f24baa7f04055b8b3841c2de1/app.py#L211)

A non-successful (error) response (The license cannot be removed):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: [A non-successful response](#non-successful-responses)

#### Remarks

This callback MUST be idempotent, meaning that it MUST consistently return the same result given a set of arguments. This is because the callback may be called more than one time with the same arguments by the system as part of a transaction that could be retried.
