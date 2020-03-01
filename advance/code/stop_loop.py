import asyncio

async def nip(times):
    print('go to bed')
    await asyncio.sleep(times)
    print('get up after {}s'.format(times))

def main():
    loop = asyncio.get_event_loop()
    tasks = [nip(times) for times in range(1,5)]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print('task cancel:{}'.format(task.cancel()))
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

main()