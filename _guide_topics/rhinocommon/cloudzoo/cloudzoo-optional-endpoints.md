---
title: Optional Cloud Zoo endpoints for License Management
description: It is possible to query and modify licensing data stored in Cloud Zoo by a registered issuer. This can be useful when a customer returns a license for a refund, as well as other scenarios. It is not required that you interact with these endpoints, but you may find them useful given your business requirements.
authors: ['aj']
sdk: ['RhinoCommon']
languages: unset
platforms: ['Windows', 'Mac']
categories: ['CloudZoo']
origin: unset
order: 1
keywords: ['Plugin', 'Cloud Zoo']
layout: toc-guide-page
---

## Endpoint Conventions

Unless noted, the following conventions apply to *all* endpoints available to registered issuers in Cloud Zoo.

### Endpoint Location
All endpoint requests should be made to All calls are to made to `https://cloudzoo.rhino3d.com/v1`.

### JSON

All payload to and from endpoints happens in [JSON format](https://www.json.org). To make this explicit, every response to an endpoint will have the  header `Content-Type: application/json` present in the HTTPS response.

### Authentication

All endpoints in Cloud Zoo or on the issuer use [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). To receive a successful response from an endpoint, you must include an `Authorization` header like so:
	
```
Authorization: Basic BASE64ENCODEDSTRING
```

where `BASE64ENCODEDSTRING` is a [base64](https://en.wikipedia.org/wiki/Base64) encoded string containing your issuer id and your issuer secret: 

```python
	BASE64ENCODEDSTRING = b64.encode(issuer_id + ":" + issuer_secret)
```
	
### Non-successful responses

All unsuccessful responses from endpoints will have an HTTP status code greater or equal to `400`. If the status code is also less than `500`, the payload will include the following JSON:

    {
	    "Error": "SomeErrorCode"
		"Description": "A description about the error message",
		"Details": "More details about the error"
	}

 - The `Error` field contains a specific error code that can be used by the issuer to recognize a specific error, such as incorrect credentials. 
 - The `Description` field contains a description of the error.
 - The `Details` field contains details of the error, possibly suggesting how to fix it.

If the status code is greater or equal to `500`, the response may not be in JSON format and may be empty.

## Endpoints

### DELETE /license

Removes a license from Cloud Zoo. This method deletes the entire [License Cluster object]({{ site.baseurl }}/guides/rhinocommon/cloudzoo/cloudzoo-licensecluster) the license is in. If the License Cluster the license belongs to contains additional licenses, they will be removed as well.

#### Example Request

    DELETE /license?licenseId=LICENSE_ID&productId=PRODUCT_ID&entityId=ENTITY_ID
    
-  `entityId`: The id of the entity the license belongs to.
-  `productId`: The id of the product the license represents. This is a GUID.
- `licenseId`: The license id that identifies a unique license within the product id domain.

#### Response

A successful response (The license was removed):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: Empty. 

A non-successful (error) response (The license cannot be removed):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: [A non-successful response](#non-successful-responses)


