#Rerties with exponential backoff
#-> why? Avoid flooding a failing service.Useful for calling external apis or microservices.
import time
import httpx

def retry_request(url, retries=3, backoff=0.5):
    for i in range(retries):
        try:
            response = httpx.get(url)
            if response.status_code == 200:
                return response
        except httpx.RequestError:
            time.sleep(backoff * (2 ** i))
            
    raise Exception("Request failed after retries")


retry_request(' https://jsonplaceholder.typicode.com/posts/1')