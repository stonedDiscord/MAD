from contextlib import contextmanager

# https://stackoverflow.com/questions/16740104/python-lock-with-statement-and-timeout/16782391
from multiprocessing import Lock


class TimeoutLock(object):
    def __init__(self):
        self._lock = Lock()

    def acquire(self, blocking=True, timeout=-1):
        return self._lock.acquire(blocking, timeout)

    @contextmanager
    def acquire_timeout(self, timeout):
        result = self._lock.acquire(timeout=timeout)
        yield result
        if result:
            self._lock.release()

    def release(self):
        self._lock.release()