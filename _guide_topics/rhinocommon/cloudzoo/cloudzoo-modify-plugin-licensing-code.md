---
title: Creating Plugins that use Cloud Zoo
description: This guide discusses all the steps needed to create RhinoCommon plugins that support Cloud Zoo.
authors: ['aj']
sdk: ['RhinoCommon']
languages: unset
platforms: ['Windows', 'Mac']
categories: ['Zoo']
origin: unset
order: 1
keywords: ['Zoo', 'Plugin', 'CloudZoo']
layout: toc-guide-page
---


## Overview

Add Cloud Zoo support to your Plug-In by following the steps below. Cloud Zoo allows Rhino users to add their license keys to their personal Rhino account or to a team composed of multiple Rhino accounts. The users may then login from any computer that has Rhino installed and run Rhino. Cloud Zoo enforces license restrictions by making sure that users can only run concurrently in as many computers as there are licenses for a specific product. This allows individual users to run Rhino and other Plug-Ins on any machine. In a team scenario, members can be anywhere in the world and have access to a license. 

Cloud Zoo does not require users to have a constant internet connection—only an occasional one every couple of weeks. This is possible because Cloud Zoo employs license lease mechanism wherein a lease--not a license itself--is issued by Cloud Zoo to a client running Rhino. A lease usually expires within a few weeks, but a new lease is frequently issued between Rhino and Cloud Zoo while a client is online. This allows for a buffer of a few weeks in case the computer is offline for extended periods of time. This design allows Rhino and other Plug-Ins to run reliably even in environments with poor internet connections. Cloud Zoo can also void a lease at any point in time. For example, when a license is removed by a user or by the developer (Such as when a customer returns a license for a refund), Cloud Zoo immediately voids all related leases, effectively ending the user's ability to use the software the license is intended for.

Under certain scenarios, such as when adding or removing a license, Cloud Zoo will contact your server to make sure you allow such operations to succeed. Your server is not required to interact with the license lease process.

AJ TODO INSERT IMAGE HERE!!!

## Required Steps

To have your Plug-In support Cloud Zoo, you must:
 1. Register as an Issuer in Cloud Zoo.
 2. Implement the required HTTPS callbacks.
 3. Add products to Cloud Zoo.
 4. Modify Plug-In licensing code to support Cloud Zoo.
 5. (*Optional*) Take advantage of Cloud Zoo endpoints for querying and modifying licenses in Cloud Zoo.

## Register as an Issuer in Cloud Zoo

In Cloud Zoo, an _issuer_ represents a vendor of products with license keys. If you want your plugin to use Cloud Zoo, you must register to be an issuer by emailing [aj@mcneel.com](mailto:aj@mcneel.com). You will be provided with an issuer id and a secret that will uniquely identify you as a product vendor and will allow you to implement the required HTTPS callbacks.

## Add products to Cloud Zoo

Once you are registered as an issuer, you can add, view, and modify products in Cloud Zoo using the endpoints described below. 

### Endpoint Conventions

Unless noted, the following conventions apply to *all* product endpoints available to registered issuers in Cloud Zoo.

#### Endpoint Location
All requests should be made to the following location: `https://cloudzoo.rhino3d.com/v1`.

#### JSON

