# basic example

from aiofile import AIOFile, LineReader
import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - async world!")

if __name__ == '__main__':
    asyncio.run(main())


# Podejście await afp.read()


async def main():
    async with async_open("hello.txt", 'r') as afp:
        print(await afp.read())

if __name__ == '__main__':
    asyncio.run(main())


# Podejście async for


async def main():
    async with async_open("hello.txt", 'r') as afp:
        async for line in afp:
            print(line)

if __name__ == '__main__':
    asyncio.run(main())


# LineReaner


async def main():
    async with AIOFile("hello.txt", 'r') as afp:
        async for line in LineReader(afp):
            print(line)

if __name__ == '__main__':
    asyncio.run(main())
