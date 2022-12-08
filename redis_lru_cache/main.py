import redis
from redis_lru import RedisLRU
import time

client = redis.StrictRedis(host='localhost', port=6379, password=None)
cache = RedisLRU(client=client, default_ttl=600)


@cache
def some_func(n: int):

    return 1000000 ** n


start_1 = time.time()
some_func(100000)
finish_1 = time.time()
without_cache_time = finish_1 - start_1

start_2 = time.time()
some_func(100000)
finish_2 = time.time()
using_cache_time = finish_2 - start_2


print(without_cache_time)
print(using_cache_time)
