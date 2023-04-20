import asyncio
from asyncio import sleep

import requests


async def start():
    await checker()
    await sleep(10)
    print(requests.post("http://127.0.0.1:5000/app/api/v1.0/жопа").text)

async def worker():
    while True:
        print(1)
        await sleep(0.5)

async def checker():
    while True:
        response = requests.get("http://127.0.0.1:5000/app/api/v1.0/жопа").json()
        if response["status"]:
            print("YES")
        else:
            print("NO")
        await sleep(2)
if __name__ == "__main__":
    asyncio.run(start())