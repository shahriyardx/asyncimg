import aiohttp
from io import BytesIO


async def get_image(link):
    """Get image from link

    Args:
        link (str): link to image
    
    Returns:
        BytesIO: The image bytes
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            data = await response.read()

    image_bytes = BytesIO(data)
    return image_bytes
