import urllib2
import httplib

class msgclient:
    def __init__(self, qServerUrl):
        self._url=qServerUrl
        self._hostname=self._url
        if self._hostname[-1]=="/":  #remove trailing /
            self._hostname = self._hostname[:-1] 
        if self._hostname[:7]=="http://":
            self._hostname = self._hostname[7:]
        
    def get(self, qName):
        url = self._url+qName
        
        try:
            data = urllib2.urlopen(url).read()
        except urllib2.HTTPError, e:
            print "HTTP error: %d" % e.code
        except urllib2.URLError, e:
            print "Network error: %s" % e.reason.args[1]
        return data

    def post(self, qName, value):
        url = self._url+qName
        try:
            data = urllib2.urlopen(url, value).read()
        except urllib2.HTTPError, e:
            if e.code==201: #Not really an error as that is the expected response
                data = e.msg
            else:
                print "HTTP error: %d" % e.code
                print repr(dir(e))
                print e.msg
        except urllib2.URLError, e:
            print "Network error: %s" % e.reason.args[1]
            raise
        return data

    def put(self, qName):
        conn = httplib.HTTPConnection(self._hostname)
        conn.request("PUT", "/" + qName)
        r1 = conn.getresponse()
        print r1.status, r1.reason
        data1 = r1.read()
        conn.close()
