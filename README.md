#AI Agent Creation API Wrapper

This project provides a Flask-based API wrapper that standardizes the process of creating AI agents using two different AI services: VAPI and Retell. By sending a single request, users can choose between these services via a provider parameter, and the system will handle the request routing and response formatting.

**Features:**

*Unified API*: A single endpoint /create-agent allows the creation of AI agents using either the VAPI or Retell APIs.
*Standardized Input/Output*: Regardless of the selected provider, the input parameters and the response format are standardized for ease of use.
*Error Handling*: Proper error messages are returned when invalid input or API call failures occur.
*Easy Testing*: A Postman collection is provided for easy testing of both providers.
