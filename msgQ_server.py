from wsgiref.simple_server import make_server, demo_app
from msgQ import MsgQ, MsgQException
import string

q=MsgQ()

def simple_app(environ, start_response):
    """Simplest possible application object""" 
    status = '200 OK'
    #print "simple_app"
    method = string.lower(environ['REQUEST_METHOD'])
    body=''
    pi = environ['PATH_INFO'][1:]
    ret = ""
    ct = "text/json"

    if method=='post':
        body=environ['wsgi.input'].readline(int(environ['CONTENT_LENGTH']))
        #print body
        try:
            ret=q.post(pi, body)
        except MsgQException, me:
            status = " ".join([str(v) for v in me.value])
        else:
            status = "201 Post to Q"
    if method=="put":
        try: 
            ret=q.put(pi)
        except MsgQException, me:
            status = " ".join([str(v) for v in me.value])
    if method=='get':
        l = pi.split("/")
        if l[0] == 'msg':
            try:
                ret=q.get(l[1])
            except MsgQException, me:
                status = " ".join([str(v) for v in me.value])
        elif l[0] == 'index':
            ret = '<html><body><table>'
            for n in q.qDict:
                ret += "<tr><td>" + n + "</td><td>" + str(len(q.qDict[n].q)) + "</td></tr>"
            ret += '</table></body></html>'
            ct = "text/html"
    if method=='delete':
        try:
            ret=q.delete(pi)
        except MsgQException, me:
            status = " ".join([str(v) for v in me.value])
        else:
            status = "204 Deleted"

    response_headers = [('Content-type',ct)]
    start_response(status, response_headers)

    #print pi
    #print method
    #print body
    #print repr(environ)
    #print "RET:", repr(ret)
    if not ret: ret=""
    return [ret]

port=8990
httpd = make_server('', port, simple_app)
print "Serving HTTP on port", port, "..."

#httpd.handle_request()

# Respond to requests until process is killed
httpd.serve_forever()
