import asyncio

async def prod(q1):
    for i in range(5):
        await q1.put(f'value {i}')
        print(f'prod: put {i} to q1')
        await asyncio.sleep(1)

async def mid(q1, q2):
    while True:
        a = await q1.get()
        print(f'mid: got {a} from q1')
        await q2.put(a)
        print(f'mid: put {a} to q2')

async def cons(q2):
    while True:
        a = await q2.get()
        print(f'cons: got {a} from q2')

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    ptask = asyncio.create_task(prod(q1))
    mtask = asyncio.create_task(mid(q1, q2))
    ctask = asyncio.create_task(cons(q2))
    await ptask
    mtask.cancel()
    ctask.cancel()

asyncio.run(main())
