import string
import redis
import os
import random

BASE62 = string.ascii_letters + string.digits
# Redis vars are currently not currently used
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = 6379
REDIS_DB = 0
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

COUNTER_KEY = 'url_counter'

def base62_encode(num):
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        num, rem = divmod(num, base)
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

# Redis implementation, this func is currently not used
def generate_short_url():
    counter = redis_client.incr(COUNTER_KEY)
    return base62_encode(counter)

def base62_decode(s):
    base = len(BASE62)
    strlen = len(s)
    num = 0

    idx = 0
    for char in s:
        power = (strlen - (idx + 1))
        num += BASE62.index(char) * (base ** power)
        idx += 1
    return num