# Logging with Request IDs / Trace IDs
# Useful for tracing logs across services. Attach a unique ID to each request.

# import uuid
# from fastapi import Request

# @app.middleware("http")
# async def add_request_id(request: Request, call_next):
#     request_id = str(uuid.uuid4())
#     response = await call_next(request)
#     response.headers["X-Request-ID"] = request_id
#     print(f"[{request_id}] {request.method} {request.url}")
    # return response



#In production, integrate with OpenTelemetry or ELK Stack.
# Key Concepts:
# Request ID / Trace ID:

# A unique identifier (e.g., UUID) is generated for each incoming HTTP request.
# This ID is used to trace the request across logs, making it easier to debug and monitor distributed systems.
# Middleware:

# Middleware is a function that runs before and after each request in a FastAPI application.
# In this case, the middleware is used to generate a Request ID and attach it to the response headers.
# Integration:

# This approach can be extended to integrate with tools like OpenTelemetry or ELK Stack for centralized logging and tracing.





###############Example###################
######CLIENT REQUEST########
# GET /api/resource HTTP/1.1
# Host: example.com

#####SERVER RESPONSE########
# HTTP/1.1 200 OK
# X-Request-ID: 123e4567-e89b-12d3-a456-426614174000
# Content-Type: application/json

#####LOG OUTPUT####
# [123e4567-e89b-12d3-a456-426614174000] GET http://example.com/api/resource