All payload to and from endpoints happens in [JSON format](https://www.json.org). To make this explicit, every response to an endpoint will have the  header `Content-Type: application/json` present in the HTTPS response.

#### Authentication

All endpoints in Cloud Zoo or on the issuer use [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). To receive a successful response from an endpoint, you must include an `Authorization` header like so:

    Authorization: Basic BASE64ENCODEDSTRING
Where `BASE64ENCODEDSTRING` is a base64 (AJ TODO LINK!!!) encoded string containing your issuer id and your issuer secret:

    BASE64ENCODEDSTRING = b64.encode(issuer_id + ":" + issuer_secret)
	
#### Non-successful responses

All unsuccessful responses from endpoints will have an HTTP status code greater or equal to `400`. If the status code is also less than `500`, the payload will include the following JSON:

    {
	    "Error": "SomeErrorCode"
		"Description": "A description about the error message",
		"Details": "More details about the error"
	}

 - The `Error` field contains a specific error code that can be used by the issuer to recognize a specific error, such as incorrect credentials. 
 - The `Description` field contains a description of the error.
 - The `Details` field contains details of the error, possibly suggesting how to fix it.

If the status code is greater or equal to `500`, the response may not be JSON and may be empty.

### Endpoints

#### POST `/product`

Adds a product to Cloud Zoo registered under the authenticating issuer.

##### Example Request

    POST /product
	
	{
	    "id": "06bb1e79-5456-47a1-ad6d-104518cd894b",
	    "version": "12",
	    "platforms": [
	        "Windows"
	    ],
	    "picture": "https://elisapi.mcneel.com/media/2",
	    "downloadUrl": 	"https://www.rhino3d.com/download/new_product",
	    "titles": {
	        "en": "New Product Name",
	        "es": "Nuevo Producto",
	        "ja": "新製品"
	    },
	    "format": {
			"example": "MA7B-XXXX-XXXX-XXXX-XXXX-XXXX",
			"prefix": "MA7B",
			"length": {"min": 24, "max": 24}
		}
	}

The payload should be a Product object [AJ TODO LINK].

##### Response

A successful response (The product was created):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: The newly created Product object [AJ TODO LINK]. 

A non-successful (error) response (The product could not be created):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: A non-successful response (AJ TODO LINK!!!)

#### PUT `/product/{product_id}`

Modifies an existing product with the given `product_id`. Note that some properties of a product cannot be modified after creation, including but not limited to its unique id.

##### Example Request

    PUT /product/06bb1e79-5456-47a1-ad6d-104518cd894b
	
	{
	    "platforms": [
	        "Windows", "Mac"
	    ],
	    "picture": "https://elisapi.mcneel.com/media/new_icon_url"
	}

##### Response

A successful response (The product was modified):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: The newly updated Product object [AJ TODO LINK]. 

A non-successful (error) response (The product could not be modified):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: A non-successful response (AJ TODO LINK!!!)

#### GET `/product/{product_id}`

Gets an existing product with the given `product_id`.

##### Example Request

    GET /product/06bb1e79-5456-47a1-ad6d-104518cd894b

##### Response

A successful response:

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: A Product object [AJ TODO LINK]. 

A non-successful (error) response:

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: A non-successful response (AJ TODO LINK!!!)

## Implement HTTPS callbacks

As an issuer, you must implement four HTTPS endpoints to answer basic questions Cloud Zoo requires to function. We provide a ready-to-deploy solution [AJ TODO LINK!!!] in our Github repository you can use as a template to implement these callbacks, or if you're experienced with HTTP rest APIs, you can roll your own from scratch. Regardless of the path you choose, the issuer must answer the following questions:

-   Can a license be added to an entity? The issuer is asked this question when a user tries to add a license to their account or a team. You may request further information from the user, accept the request, or deny the request.
-   Can a license be removed from an entity? The issuer is asked this question when a user tries to remove a license from their account or a team.
-   What are the details of a specific license key? This is used to display the license information to the user.

For each of these questions, you MUST implement the following 3 callbacks:

 1. GET `/get_license`
 2. POST `/add_license`
 3. POST `/remove_license`

Note that all the callbacks listed above follow the conventions listed below.

### Callback Conventions

Unless noted, the following conventions apply to *all* callbacks implemented by an issuer.

#### JSON

All payload to and from callbacks happens in [JSON format](https://www.json.org). To make this explicit, every request to a callback will have the  header `Content-Type: application/json` present in the HTTPS request.

#### Localization

In some circumstances, such as when additional input is required from a user when adding a license to an account, a localized response SHOULD be returned by the issuer in the user's locale. To make this possible, every request to a callback will have an `Accept-Language` header present like so:

    Accept-Language: fr-CH; fr;q=0.9, en;q=0.8, *;q=0.5

The header encodes the languages preferred by the user currently interacting with Cloud Zoo. If none of the languages specified in the header are available, English SHOULD be used.

#### Authentication

All endpoints in Cloud Zoo or on the issuer use [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) using the issuer’s id and the corresponding secret shared between Cloud Zoo and the respective issuer. You MUST make sure that the secret matches verbatim before processing any callback request on any endpoint to prevent a security breach. For example, on the issuer's end:
	
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
			    'Could not verify your access level for that URL.\n'
			    'You have to authenticate with proper credentials', 401,
			    {'WWW-Authenticate': 'Basic realm="Credentials Required"'})
		else:
			pass #Continue processing the request HERE
		
#### Non-successful responses

If returning a response with an HTTP status code greater or equal to `400`, the issuer SHOULD include the following JSON in the payload as well:

    {
		"description": "The license cannot be removed from Cloud Zoo because [Marley](https://example.com) says so.",
		"details": "request id 239231203123212"
	}

 - The `description` field is user facing, and SHOULD be localized.  In addition, the description string may have markdown style links as in the example above. The links can be used to help the user navigate and solve the issue.
 - The `details` field is not user-facing, but may be logged for troubleshooting purposes. You MUST NOT include sensitive data in the details string.

### Callbacks

#### GET `/get_license`

Return information about a specific license so users can see details about the license.

#### Example Request

    GET /get_license?aud=PRODUCT_ID&key=A_LICENSE_KEY

 - `aud`: The product id of the license whose information is to be returned.
 - `key`:  The license key of the license whose information is to be returned.

##### Required Response
The response will vary depending on the issuer’s decision as described below:

A successful response:

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: A license object (AJ TODO LINK!!!). See an actual example in our GitHub example (AJ TODO LINK!!!)

A non-successful (error) response:

- HTTP Status Code: A code greater or equal to `400 (Bad Request)` 
- Response Payload: A non-successful response (AJ TODO LINK!!!)
 
#### POST `/add_license`

See if a license can be added to an entity or whether an issuer should ask more information, or whether we should  
deny the request. This callback is invoked whenever a license is about to be added to an entity.

##### Example Request

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

-   `entityId`: The id of the entity whom the license will be added to. Entities can be individual users or groups as defined in Rhino Accounts.
-  `userInfo`: The decoded JWT representing the user’s OpenID Token who wants to add the license to the specified entity. See [Rhino Accounts OpenID Tokens](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig/edit#heading=h.qctsih4c0ctd) for details. The user is always a privileged member of the entity or is the entity itself in case `entityType` is `User`. Additional fields could be present and MAY be used but SHOULD NOT be assumed to be present.
-   `license`: The license that is to be added. This field is a simplified License object (AJ TODO LINK!!!) with the license key and product id of the license.
- `precondition`: This field is optional. If provided, it is a string string containing a precondition that was requested by the issuer (see response details below for more details on this field).

##### Required Response
The response will vary depending on the issuer’s decision as described below:

If the license *can* be added to an entity:
 - HTTP Status Code: `200 (OK)` 
 - Response Payload: A License Cluster object representing the license(s) to be added. See an actual example in our GitHub example (AJ TODO LINK!!!)

If more information (`precondition`) is required: 
- HTTP Status Code: `428 (Precondition Required)`
- Response Payload: A non-successful response (AJ TODO LINK!!!). The `description` field will be used to describe what input is required from the user, such as a previous license key or a secret code. See an actual example (AJ TODO LINK!!!).

If the additional information (`precondition`) is incorrect:
- HTTP Status Code: `412 (Precondition Failed)`
- Response Payload: A non-successful response (AJ TODO LINK!!!). See an actual example (AJ TODO LINK!!!)

If the license *cannot* be added to an entity:
- HTTP Status Code: `409 (Conflict)`
- Response Payload: A non-successful response (AJ TODO LINK!!!). See an actual example (AJ TODO LINK!!!)

##### Remarks

This callback MUST be idempotent, meaning that it MUST consistently return the same result given a set of arguments. This is because the callback may be called more than one time with the same arguments by the system as part of a transaction that could be retried.

#### POST `/remove_license`

See if a license can be removed from an entity. This callback is invoked right before a license is removed from an entity. Issuers SHOULD make sure to note that a license is no longer in the entity. 

##### Example Request

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

 - `entityId`: The id of the entity whom the license will be removed from. Entities can be individual users or groups as defined in [Rhino Accounts](https://accounts.rhino3d.com/help).
 - `entityType`:  Entities can be individual users (`User`) or groups (`Group`) as defined in [Rhino Accounts](https://accounts.rhino3d.com/help).
 - `userInfo`: The decoded JWT representing the user’s OpenID Token who wants to add the license to the specified entity. See [Rhino Accounts OpenID Tokens](https://docs.google.com/document/d/1-U0FYt6iQAM3UA6Rio4z0sDVXBSdc0kQk5e4zumnKig/edit#heading=h.qctsih4c0ctd) for details. The user is always a privileged member of the entity or is the entity itself in case `entityType` is `User`. Additional fields could be present and MAY be used but SHOULD NOT be assumed to be present.
 - `licenseCluster`: The License Cluster to be removed. AJ TODO LINK!!!!

##### Required Response
The response will vary depending on the issuer’s decision as described below:

A successful response (The license can be removed):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: Empty. See an actual example in our GitHub example (AJ TODO LINK!!!)

A non-successful (error) response (The license cannot be removed):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: A non-successful response (AJ TODO LINK!!!)

##### Remarks

This callback MUST be idempotent, meaning that it MUST consistently return the same result given a set of arguments. This is because the callback may be called more than one time with the same arguments by the system as part of a transaction that could be retried.

## Cloud Zoo Endpoints (*Optional*)

It is possible to query and modify licensing data stored in Cloud Zoo by a registered issuer. This can be useful when a customer returns a license for a refund, as well as other scenarios. It is not required that you interact with these endpoints, but you may find them useful given your business requirements.

### Endpoint Conventions

Unless noted, the following conventions apply to *all* endpoints available to registered issuers in Cloud Zoo.

#### Endpoint Location
All endpoint requests should be made to All calls are to made to `https://cloudzoo.rhino3d.com/v1`.

#### JSON

All payload to and from endpoints happens in [JSON format](https://www.json.org). To make this explicit, every response to an endpoint will have the  header `Content-Type: application/json` present in the HTTPS response.

#### Authentication

All endpoints in Cloud Zoo or on the issuer use [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). To receive a successful response from an endpoint, you must include an `Authorization` header like so:

    Authorization: Basic BASE64ENCODEDSTRING
Where `BASE64ENCODEDSTRING` is a base64 (AJ TODO LINK!!!) encoded string containing your issuer id and your issuer secret:

    BASE64ENCODEDSTRING = b64.encode(issuer_id + ":" + issuer_secret)
	
#### Non-successful responses

All unsuccessful responses from endpoints will have an HTTP status code greater or equal to `400`. If the status code is also less than `500`, the payload will include the following JSON:

    {
	    "Error": "SomeErrorCode"
		"Description": "A description about the error message",
		"Details": "More details about the error"
	}

 - The `Error` field contains a specific error code that can be used by the issuer to recognize a specific error, such as incorrect credentials. 
 - The `Description` field contains a description of the error.
 - The `Details` field contains details of the error, possibly suggesting how to fix it.

If the status code is greater or equal to `500`, the response may not be JSON and may be empty.

### Endpoints

#### DELETE `/license`

Removes a license from Cloud Zoo. This method deletes the entire License Cluster (AJ TODO LINK!!!)  the license is in. If the License Cluster the license belongs to contains additional licenses, they will be removed as well.

##### Example Request

    DELETE /license?licenseId=LICENSE_ID&productId=PRODUCT_ID&entityId=ENTITY_ID
    
-  `entityId`: The id of the entity the license belongs to.
-  `productId`: The id of the product the license represents. This is a GUID.
- `licenseId`: The license id that identifies a unique license within the product id domain.

##### Response

A successful response (The license was removed):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: Empty. 

A non-successful (error) response (The license cannot be removed):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: A non-successful response (AJ TODO LINK!!!)

### Related Topics

- [Creating Zoo Plugins]({{ site.baseurl }}/guides/rhinocommon/creating-zoo-plugins)
- [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo)
- [Sample RhinoCommon plugin project (GitHub)](https://github.com/mcneel/rhino-developer-samples/tree/6/rhinocommon/cs/SampleCsWithLicense)


