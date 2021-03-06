# roccclient.ChallengeApi

All URIs are relative to *https://rocc.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_challenge**](ChallengeApi.md#create_challenge) | **POST** /challenges | Add a challenge
[**delete_challenge**](ChallengeApi.md#delete_challenge) | **DELETE** /challenges/{challengeId} | Delete a challenge
[**get_challenge**](ChallengeApi.md#get_challenge) | **GET** /challenges/{challengeId} | Get a challenge
[**list_challenges**](ChallengeApi.md#list_challenges) | **GET** /challenges | List all the challenges


# **create_challenge**
> ChallengeCreateResponse create_challenge(challenge_create_request)

Add a challenge

Adds a challenge

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.ChallengeApi(api_client)
    challenge_create_request = roccclient.ChallengeCreateRequest() # ChallengeCreateRequest | 

    try:
        # Add a challenge
        api_response = api_instance.create_challenge(challenge_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->create_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_create_request** | [**ChallengeCreateRequest**](ChallengeCreateRequest.md)|  | 

### Return type

[**ChallengeCreateResponse**](ChallengeCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid request |  -  |
**409** | The request conflicts with current state of the target resource |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_challenge**
> object delete_challenge(challenge_id)

Delete a challenge

Deletes the challenge specified

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The ID of the challenge

    try:
        # Delete a challenge
        api_response = api_instance.delete_challenge(challenge_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->delete_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The ID of the challenge | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge**
> Challenge get_challenge(challenge_id)

Get a challenge

Returns the challenge specified

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.ChallengeApi(api_client)
    challenge_id = 'challenge_id_example' # str | The ID of the challenge

    try:
        # Get a challenge
        api_response = api_instance.get_challenge(challenge_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->get_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **str**| The ID of the challenge | 

### Return type

[**Challenge**](Challenge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The specified resource was not found |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_challenges**
> PageOfChallenges list_challenges(limit=limit, offset=offset, filter=filter)

List all the challenges

Returns all the challenges

### Example

```python
from __future__ import print_function
import time
import roccclient
from roccclient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rocc.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = roccclient.Configuration(
    host = "https://rocc.org/api/v1"
)


# Enter a context with an instance of the API client
with roccclient.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = roccclient.ChallengeApi(api_client)
    limit = 10 # int | Maximum number of results returned (optional) (default to 10)
offset = 0 # int | Index of the first result that must be returned (optional) (default to 0)
filter = roccclient.ChallengeFilter() # ChallengeFilter | Object that describes how to filter the results (optional)

    try:
        # List all the challenges
        api_response = api_instance.list_challenges(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChallengeApi->list_challenges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results returned | [optional] [default to 10]
 **offset** | **int**| Index of the first result that must be returned | [optional] [default to 0]
 **filter** | [**ChallengeFilter**](.md)| Object that describes how to filter the results | [optional] 

### Return type

[**PageOfChallenges**](PageOfChallenges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | The request cannot be fulfilled due to an unexpected server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

