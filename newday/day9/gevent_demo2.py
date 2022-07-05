from gevent import monkey
import gevent
from urllib.request import urlopen

monkey.patch_all()


def f(url):
    print('get: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    # gevent.spawn(f, "https://www.python.org/"),
    # gevent.spawn(f, "https://www.yahoo.com/"),
    # gevent.spawn(f, "https://github.com/"),
    gevent.spawn(f, "http://www.baidu.com")
])
