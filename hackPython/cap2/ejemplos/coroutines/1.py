import asyncio

async def example():
    print("Example is running")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(example())
