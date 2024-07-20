# Pakiet aioshutil

"""
The [aioshutil](https://github.com/kumaraditya303/aioshutil) library provides an asynchronous version of the Shutil module functions. 
The Shutil module is synchronous, and using it in asynchronous programs will block the event loop and slow down the program. 
aioshutil provides asynchronous friendly versions of Shutil module functions.
"""

import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile


async def main():
    apath = AsyncPath("hello.txt")
    if await apath.exists():
        new_path = AsyncPath('logs')
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(apath, new_path / apath)

if __name__ == '__main__':
    asyncio.run(main())
