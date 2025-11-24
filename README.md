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
python main.py http://localhost:8000/ --ip 5 --requests 100 --sleep 0.00
```


Outputs in same directory in file `results.log`
```python
===== FLOOD TEST RESULTS =====
URL: http://localhost:8000/
Workers: 5
Requests per worker: 500
Total Requests: 2500
Delay per request: 0.0 sec

--- IP 75.47.75.234 ---
200: 200
403: 291
429: 9
Other: 0
ERR: 0
Latency avg: 9.40 ms
Latency min: 3 ms
Latency max: 1569 ms

--- IP 42.254.135.22 ---
200: 200
403: 291
429: 9
Other: 0
ERR: 0
Latency avg: 8.70 ms
Latency min: 2 ms
Latency max: 1247 ms

--- IP 93.243.60.67 ---
200: 200
403: 291
429: 9
Other: 0
ERR: 0
Latency avg: 8.12 ms
Latency min: 3 ms
Latency max: 912 ms

--- IP 109.117.182.190 ---
200: 200
403: 291
429: 9
Other: 0
ERR: 0
Latency avg: 7.52 ms
Latency min: 3 ms
Latency max: 616 ms

--- IP 148.188.131.177 ---
200: 200
403: 291
429: 9
Other: 0
ERR: 0
Latency avg: 6.83 ms
Latency min: 3 ms
Latency max: 282 ms
```
