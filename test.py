import msgQ_client
import sys

mq = msgQ_client.msgclient("localhost", 8990)
mq.put("pyQ")

for i in range(10000):
    mq.post("pyQ", "pyTest"+str(i))

for i in range(10000):
    ret= mq.get("pyQ")
    #print ret
