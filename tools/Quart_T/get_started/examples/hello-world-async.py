import asyncio

from quart import Quart

app = Quart(__name__)

@app.route('/')
async def hello():
    return 'hello'

if __name__ == "__main__":
    asyncio.run(app.run_task())