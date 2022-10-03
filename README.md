# apimatic-core-interfaces-python
This project contains the abstract layer for APIMatic's core library. The purpose of creating interfaces is to separate out the functionalities needed by APIMatic's core library module. The goal is to support scalability and feature enhancement of the core library and the SDKs along with avoiding any breaking changes by reducing tight coupling between modules through the introduction of interfaces.

## Interfaces
| Name                                                                       | Description                                                                              |
|--------------------------------------------------------------------------- |------------------------------------------------------------------------------------------|
| [`HttpClient`](apimatic_core_interfaces/client/http_client.py)             | To save both Request and Response after the completion of response                         |
| [`ResponseFactory`](apimatic_core_interfaces/factories/response_factory.py)| To convert the client-adapter response into a custom HTTP response                       |
| [`Authentication`](apimatic_core_interfaces/types/authentication.py)       | To setup methods for the validation and application of the required authentication scheme|


## Enumerations
| Name                                                                          | Description                                                     |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [`HttpMethodEnum`](apimatic_core_interfaces/types/http_method_enum.py )       | Enumeration containig HTTP Methods (GET, POST, PATCH, DELETE)   |
