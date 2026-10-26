import asyncio


async def another_task():
    print("starting another task")
    await asyncio.sleep(1)
    print("ending another task")


async def crashing_task():
    print("starting crashing task")
    await asyncio.sleep(0.1)
    raise ValueError("Boom!")


async def worker_task(tg):
    print("starting worker task")
    try:
        await asyncio.sleep(10)
        print("ending worker task")
    except asyncio.CancelledError:
        # this throws an error because TaskGroup <TaskGroup entered> is shutting down
        tg.create_task(another_task())


async def main():
    print("hello world")

    tg = asyncio.TaskGroup()

    # Error type 1:
    # this throws an runtime error
    # because TaskGroup <TaskGroup> has not been entered
    # tg.create_task(another_task())

    async with tg:
        tg.create_task(another_task())

        print("starting main task")
        await asyncio.sleep(0.5)
        print("ending main task")

        # Error type 3:
        # this combo also throws errors because
        # after the crashing_task() crashes and raises error,
        # the TaskGroup <TaskGroup tasks=1 errors=1 cancelling> is shutting down
        # TaskGroup cancels worker_task.
        # and rejects the create_task() call from the worker_task()
        # TaskGroup handles the closing of the coroutines as well.
        # tg.create_task(worker_task(tg))
        # tg.create_task(crashing_task())

    # Error type 2:
    # this throws an runtime error
    # because TaskGroup <TaskGroup entered> is finished
    # tg.create_task(another_task())


asyncio.run(main())
