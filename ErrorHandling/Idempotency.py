# Definition: Operation can be repeated without side effects.
# GET, PUT, DELETE → Naturally idempotent
# POST → Not idempotent unless handled

# Example: Idempotent POST using a unique idempotency key

# @app.post("/payments")
# def create_payment(payment: Payment, idempotency_key: str = Header(...)):
#     if key_exists(idempotency_key):
#         return get_cached_response(idempotency_key)
    
#     result = process_payment(payment)
#     cache_response(idempotency_key, result)
#     return result


#Another example for creating a users
############################    CLIENT SIDE    ########################
# import uuid
# import requests

# users = [
#     {"name": "Alice", "email": "alice@example.com"},
#     {"name": "Bob", "email": "bob@example.com"},
# ]

# for user in users:
#     idempotency_key = str(uuid.uuid4())  # Generate a unique key for each user
#     headers = {"Idempotency-Key": idempotency_key}
#     response = requests.post("https://example.com/users", json=user, headers=headers)
#     print(response.json())


###########################    SERVER SIDE      #########################
# @app.post("/users")
# def create_user(user: User, idempotency_key: str = Header(...)):
#     if key_exists(idempotency_key):
#         return get_cached_response(idempotency_key)
    
#     result = save_user_to_database(user)
#     cache_response(idempotency_key, result)
#     return result



############ To handle request with same data but multiple request call #####

import hashlib
import requests

users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
]

for user in users:
    # Generate idempotency_key based on user data
    idempotency_key = hashlib.sha256(f"{user['name']}{user['email']}".encode()).hexdigest()
    headers = {"Idempotency-Key": idempotency_key}
    response = requests.post("https://example.com/users", json=user, headers=headers)
    print(response.json())