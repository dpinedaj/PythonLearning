import asyncio


async def simulated_fetch(url, delay):
    await asyncio.sleep(delay)
    print(f"Fetched {url} after {delay}")
    return f"<html>{url}"


def main():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(
        asyncio.gather(
            simulated_fetch("http://google.com", 2),
            simulated_fetch("http://bbc.co.uk", 1),
        )
    )
    print(results)


main()
