+++
aliases = ["/en/en/5/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/", "/en/6/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/", "/en/7/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/", "/wip/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/"]
authors = [ "aj" ]
categories = [ "CloudZoo" ]
description = "It is possible to query and modify licensing data stored in Cloud Zoo by a registered issuer. This can be useful when a customer returns a license for a refund, as well as other scenarios. It is not required that you interact with these endpoints, but you may find them useful given your business requirements."
keywords = [ "Plugin", "Cloud Zoo" ]
languages = "unset"
sdk = [ "RhinoCommon" ]
title = "Optional Cloud Zoo endpoints for License Management"
type = "guides"
weight = 6
override_last_modified = "2021-06-02T11:33:03Z"

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

Unless noted, the following conventions apply to *all* endpoints available to registered issuers in Cloud Zoo.

### Endpoint Location

The base URL for all requests is `https://cloudzoo.rhino3d.com/v1`.

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

Removes a license from Cloud Zoo. This method deletes the entire [License Cluster object](/guides/rhinocommon/cloudzoo/cloudzoo-licensecluster) the license is in. If the License Cluster the license belongs to contains additional licenses, they will be removed as well.

{{< call-out "note" "Heads up!" >}}
This endpoint expects the arguments to be passed as a <a href="https://en.wikipedia.org/wiki/Query_string" class="alert-link">query string</a>.
{{< /call-out >}}

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

### PUT /license

Adds or replaces a License Cluster in Cloud Zoo. If any of the licenses in the [License Cluster object](/guides/rhinocommon/cloudzoo/cloudzoo-licensecluster) passed already exist in the given entity, their license cluster will be overwritten with the License Cluster passed. If there is more than one cluster in the entity containing the licenses in the cluster passed, an error will be returned and the operation will be aborted.

#### Example Request

    PUT /license
	
	{
	    "entityId": "9034901491490-|-Group",
	    "licenseCluster": LICENSE_CLUSTER_OBJECT
	}

	
The `entityId` should be the entity where the License Cluster will be added or updated.
The `licenseCluster` should be a [License Cluster object](/guides/rhinocommon/cloudzoo/cloudzoo-licensecluster) representing the license(s) to be added or updated.

#### Response

A successful response (The license was removed):

 - HTTP Status Code: `200 (OK)` 
 - Response Payload: Empty. 

A non-successful (error) response (The license cannot be added/updated):

- HTTP Status Code: A code greater or equal to `400 (Bad Request)`
- Response Payload: [A non-successful response](#non-successful-responses)


