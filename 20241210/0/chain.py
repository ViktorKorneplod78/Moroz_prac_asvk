import asyncio

async def snd(ev):
    ev.set()
    print(f'snd: generated {ev}')

async def mid(num, evw, evs):
    await evw.wait()
    evs.set()
    print(f'mid(): generated {evw}')

async def rcv(ev0, ev1):
    await ev0.wait()
    await ev1.wait()
    print(f'rcv: generated {ev0}')

async def main():
    evs, evm0, evm1 = asyncio.Event(), asyncio.Event(), asyncio.Event()
    res = await asyncio.gather(rcv(evm0, evm1), mid(1, evs, evm1), mid(0, evs, evm0), snd(evs))
    return res
asyncio.run(main())
