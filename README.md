# Install

**Install httpx**
```
pip install -r requirements.txt
```

or
```
pip install httpx rich
```

**Run command:**
``` 
python main.py http://localhost:8000/ --ip 5 --requests 5000 --sleep 0.00
```


Outputs in same directory in file `results.log`
```python
===== FLOOD TEST RESULTS =====
URL: http://localhost:8000/
Workers: 5
Requests per worker: 5000
Total Requests: 25000
Delay per request: 0.0 sec

--- IP 251.166.198.199 ---
200: 200
403: 4796
429: 4
Other: 0
ERR: 0
Latency avg: 6.92 ms
Latency min: 3 ms
Latency max: 1619 ms

--- IP 171.180.27.214 ---
200: 200
403: 4796
429: 4
Other: 0
ERR: 0
Latency avg: 6.89 ms
Latency min: 2 ms
Latency max: 1309 ms

--- IP 77.72.241.132 ---
200: 200
403: 4796
429: 4
Other: 0
ERR: 0
Latency avg: 6.84 ms
Latency min: 2 ms
Latency max: 965 ms

--- IP 41.219.206.186 ---
200: 200
403: 4796
429: 4
Other: 0
ERR: 0
Latency avg: 6.74 ms
Latency min: 2 ms
Latency max: 658 ms

--- IP 93.65.109.171 ---
200: 200
403: 4796
429: 4
Other: 0
ERR: 0
Latency avg: 6.68 ms
Latency min: 3 ms
Latency max: 341 ms
```
