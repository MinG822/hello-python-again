import asyncio, inspect

'''
reference)
https://stackoverflow.com/questions/46258800/python-asyncio-walk-up-the-coroutine-chain
https://stackoverflow.com/questions/40641615/what-is-the-difference-between-a-frame-and-object-and-when-should-i-modify-one
https://elizaveta239.github.io/the-hidden-power-part1/
'''

TIME_TO_WAIT = 1


async def async_run():
    print(locals())
    tasks = [asyncio.create_task(f()) for f in [foo, bar]]
    print(locals())
    tasks += [asyncio.create_task(f()) for f in [foo, bar]]
    print(locals())
    await asyncio.gather(*tasks)


async def foo():
    await asyncio.sleep(TIME_TO_WAIT)
    cur_frame = inspect.currentframe()
    print('foo', cur_frame)
    await bar()


async def bar():
    cur_frame = inspect.currentframe()
    print('bar', cur_frame)
    print_frame_stack(cur_frame)



def print_frame_stack(frame):
    if frame is None:
        return
    print(frame.f_code.co_name)
    if frame.f_back:
        print_frame_stack(frame.f_back)


if __name__ == "__main__":
    print(locals())
    cur_frame = inspect.currentframe()
    print('main', cur_frame)
    cur_loop = asyncio.get_event_loop()
    cur_loop.run_until_complete(async_run())


