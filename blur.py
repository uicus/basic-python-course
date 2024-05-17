import struct, math


def redden(pixel_list: bytearray, height: int, width: int) -> bytearray:
    for y in range(height):
        for x in range(width):
            pixel[width*y]


with open('picture.bmp', 'rb') as file:
    print('Type:', file.read(2).decode())
    print('Size: %s' % struct.unpack('I', file.read(4)))
    print('Reserved 1: %s' % struct.unpack('H', file.read(2)))
    print('Reserved 2: %s' % struct.unpack('H', file.read(2)))
    offset, = struct.unpack('I', file.read(4))
    print('Offset: %s' % offset)
    print('DIB Header Size: %s' % struct.unpack('I', file.read(4)))
    width, = struct.unpack('I', file.read(4))
    print('Width: %s' % width)
    height, = struct.unpack('I', file.read(4))
    print('Height: %s' % height)
    print('Colour Planes: %s' % struct.unpack('H', file.read(2)))
    print('Bits per Pixel: %s' % struct.unpack('H', file.read(2)))
    print('Compression Method: %s' % struct.unpack('I', file.read(4)))
    print('Raw Image Size: %s' % struct.unpack('I', file.read(4)))
    print('Horizontal Resolution: %s' % struct.unpack('I', file.read(4)))
    print('Vertical Resolution: %s' % struct.unpack('I', file.read(4)))
    print('Number of Colours: %s' % struct.unpack('I', file.read(4)))
    print('Important Colours: %s' % struct.unpack('I', file.read(4)))
    file.seek(0)
    header = bytearray(file.read(offset))
    content = bytearray(file.read())
    if width*height*3 != len(content):
        raise Exception("Coś się nie zgadza!")

with open('picture_output.bmp', 'wb') as file:
    file.write(header)
    file.write(content)
