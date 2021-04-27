import os
import asyncio
import functools
from asyncimg._util import get_image
from io import BytesIO
from asyncimg._generator import (
    generate_lovers,
    generate_frame,
    generate_stars,
    generate_colors,
    generate_envelop,
    generate_ko,
    generate_fart
)

lovers_bg = os.path.join(os.path.dirname(__file__), "assets", "love.png")
frame_bg = os.path.join(os.path.dirname(__file__), "assets", "envelop.png")
star_filter = os.path.join(os.path.dirname(__file__), "assets", "stars.png")
font = os.path.join(os.path.dirname(__file__), "assets", "font.ttf")
envelop_ = os.path.join(os.path.dirname(__file__), "assets", "envelop.png")
ko_bg = os.path.join(os.path.dirname(__file__), "assets", "ko.jpeg")
fart_bg = os.path.join(os.path.dirname(__file__), "assets", "fart.jpeg")


class Generator:
    def __init__(self):
        pass

    async def lovers(self, boy: str, girl: str) -> BytesIO:
        """
        Generate a lovers card

        Parameters
            boy     Link of boy's image
            girl    Link of girl's image
        """

        args = {
            "boy_image_bytes": await get_image(boy),
            "girl_image_bytes": await get_image(girl),
            "bg_path": self.lovers_bg,
        }

        func = functools.partial(generate_lovers, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)
        return image

    async def frame(self, profile: str) -> BytesIO:
        """
        Photo in a frame

        Parameters
            profile     Profile pic image
        """

        args = {"image_bytes": await get_image(profile), "bg_path": frame_bg}

        func = functools.partial(generate_frame, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)

        return image

    async def stars(self, profile: str) -> BytesIO:
        """
        Star filtered photo

        Parameters
            profile     Profile pic image
        """
        args = {
            "image_bytes": await get_image(profile),
            "filter_path": star_filter,
        }
        func = functools.partial(generate_stars, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)

        return image

    async def colors(self, profile: str) -> BytesIO:
        """
        Star filtered photo

        Parameters
            profile     Profile pic image
        """
        args = {"image_bytes": await get_image(profile), "font_path": font}
        func = functools.partial(generate_colors, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)

        return image

    async def envelop(self, profile: str) -> BytesIO:
        """
        Photo in a envelop

        Parameters
            profile     Profile pic image
        """

        args = {"image_bytes": await get_image(profile), "cover_path": envelop_}
        func = functools.partial(generate_envelop, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)

        return image

    async def knockout(self, profile1, profile2) -> BytesIO:
        """
        Generate a knockout image

        Parameters
            profile1    Profile picture image link of first person
            profile2    Profile picture image link of second person
        """

        args = {
            'profile1': await get_image(profile1),
            'profile2': await get_image(profile2),
            'bg_path': ko_bg
        }

        func = functools.partial(generate_ko, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)

        return image

    async def fart(self, profile) -> BytesIO:
        """
        Farting image

        Parameters
            profile     Profile pic image
        """
        args = {
            "profile": await get_image(profile),
            "bg_path": fart_bg,
        }
        func = functools.partial(generate_fart, **args)
        image = await asyncio.get_event_loop().run_in_executor(None, func)

        return image
