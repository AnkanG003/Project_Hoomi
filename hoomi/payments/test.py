import hmac
import hashlib

webhook_secret = b'q92ZjyG@i5DyNZs'
webhook_body = b'{"example":"data"}'  # raw request.body

signature = hmac.new(webhook_secret, webhook_body, hashlib.sha256).hexdigest()
print(signature)
