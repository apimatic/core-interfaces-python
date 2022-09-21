# core-interfaces-python
This project contains the abstract layer for APIMatic's core-lib.

## Interfaces
| Name                                                                    | Description                                                        |
|-------------------------------------------------------------------------|--------------------------------------------------------------------|
| [` HttpClient`](core_interfaces/client/http_client.py)                  | To save both Request and Response after the completion of response |
| [`ResponseFactory`](core_interfaces/factories/response_factory.py)      | To create a Response                                               |
| [`Authentication`](core_interfaces/types/authentication.py)             | To setup methods for authentication                                |


## Enumerations
| Name                                                                          | Description                                                     |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [`HttpMethodEnum`](core_interfaces/types/http_method_enum.py )                | Enumeration containig HTTP Methods                              |
