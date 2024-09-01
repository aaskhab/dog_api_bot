import logging
import asyncio
from aiohttp import ClientSession

async def get_dog_url():
    url = 'https://dog.ceo/api/breeds/image/random'
    
    async with ClientSession() as session:
        response = await session.get(url=url)

        response = await response.json()

        if response['status'] == 'success':
            return response['message']
        else:
            logging.info('Wrong response: %s', response)