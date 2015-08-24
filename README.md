# speeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeed

## Start python server
python python/server.py

## Start node server
cd node && npm install
node node/index.js

## Bench Python 
ab -n 1000 -c 100 http://127.0.0.1:8888/

## Bench Node
ab -n 1000 -c 100 http://127.0.0.1:8881/
