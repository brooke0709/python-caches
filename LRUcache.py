import time
import operator

allCache = {}
timeCache = {}

def cache_update(user_input):
    input_key = user_input[0]
    #print input_key
    input_value = user_input[1]
    #print input_value

    allCache[input_key] = input_value
    timeCache[input_key] = time.time()
    if len(allCache) > 5:
        #print("get rid of one")
        sorted_Cache = sorted(timeCache.iteritems(), key=operator.itemgetter(1))
        remove_Key = sorted_Cache[0][0]
        print remove_Key
        del allCache[remove_Key]
        del timeCache[remove_Key]
    print allCache
    print timeCache

while True:
    raw_user_input = raw_input("Enter set: ")
    user_input = raw_user_input.strip().split(',')
    #print user_input[0]
    #print user_input[1]

    cache_update(user_input)

