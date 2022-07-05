from urllib import request
import gevent


def f(url):
    print('get: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("url.html", "wb")
    f.write(data)
    f.close()
    pass


gevent.joinall([
    gevent.spawn(f, 'http://www.baidu.com'),
    gevent.spawn(f, 'http://www.baidu.com'),
    gevent.spawn(f, 'http://www.baidu.com'),
])

# f("http://www.baidu.com")
