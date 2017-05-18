#!/usr/bin/env python

from PIL import Image
import sys


def merge_pixel(up_pixel, down_pixel, up_rate, down_rate):
    new_pixel_R = int(up_pixel[0] * up_rate + down_pixel[0] * down_rate)
    new_pixel_G = int(up_pixel[1] * up_rate + down_pixel[1] * down_rate)
    new_pixel_B = int(up_pixel[2] * up_rate + down_pixel[2] * down_rate)
    return (new_pixel_R, new_pixel_G, new_pixel_B)

def merge_image(up_image, down_image, up_rate, down_rate):
    width = up_image.size[0]
    height = up_image.size[1]
    total = width * height
    print "[+] Resize the down image to (%d x %d)..." % (width, height)
    down_image = down_image.resize((width, height))

    print "[+] Building new image..."
    output_image = Image.new("RGB", (width, height), (0,0,0))

    counter = 0
    for i in xrange(width):
        for j in xrange(height):
            show_progress(counter, total)
            up_pixel = up_image.getpixel((i, j))
            down_pixel = down_image.getpixel((i, j))
            new_pixel = merge_pixel(up_pixel, down_pixel, up_rate, down_rate)
            output_image.putpixel((i, j), new_pixel)
            counter += 1

    output_image.show()

def show_progress(progress, total):
    percent = (((progress * 1.0) / total) * 100)
    sys.stdout.write("[+] %2f%%\r" % (percent))
    sys.stdout.flush()


def main():
    if len(sys.argv) != 5:
        print "Usage : "
        print "        python ImageCombiner.py [ImageA] [ImageB] [RateA] [RateB]"
        print "Author : "
        print "        WangYihang <wangyihanger@gmail.com>"
        exit(1)
    up_image = Image.open(sys.argv[1])
    down_image = Image.open(sys.argv[2])
    rate_A = float(sys.argv[3])
    rate_B = float(sys.argv[4])
    merge_image(up_image, down_image, rate_A, rate_B)

if __name__ == "__main__":
    main()
