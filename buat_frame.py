from PIL import Image, ImageDraw

img = Image.new('RGBA', (600, 900), color=(200, 230, 255, 255))
draw = ImageDraw.Draw(img)

draw.rectangle([50, 50, 550, 300], fill=(0, 0, 0, 0))
draw.rectangle([50, 325, 550, 575], fill=(0, 0, 0, 0))
draw.rectangle([50, 600, 550, 850], fill=(0, 0, 0, 0))

img.save("frame_template.png")
print("frame_template.png berhasil dibuat!")