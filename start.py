import asyncio

from app.handlers.schedulers import run_scheduler

if __name__ == '__main__':
    print("Polling...")
    asyncio.run(run_scheduler())
