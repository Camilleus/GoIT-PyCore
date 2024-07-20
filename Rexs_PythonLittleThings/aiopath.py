# Pakiet aiopath

"""
If you're writing asynchronous Python code and want to take advantage of pathlib's capabilities, 
but don't want to mix blocking and non-blocking I/O, you can use [aiopath](https://github.com/alexdelorenzo/aiopath). 
The aiopath API is exactly the same as the pathlib API, but all necessary methods are asynchronous.
"""

import asyncio
from aiopath import AsyncPath


async def main():
    apath = AsyncPath("hello.txt")
    print(await apath.exists())
    print(await apath.is_file())
    print(await apath.is_dir())

if __name__ == '__main__':
    asyncio.run(main())
