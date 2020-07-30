import base64
import io, math
from PIL import Image, ImageDraw, ImageFont

def decode_img(msg):
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf, mode='r')
    return img

def add_watermark(input_img, watermark_text):
    # get a font
    fnt = ImageFont.truetype("arial.ttf", 32)
    # get a drawing context
    d = ImageDraw.Draw(input_img)
    x = (input_img.size[0]/2) - math.floor((len(watermark_text)/2)) - len(watermark_text)*2
    y = 60
    shadowColor = 0
    outlineAmount = 3
    
    #create outline text
    for adj in range(outlineAmount):
        #move right
        d.multiline_text((x-adj, y), watermark_text, font=fnt, fill=shadowColor, align="center")
        #move left
        d.multiline_text((x+adj, y), watermark_text, font=fnt, fill=shadowColor, align="center")
        #move up
        d.multiline_text((x, y+adj), watermark_text, font=fnt, fill=shadowColor, align="center")
        #move down
        d.multiline_text((x, y-adj), watermark_text, font=fnt, fill=shadowColor, align="center")
        #diagnol left up
        d.multiline_text((x-adj, y+adj), watermark_text, font=fnt, fill=shadowColor, align="center")
        #diagnol right up
        d.multiline_text((x+adj, y+adj), watermark_text, font=fnt, fill=shadowColor, align="center")
        #diagnol left down
        d.multiline_text((x-adj, y-adj), watermark_text, font=fnt, fill=shadowColor, align="center")
        #diagnol right down
        d.multiline_text((x+adj, y-adj), watermark_text, font=fnt, fill=shadowColor, align="center")
    # draw text, half opacity
    d.multiline_text((x,y), watermark_text, font=fnt, fill=(255,255,255,128), align="center")
    return input_img

if __name__ == "__main__":
    message = open("F:/Nand's Work Folder - DO NOT OPEN/heroku/Python/image watermark/image_data_base64.txt", "r").read()
    print("hello world")
    img = decode_img(message)
    out = add_watermark(img, "F:/Nand's Work \nFolder - DO NOT OPEN/heroku/Python/image watermark/image_data_base64.txt")
    imgByteArr = io.BytesIO()
    out.save(imgByteArr, format=img.format)
    out_string = base64.b64encode(imgByteArr.getvalue())
    f = open("F:/Nand's Work Folder - DO NOT OPEN/heroku/Python/image watermark/demofile2.txt", "w")
    f.write(str(out_string))
    f.close()
    # out_img = decode_img(out_string)
    # out_img.show()
