import asyncio

async def squarer(a):
    return a * a

async def doubler(a):
    return a * 2

async def main(x, y):
    async with asyncio.TaskGroup() as tg:
        tasks = tg.create_task(squarer(x)), tg.create_task(squarer(y))
    dx, dy = tasks[0].result(), tasks[1].result()
    async with asyncio.TaskGroup() as tg:
        tasks = tg.create_task(doubler(dx)), tg.create_task(doubler(dy))
    dx, dy = tasks[0].result(), tasks[1].result()
    return dx, dy

print(asyncio.run(main(2, 3)))
