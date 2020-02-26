from multiprocessing import Process, Queue, Manager, Pool, Pipe
import time

def producer(queue):
    queue.put('food')
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    print(queue.get())

def producer_pipe(send_port):
    send_port.send('food')

def consumer_pipe(recv_port):
    print(recv_port.recv())

def producer_dict(arg_dict):
    arg_dict['Producer'] = 'create food'

def consumer_dict(arg_dict):
    arg_dict['Consumer'] = 'eat food'

if __name__ == '__main__':

    # 两进程间通过消息队列通信

    # queue = Queue(10)
    # produce_thread = Process(target=producer, args=(queue,))
    # consume_thread = Process(target=consumer, args=(queue,))

    # produce_thread.start()
    # consume_thread.start()

    # produce_thread.join()
    # consume_thread.join()

    # 进程池间通过共享变量通信

    # queue = Manager().Queue(10)
    # pool = Pool(2)
    
    # pool.apply_async(producer, args=(queue,))
    # pool.apply_async(consumer, args=(queue,))

    # pool.close()
    # pool.join()

    # 两进程间通过管道通信

    # send_port, recv_port = Pipe()
    # produce_thread = Process(target=producer_pipe, args=(send_port,))
    # consume_thread = Process(target=consumer_pipe, args=(recv_port,))

    # produce_thread.start()
    # consume_thread.start()

    # produce_thread.join()
    # consume_thread.join()

    # 通过共享变量通信
    arg_dict = Manager().dict()
    produce_thread = Process(target=producer_dict, args=(arg_dict,))
    consume_thread = Process(target=consumer_dict, args=(arg_dict,))

    produce_thread.start()
    consume_thread.start()

    produce_thread.join()
    consume_thread.join()
    print(arg_dict)