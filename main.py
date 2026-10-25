import asyncio


async def another_task():
    print("starting another task")
    await asyncio.sleep(1)
    print("ending another task")


async def main():
    print("hello world")

    # this throws a runtime warning as another_task() returns a coroutine
    # and it does not execute a single line of code
    # you'd have to await it to execute the code
    # or use asyncio.create_task() to create a task
    task = another_task()

    # This throws a runtime error as it is responsible for starting an event loop
    # asyncio.run(another_task())

    # before running the entire task the asyncio.run() destroys the event loop
    # at the completion of the main function
    # asyncio.create_task(another_task())

    task = asyncio.create_task(another_task())

    print("some task in main")
    await asyncio.sleep(0.5)
    print("some task ended in main")

    # this is important as it keeps the event loop running
    await task
    print()

    # OR one better way to do this is

    async with asyncio.TaskGroup() as tg:
        tg.create_task(another_task())

        print("some task in main")
        await asyncio.sleep(0.5)
        print("some task ended in main")

    # No need for await task


asyncio.run(main())
