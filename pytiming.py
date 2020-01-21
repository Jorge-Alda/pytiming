import time
import datetime
from contextlib import contextmanager

@contextmanager
def timing(mode=''):
    try:
        if mode == 'process':
            start = time.process_time()
        elif mode == 'thread':
            start = time.thread_time()
        elif mode == 'perf':
            start = time.perf_counter()
        else:
            start = time.time()
        yield start
    finally:
        if mode == 'process':
            end = time.process_time()
        elif mode == 'thread':
            end = time.thread_time()
        elif mode == 'perf':
            end = time.perf_counter()
        else:
            end = time.time()
        delta = datetime.timedelta(seconds=end-start)
        print(str(delta))

        
