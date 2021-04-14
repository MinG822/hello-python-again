from asyncio import get_event_loop, set_event_loop, new_event_loop, sleep as asleep, set_event_loop_policy
from asyncio.events import BaseDefaultEventLoopPolicy
from threading import current_thread, Thread, local as thread_local


class ThreadEventLoopPolicy(BaseDefaultEventLoopPolicy):
    class _Local(thread_local):
        _loop = None
        _set_called = False

    def __init__(self):
        super().__init__()
        self._local = self._Local()

    def get_event_loop(self):
        if (self._local._loop is None and
                not self._local._set_called):
            self.set_event_loop(self.new_event_loop())

        if self._local._loop is None:
            raise RuntimeError('There is no current event loop in thread %r.'
                               % current_thread().name)

        return self._local._loop


class ThreadSensitiveLoopTest:
    def __init__(self):
        self.thread_loop_policy = None


    def set_policy(self):
        thread_loop_policy = ThreadEventLoopPolicy()
        set_event_loop_policy(thread_loop_policy)


    def run_in_thread_sensitive_loop(self):
        thread1 = Thread(target=self._sleep_async)
        try:
            yield thread1.start()
        finally:
            thread1.join()


    def _sleep_async(self):
        if self.thread_loop_policy is None or not isinstance(self.thread_loop_policy, (ThreadEventLoopPolicy,)):
            set_event_loop(new_event_loop())

        cur_loop = get_event_loop()
        print(current_thread(), '에서 1초간 잠듭니다')
        cur_loop.run_until_complete(asleep(1))
        cur_loop.close()






if __name__ == "__main__":
    # automatically event loop created for main thread (in default policy)
    loop = get_event_loop()

    new_loop = new_event_loop()
    set_event_loop(new_loop)
    cur_loop = get_event_loop()

    # one event loop per current (in default policy)
    print(loop == cur_loop)
    print(new_loop == cur_loop)

    thread_event_test = ThreadSensitiveLoopTest()

    # run sleep (in default policy)
    thread_event_test.run_in_thread_sensitive_loop()

    # run sleep (in customized policy)
    thread_event_test.set_policy()
    thread_event_test.run_in_thread_sensitive_loop()



