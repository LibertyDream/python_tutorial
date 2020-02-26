from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    rst = fib(n-1) + fib(n-2)
    return rst

def sleep(times):
    time.sleep(times)
    return 'done'

if __name__ == '__main__':

    for func in [ProcessPoolExecutor, ThreadPoolExecutor]:
        with func(max_workers=3) as exc:
            print('{} begin compute Fibonacci'.format(exc.__class__.__name__))
            tasks_rst = [exc.submit(fib, (i)) for i in range(20, 35)]
            start_time = time.time()
            rst = []
            for future in as_completed(tasks_rst):
                rst.append(future.result())
            print(rst)
            print('{} time cost:{}'.format(exc.__class__.__name__, (time.time() - start_time)))
    
    print('--------------------')

    for func in [ProcessPoolExecutor, ThreadPoolExecutor]:
        with func(max_workers=3) as exc:
            print('{} begin random sleep test'.format(exc.__class__.__name__))
            tasks_rst = [exc.submit(sleep, (i)) for i in [2]*10]
            start_time = time.time()
            rst = []
            for future in as_completed(tasks_rst):
                rst.append(future.result())
            print('{} time cost:{}'.format(exc.__class__.__name__, (time.time() - start_time)))