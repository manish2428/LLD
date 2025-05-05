# . Algorithm Overview:
    # A bucket holds tokens up to a maximum capacity.
    # Tokens are added at a fixed rate per second.
    # Each request consumes 1 token.
    # If the bucket has enough tokens, the request is allowed.
    # If not, it is rejected

import time
import threading

class TokenBucket:
    def __init__(self, rate: float, capacity: float):
        self.rate = rate              # Tokens per second
        self.capacity = capacity      # Max bucket size
        self.tokens = capacity        # Current token count
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def allow_request(self) -> bool:
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            refill = elapsed * self.rate

            self.tokens = min(self.capacity, self.tokens + refill)
            self.last_refill = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False

if __name__ == "__main__":
    bucket = TokenBucket(rate=5.0, capacity=10.0)  # 5 requests/sec, max 10 tokens
    accepted = 0
    rejected = 0
    for i in range(100):
        if bucket.allow_request():
            print(f"Request {i}: Allowed")
            accepted += 1
        else:
            print(f"Request {i}: Rejected")
            rejected += 1
        time.sleep(0.1)  # 10 requests/sec

    print(f"Total Requests Accepted: {accepted}, Total Requests Rejected: {rejected}")




