import time, asyncio


TIME_TO_SLEEP = 1


def print_elapsed_time(target_func, start_time):
    print(f'{target_func.__name__} elapsed : {round(time.time() - start_time, 3) * 1000} ms')


def print_wrapper_args(*args):
    txt_args = ', '.join(str(arg) for arg in args)
    print(txt_args)


def async_wrapper(f):
    async def async_profile(*args, **kwargs):
        try:
            t1 = time.time()
            ret_value = await f(*args, **kwargs)
            print_elapsed_time(f, t1)
            return ret_value
        except Exception as e:
            print(e)
    return async_profile


def wrapper(f):
    def profile(*args, **kwargs):
        try:
            t1 = time.time()
            ret_value = f(*args, **kwargs)
            print_elapsed_time(f, t1)
            return ret_value
        except Exception as e:
            print(e)
    return profile


def wrapper_with_args(*wrapper_args):
    def inner_wrapper(f):
        def profile(*args, **kwargs):
            try:
                ret_value = f(*args, **kwargs)
                print_wrapper_args(*wrapper_args)
                return ret_value
            except Exception as e:
                print(e)
        return profile
    return inner_wrapper


def async_wrapper_with_args(*wrapper_args):
    def inner_async_wrapper(f):
        async def profile(*args, **kwargs):
            try:
                ret_value = await f(*args, **kwargs)
                print_wrapper_args(*wrapper_args)
                return ret_value
            except Exception as e:
                print(e)
        return profile
    return inner_async_wrapper


@wrapper_with_args("1", "2", "3") # 주의) sleep_func 를 호출하지 않아도 데코레이터는 실행된다.
@wrapper
def sleep_func():
    time.sleep(TIME_TO_SLEEP)


@async_wrapper_with_args("a", "b", "c")
@async_wrapper
async def async_sleep_func():
    await asyncio.sleep(TIME_TO_SLEEP)

    
    
def plain_sleep_func():
    time.sleep(TIME_TO_SLEEP)


if __name__ == "__main__":
    sleep_func()

    cur_loop = asyncio.get_event_loop()
    cur_loop.run_until_complete(async_sleep_func())

    # TODO ) 멱함수가 데코레이터와 다른 실행 순서인 이유 체크
    plain_sleep_func = wrapper_with_args("ㄱ", "ㄴ", "ㄷ")(wrapper)(plain_sleep_func)() 