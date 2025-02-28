import string
import redis

BASE62 = string.ascii_letters + string.digits
REDIS_HOST = 'redis'
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

def generate_short_url():
    counter = redis_client.incr(COUNTER_KEY)
    return base62_encode(counter)