# asyncimg
An async image manipulation lib. Can be used for discord.

# Usage
```py
from asyncimg import Generator

generator = Generator()
image = await generator.lovers(profile_pic_link1, profile_pic_link2)

# In discord command
file = discord.File(fp=image, filename='image.png')
await ctx.send(file=file)
```

# Available methods
```py
lovers(profile_pic_link1, profile_pic_link2)
stars(profile_pic_link)
colors(profile_pic_link)
frame(profile_pic_link)
envelop(profile_pic_link)
knockout(profile_pic_link1, profile_pic_link2)
fart(profile_pic_link)
```
> More coming soon

## Any help need or better suggesions? [Join here](https://discord.gg/7SaE8v2) to contribute