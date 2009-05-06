QNAME="testScriptQ"

curl -H "Accept: text/json" -X PUT  http://localhost:8990/$QNAME

for (( COUNT=0; COUNT<1000; COUNT=COUNT+1 )) ; 
do 
    #echo $COUNT 
    curl -H "Accept: text/json" -X post -d "Test: $COUNT"  http://localhost:8990/$QNAME
done 

for (( COUNT=0; COUNT<1000; COUNT=COUNT+1 )) ; 
do 
    #echo $COUNT 
    curl -H "Accept: text/json" -X GET  http://localhost:8990/msg/$QNAME
done 

curl -H "Accept: text/json" -X DELETE  http://localhost:8990/$QNAME