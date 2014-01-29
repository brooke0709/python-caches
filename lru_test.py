from lru_cache import LRUCache

my_cache = LRUCache(5)
my_cache.set("key1", "bar")
my_cache.set("key2", "bat")
my_cache.print_cache

print my_cache.get("key1")

my_cache.set("key3", "bad")
my_cache.set("key4", "ban")
my_cache.set("key5", "bay")

my_cache.print_cache()

print my_cache.get("key4")

my_cache.set("key6", "bla")

my_cache.print_cache()

print my_cache.get("key2")
