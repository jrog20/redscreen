from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.55

def redscreen(main_filename, back_filename):
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    image.make_as_big_as(back)

    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image

def main():
    original_redrose = SimpleImage('images/redrose.jpg')
    original_redrose.show()

    original_purpleswirl = SimpleImage('images/purpleswirl.jpg')
    original_purpleswirl.show()

    redrose_purpleswirl_replaced = redscreen('images/redrose.jpg', 'images/purpleswirl.jpg')
    redrose_purpleswirl_replaced.show()


if __name__ == '__main__':
    main()
