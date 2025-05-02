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
#