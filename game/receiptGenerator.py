from PIL import Image, ImageDraw, ImageFont, ImageOps


def _insert_text(draw: ImageDraw, x, y, text,
                 color='rgb(0, 0, 0)',
                 font_file='fonts/Roboto-Bold.ttf',
                 font_size=12):
    text = str(text)
    font = ImageFont.truetype(font_file, size=font_size)
    draw.text((x, y), text, fill=color, font=font)
    return draw


def _combine_all_images_horizantally(images):
    w = sum(i.size[0] for i in images)
    mh = max(i.size[1] for i in images)

    result = Image.new("RGBA", (w, mh))

    x = 0
    for i in images:
        result.paste(i, (x, 0))
        x += i.size[0]
    return result


def _combine_all_images_vertically(images):
    w = max(i.size[0] for i in images)
    mh = sum(i.size[1] for i in images)

    result = Image.new("RGBA", (w, mh))

    x = 0
    for i in images:
        result.paste(i, (0, x))
        x += i.size[1]
    return result


class ReceiptGenerator:
    def __init__(self, size=None):
        self.header = None
        self.body = None
        self.footer = None
        self.final_output_image = None
        self._debug_ = False  # Debug Param

        self.image_size = size if size else (320, 480)
        self.image_line_sep = self._text_image('--' * 35, font_size=14, size=self.image_size)
        self.image_whitespace_sep = self._text_image(' ', font_size=14, size=self.image_size)

        self.receipt_text_data = []

    def _text_image(self, text, font_size=12, size=(320, 480)):
        width, height = size
        _text = text.center(int(int(width / font_size) * 3.2))
        if self._debug_:
            _text = _text.replace(' ', '.')
        image = Image.new(mode="RGB", size=(width, font_size + 4), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw = _insert_text(draw=draw, x=0 + 4, y=0, text=_text, font_size=font_size)
        if self._debug_:
            image = ImageOps.expand(image, border=2, fill='black')
        return image

    def generate_header(self, header_text_data):

        image1 = _combine_all_images_vertically([
            self._text_image(header_text_data[0], font_size=25, size=(320, 0)),
            self._text_image(header_text_data[1], font_size=12, size=(320, 0)),
            self._text_image(header_text_data[2], font_size=12, size=(320, 0)),
        ]
        )
        self.receipt_text_data += header_text_data[:3]

        image2 = _combine_all_images_horizantally([
            self._text_image(header_text_data[3], font_size=12, size=(160, 0)),
            self._text_image(header_text_data[4], font_size=12, size=(160, 0))
        ])
        self.receipt_text_data.append(header_text_data[3] + ' ' + header_text_data[4])

        self.header = _combine_all_images_vertically([image1, image2])

    def generate_body(self, body_text_data):

        bag = []

        for each_line in body_text_data:
            _image_line_item = _combine_all_images_horizantally([
                self._text_image(each_line[0], font_size=12, size=(40, 0)),
                self._text_image(each_line[1], font_size=12, size=(160, 0)),
                self._text_image(each_line[2], font_size=12, size=(40, 0)),
                self._text_image(each_line[3], font_size=12, size=(80, 0)),
            ])
            bag.append(_image_line_item)
            self.receipt_text_data.append('{} {} {} {}'.format(*each_line))

        image3 = _combine_all_images_vertically(bag)

        self.body = image3

    def generate_footer(self, footer_text_data):

        bag = []
        for each_line in footer_text_data:
            _image_text = _combine_all_images_horizantally([
                self._text_image('', font_size=14, size=(160, 0)),
                self._text_image(each_line[0], font_size=14, size=(80, 0)),
                self._text_image(each_line[1], font_size=14, size=(80, 0))
            ])
            bag.append(_image_text)
            self.receipt_text_data.append('{} {}'.format(*each_line))

        self.footer = _combine_all_images_vertically(bag)

    def generate_resulted_image(self):
        self.final_output_image = _combine_all_images_vertically(
            [
                self.image_whitespace_sep,
                self.header,
                self.image_whitespace_sep,
                self.image_line_sep,
                self.body,
                self.image_line_sep,
                self.footer,
                self.image_line_sep,
                self.image_whitespace_sep,
            ]
        )
        return self.final_output_image
