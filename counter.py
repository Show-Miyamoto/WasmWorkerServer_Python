CACHE_KEY = "counter"

def worker(request):
    count = Cache.get(CACHE_KEY)

    if count is None:
        count = 0
    else:
        count = int(count)

    body = '''\
        The counter valu is: {count}
    '''.format(
        count=count
    )

    res = Response(body)

    Cache.set(CACHE_KEY, count + 1)

    return res
