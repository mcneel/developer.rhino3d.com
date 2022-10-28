+++
aliases = ["/5/guides/rhinocommon/cloudzoo/cloudzoo-add-products/", "/6/guides/rhinocommon/cloudzoo/cloudzoo-add-products/", "/7/guides/rhinocommon/cloudzoo/cloudzoo-add-products/", "/wip/guides/rhinocommon/cloudzoo/cloudzoo-add-products/"]
authors = [ "aj" ]
categories = [ "CloudZoo" ]
description = "Once you are registered as an issuer, you can add, view, and modify products in Cloud Zoo using the endpoints described below."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "Add Products to Cloud Zoo"
type = "guides"
weight = 3
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


## Endpoint Conventions

Unless noted, the following conventions apply to *all* product endpoints available to registered issuers in Cloud Zoo.

### Endpoint Location
All requests should be made to the following location: `https://cloudzoo.rhino3d.com/v1`.

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

If the status code is greater or equal to `500`, the response may not be JSON and may be empty.

## Endpoints

### POST /product

Adds a product to Cloud Zoo registered under the authenticating issuer.

#### Example Request

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

The payload should be a [Product object](/guides/rhinocommon/cloudzoo/cloudzoo-product).

{{< call-out "note" "Note" >}}
The product ID must be lowercase!
{{< /call-out >}}

#### Response

A successful response (The product was created):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: The newly created [Product object](/guides/rhinocommon/cloudzoo/cloudzoo-product). 

A non-successful (error) response (The product could not be created):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: [A non-successful response](#non-successful-responses)

### PUT /product/{product_id}

Modifies an existing product with the given `product_id`. Note that some properties of a product cannot be modified after creation, including but not limited to its unique id.

#### Example Request

    PUT /product/06bb1e79-5456-47a1-ad6d-104518cd894b
	
	{
	    "platforms": [
	        "Windows", "Mac"
	    ],
	    "picture": "https://elisapi.mcneel.com/media/new_icon_url"
	}

#### Response

A successful response (The product was modified):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: The newly updated [Product object](/guides/rhinocommon/cloudzoo/cloudzoo-product). 

A non-successful (error) response (The product could not be modified):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: [A non-successful response](#non-successful-responses)

### GET /product/{product_id}

Gets an existing product with the given `product_id`.

#### Example Request

    GET /product/06bb1e79-5456-47a1-ad6d-104518cd894b

#### Response

A successful response:

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: A [Product object](/guides/rhinocommon/cloudzoo/cloudzoo-product). 

A non-successful (error) response:

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: [A non-successful response](#non-successful-responses)