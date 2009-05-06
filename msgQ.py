
class myQ(object):
    def __init__(self):
        #Also need a mutex eventually
        self.q=[]
    def get(self):
        if self.q==[]:
            return None
        else:
            #TODO: return in the future rather than pop.
            #TODO: Will need IDs and an accept method.
            return self.q.pop(0)
    #def accept(self):
    def put(self, val):
        self.q.append(val)

class MsgQException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#TODO: Add a message accept mechanism, instead of get deleting the message.
#      This and thread safety are the big outstanding areas where this 
#      doesn't meet the design.  Also, this is just the msg Q itself, and
#      not the WSGI interface to it.

class MsgQ(object):
    def __init__(self):
        self.qDict = {}
        #qDickLock=        
    def put(self, name):
        """Create a msg Q"""
        if name in self.qDict:
            raise MsgQException((409, "Already exists"))
        self.qDict[name] = myQ()
        
    def get(self, queueName):
        """Get the next message from a Q"""
        if not queueName in self.qDict:
            raise MsgQException((403, "Queue not found"))
        return self.qDict[queueName].get()
        
    def delete(self, queueName):
        """Delete a Q"""
        if not queueName in self.qDict:
            raise MsgQException((403, "Queue wasn't found"))
        del self.qDict[queueName]
    
    def post(self, queueName, content):
        """Put a msg in a queue"""
        if not queueName in self.qDict:
            raise MsgQException((403, "Queue wasn't found"))
        self.qDict[queueName].put(content)

if __name__=='__main__':
    q = MsgQ()
    q.put("unreadCount")
    print repr(q.qDict)
    q.post("unreadCount", {'id': 5})
    print repr(q.qDict['unreadCount'].q)
    print q.get('unreadCount')
    print q.get('unreadCount')
