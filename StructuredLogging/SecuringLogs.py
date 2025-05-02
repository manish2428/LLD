# Never log: passwords, tokens, full request bodies
# Use libraries like pydantic’s .dict(exclude=...)
# Use log masking tools in production

##EXAMPLE
import logging

logging.info("Login attempt", extra={"user": "john", "token": "***"})


# In Production:
# Use tools or libraries to automate the exclusion or masking of sensitive data.
# For example, with Pydantic:

# from pydantic import BaseModel

# class LoginData(BaseModel):
#     user: str
#     token: str

#     def to_safe_dict(self):
#         return self.dict(exclude={"token"})

# data = LoginData(user="john", token="abc123")
# logging.info("Login attempt", extra=data.to_safe_dict())




# This ensures that sensitive fields like token are excluded from the logs.




#################EXAMPLE FOR STRUCTURED LOGGING################
# import logging
# from fastapi import Request

# logger = logging.getLogger("uvicorn")

# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     request_id = str(uuid.uuid4())
#     logger.info(f"{request_id} - Started {request.method} {request.url}")
#     response = await call_next(request)
#     logger.info(f"{request_id} - Completed with {response.status_code}")
#     return response
