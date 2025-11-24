# Install

**Install httpx**
```python
pip install -r requirements.txt
```

**Run command:**
```python 
python main.py http://localhost:8000/ --ip 5 --requests 100 --sleep 0.00
```


Outputs in same directory in file `results.log`
```python
===== FLOOD TEST RESULTS =====
URL: http://localhost:8000/
Workers: 5
Requests per worker: 50
Total Requests: 250

--- IP 183.22.91.144 ---
200: 2
403: 0
429: 48
Latency avg: 14.28 ms
Latency min: 5 ms
Latency max: 34 ms
```
