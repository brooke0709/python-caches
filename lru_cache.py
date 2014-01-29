class LRUCache(object):
    
    def __init__(self, cap):
        self.cap = cap
        self.cache_keys = []
        self.cache_values = []

    def set(self, input_key, input_value):
        if input_key in self.cache_keys:
            key_index = self.cache_keys.index(input_key)
            self.cache_keys.pop(key_index)
            self.cache_values.pop(key_index)
            self.cache_keys.append(input_key)
            self.cache_values.append(input_value)
        else:
            self.cache_keys.append(input_key)
            self.cache_values.append(input_value)
        if len(self.cache_keys) > self.cap:
            self.cache_keys.pop(0)
            self.cache_values.pop(0)

    def get(self, input_key):
        if input_key in self.cache_keys:
            key_index = self.cache_keys.index(input_key)
            self.cache_keys.pop(key_index)
            return_value = self.cache_values.pop(key_index)
            self.cache_keys.append(input_key)
            self.cache_values.append(return_value)
            return return_value
        else:
            return None

    def print_cache(self):
        for item_index in range(0, len(self.cache_keys)):
            print "%s, %s\n" % (self.cache_keys[item_index], self.cache_values[item_index])



