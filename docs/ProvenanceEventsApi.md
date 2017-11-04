# swagger_client.ProvenanceEventsApi

All URIs are relative to *http://localhost/nifi-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_input_content**](ProvenanceEventsApi.md#get_input_content) | **GET** /provenance-events/{id}/content/input | Gets the input content for a provenance event
[**get_output_content**](ProvenanceEventsApi.md#get_output_content) | **GET** /provenance-events/{id}/content/output | Gets the output content for a provenance event
[**get_provenance_event**](ProvenanceEventsApi.md#get_provenance_event) | **GET** /provenance-events/{id} | Gets a provenance event
[**submit_replay**](ProvenanceEventsApi.md#submit_replay) | **POST** /provenance-events/replays | Replays content from a provenance event


# **get_input_content**
> StreamingOutput get_input_content(id, cluster_node_id=cluster_node_id)

Gets the input content for a provenance event



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvenanceEventsApi()
id = 'id_example' # str | The provenance event id.
cluster_node_id = 'cluster_node_id_example' # str | The id of the node where the content exists if clustered. (optional)

try:
    # Gets the input content for a provenance event
    api_response = api_instance.get_input_content(id, cluster_node_id=cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceEventsApi->get_input_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The provenance event id. | 
 **cluster_node_id** | **str**| The id of the node where the content exists if clustered. | [optional] 

### Return type

[**StreamingOutput**](StreamingOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_content**
> StreamingOutput get_output_content(id, cluster_node_id=cluster_node_id)

Gets the output content for a provenance event



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvenanceEventsApi()
id = 'id_example' # str | The provenance event id.
cluster_node_id = 'cluster_node_id_example' # str | The id of the node where the content exists if clustered. (optional)

try:
    # Gets the output content for a provenance event
    api_response = api_instance.get_output_content(id, cluster_node_id=cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceEventsApi->get_output_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The provenance event id. | 
 **cluster_node_id** | **str**| The id of the node where the content exists if clustered. | [optional] 

### Return type

[**StreamingOutput**](StreamingOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenance_event**
> ProvenanceEventEntity get_provenance_event(id, cluster_node_id=cluster_node_id)

Gets a provenance event



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvenanceEventsApi()
id = 'id_example' # str | The provenance event id.
cluster_node_id = 'cluster_node_id_example' # str | The id of the node where this event exists if clustered. (optional)

try:
    # Gets a provenance event
    api_response = api_instance.get_provenance_event(id, cluster_node_id=cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceEventsApi->get_provenance_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The provenance event id. | 
 **cluster_node_id** | **str**| The id of the node where this event exists if clustered. | [optional] 

### Return type

[**ProvenanceEventEntity**](ProvenanceEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_replay**
> ProvenanceEventEntity submit_replay(body)

Replays content from a provenance event



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvenanceEventsApi()
body = swagger_client.SubmitReplayRequestEntity() # SubmitReplayRequestEntity | The replay request.

try:
    # Replays content from a provenance event
    api_response = api_instance.submit_replay(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceEventsApi->submit_replay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmitReplayRequestEntity**](SubmitReplayRequestEntity.md)| The replay request. | 

### Return type

[**ProvenanceEventEntity**](ProvenanceEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

