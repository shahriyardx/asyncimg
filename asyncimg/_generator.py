import os
from PIL import Image, ImageFilter, ImageChops, ImageDraw, ImageFont
from io import BytesIO
from colorthief import ColorThief

lovers_bg = os.path.join(os.path.dirname(__file__), "assets", "love.png")


def get_bytes(final_image):
    """Get bytes of an image

    Args:
        final_image (Image.Image): Image to get bytes from

    Returns:
        BytesIO: The bytes of the image
    """
    final_bytes = BytesIO()
    final_image.save(final_bytes, "png")
    final_bytes.seek(0)

    return final_bytes


def generate_lovers(boy_image_bytes, girl_image_bytes, bg_path):
    """Generate lovers image

    Args:
        boy_image_bytes (BytesIO): Images bytes of first image
        girl_image_bytes (BytesIO): Image bytes of second image
        bg_path (str): Path string for background image

    Returns:
        BytesIO: The bytes of image
    """
    background = Image.open(bg_path).convert("RGBA")

    boy_image = (
        Image.open(boy_image_bytes)
        .convert("RGBA")
        .resize((325, 325))
        .rotate(3, expand=True)
    )
    girl_image = (
        Image.open(girl_image_bytes)
        .convert("RGBA")
        .resize((325, 325))
        .rotate(5, expand=True)
    )

    blank = Image.new("RGBA", background.size, (255, 255, 255, 0))

    blank.paste(boy_image, (240, 330))
    blank.paste(girl_image, (650, 278))

    final_image = Image.alpha_composite(blank, background)

    final_bytes = get_bytes(final_image)

    return final_bytes


def generate_frame(image_bytes, bg_path):
    """Generate frame image

    Args:
        image_bytes (BytesIO): Image bytes
        bg_path (str): Path string for background image

    Returns:
        BytesIO: The bytes of image
    """
    holder = Image.open(bg_path).convert("RGBA")

    profile = Image.open(image_bytes).convert("RGBA").resize((130, 130))

    blank = Image.new("RGBA", holder.size, (255, 255, 255, 0))
    blank.paste(profile, (265, 155))

    background = profile.resize((442, 442)).filter(ImageFilter.GaussianBlur(radius=3))
    background = background.convert("RGBA")

    final_image = Image.alpha_composite(blank, holder)
    final_image = Image.alpha_composite(background, final_image)

    final_bytes = get_bytes(final_image)

    return final_bytes


def generate_stars(image_bytes, filter_path):
    """Generate stars image

    Args:
        image_bytes (BytesIO): Image bytes
        filter_path (str): Filter path

    Returns:
        BytesIO: The bytes of image
    """
    profile = Image.open(image_bytes).convert("RGBA")
    filter_ = Image.open(filter_path).convert("RGBA").resize(profile.size)

    final_image = ImageChops.add(profile, filter_, 1, 0)

    final_bytes = get_bytes(final_image)

    return final_bytes


def generate_colors(image_bytes, font_path):
    """Generate colors image

    Args:
        image_bytes (BytesIO): Image bytes
        font_path (str): Font path

    Returns:
        BytesIO: The bytes of image
    """
    image_ct = ColorThief(image_bytes)
    image_pil = Image.open(image_bytes).resize((500, 500)).convert("RGBA")

    colors = ColorThief.get_palette(image_ct, color_count=5)

    blank = Image.new("RGBA", (200, 500), (255, 255, 255, 0))
    holder = Image.new("RGBA", (720, 500))
    draw = ImageDraw.Draw(blank)

    start = 0
    font = ImageFont.truetype(font_path, 15)
    for color in colors:
        draw.ellipse((0, start, 100, start + 100), fill=color)
        draw.text(
            (120, start + 40), "#%02x%02x%02x" % color, (255, 255, 255), font=font
        )
        start += 100

    holder.paste(image_pil, (220, 0))
    holder.paste(blank, (0, 0))

    final_bytes = get_bytes(holder)

    return final_bytes


def generate_envelop(image_bytes, cover_path):
    """Generate envelope image
    
    Args:
        image_bytes (BytesIO): Image bytes
        cover_path (str): Cover path
        
    Returns:
        BytesIO: The bytes of image
    """
    profile = Image.open(image_bytes).convert("RGBA").resize((278, 278)).rotate(11, expand=True)
    frame = Image.open(cover_path).convert("RGBA")  # 750x606

    blank = Image.new("RGBA", frame.size, (255, 255, 255, 0))

    blank.paste(profile, (227, 229))

    final_image = Image.alpha_composite(blank, frame)
    final_bytes = get_bytes(final_image)

    return final_bytes


def generate_ko(profile1, profile2, bg_path):
    """Generate ko image
    
    Args:
        profile1 (BytesIO): Profile 1 bytes
        profile2 (BytesIO): Profile 2 bytes
        bg_path (str): Background path
    
    Returns:
        BytesIO: The bytes of image
    """
    background = Image.open(bg_path).convert("RGBA")

    holder = Image.new("RGBA", size=background.size, color=(255, 255, 255, 0))
    mask = Image.new("RGBA", size=background.size, color=(255, 255, 255, 0))
    profile = Image.open(profile1).convert("RGBA").resize((80, 80))
    profile2 = Image.open(profile2).convert("RGBA").resize((80, 80)).rotate(-75, expand=True)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((90, 23, 170, 103), fill=(255, 25, 255, 255))
    mask_draw.ellipse((371, 38, 451, 118), fill=(255, 25, 255, 255))

    holder.paste(profile, (90, 23))
    holder.paste(profile2, (362, 29))

    final = Image.composite(holder, background, mask)

    final_bytes = get_bytes(final)

    return final_bytes


def generate_fart(profile, bg_path):
    """Generate fart image

    Args:
        profile (BytesIO): Profile bytes
        bg_path (str): Background path
    
    Returns:
        BytesIO: The bytes of image
    """
    background = Image.open(bg_path).convert("RGBA")

    holder = Image.new("RGBA", size=background.size, color=(255, 255, 255, 0))
    mask = Image.new("RGBA", size=background.size, color=(255, 255, 255, 0))
    profile = Image.open(profile).convert("RGBA").resize((80, 80)).rotate(-50, expand=True)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((451, 121, 530, 199), fill=(255, 25, 255, 255))

    holder.paste(profile, (434, 103))
    final = Image.composite(holder, background, mask)

    final_bytes = get_bytes(final)

    return final_bytes
