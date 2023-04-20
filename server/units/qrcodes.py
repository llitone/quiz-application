import os
import qrcode

from typing import Tuple, Any


class QRCodeGenerator(object):
    DIR = False

    def __init__(
            self, bg: Tuple[int, int, int] = (255, 255, 255),
            fill_color: Tuple[int, int, int] = (0, 0, 0)
    ):
        if os.path.isdir(".qr"):
            self.__change_dir()
        self.bg = bg
        self.fill_color = fill_color
        self.qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
        self._img: Any = None


    def save(self, filename: str):
        if isinstance(self._img, type(None)):
            raise TypeError("self.img must be None. run .make(url)")
        if self.DIR:
            filename = ".qr/" + filename
        self._img.save(filename)

    def make(self, url: str):
        self.qr.add_data(url)
        self.qr.make()
        self._img = self.qr.make_image(fill_color=self.fill_color, back_color=self.bg)

    def mkdir(self):
        if not os.path.isdir(".qr"):
            os.mkdir(".qr")
            self.__change_dir()

    @classmethod
    def __change_dir(cls):
        cls.DIR = not cls.DIR
