import asyncio
import asyncpg


# pip install asyncpg

async def run():
    conn = await asyncpg.connect(user='', password='',
                                 database='', host='')

    await conn.fetch('''CREATE TABLE IF NOT EXISTS lid (id SERIAL PRIMARY KEY, name TEXT);''')
    await conn.execute('''
    INSERT INTO lidl (name) VALUES ($1)
    ''', 'John')
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
