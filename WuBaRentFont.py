# @Time    : 2019/3/15 19:11
# @Author  : SuanCaiYu
# @File    : WuBaRentFont.py
# @Software: PyCharm
import base64
from tempfile import TemporaryFile

from fontTools.ttLib import TTFont

from Exceptions import ValueIsNoneException, MapIsNoneException


class ParseXml:

    def __init__(self, base64_string=None, font_file_path=None):
        """
        解析父类
        :param base64_string: 字体文件得 base64 字符串
        :param font_file_path: 字体文件路径
        """
        self._base64_string = base64_string
        self._font_file_path = font_file_path

    def parse_ttf_map(self, cmap):
        ttf_map = {}
        for k, v in cmap.items():
            ttf_map[hex(k).replace('0x', '')] = v
        return ttf_map


class ParseFontFile(ParseXml):

    def parse_font_file(self, font_file_handler=None):
        """
        解析字体文件
        :param font_file_handler: 打开的字体文件句柄
        :return: 字体cmap 映射字典
        """
        if font_file_handler:
            font = TTFont(file=font_file_handler)
        elif self._font_file_path:
            font = TTFont(self._font_file_path)
        else:
            raise ValueIsNoneException('font_file_path or font_file_handler')
        cmap = font.getBestCmap()
        return self.parse_ttf_map(cmap)


class ParseBase64(ParseFontFile):

    def parse_base64(self):
        """
        解析base64字符串为文件，并交由字体文件解析器解析
        :return: 字体cmap 映射字典
        """
        if not self._base64_string:
            raise ValueIsNoneException('base64_string')
        content = base64.b64decode(self._base64_string)
        fp = TemporaryFile()
        fp.write(content)
        return self.parse_font_file(fp)


class RentFont:

    def __init__(self, base64_string=None, font_file_path=None, font_file_handler=None):
        self.__ttf_map = None
        self.base64_string = base64_string
        self.font_file_path = font_file_path
        self.font_file_handler = font_file_handler
        self.__num_map = {
            'glyph00001': '0',
            'glyph00002': '1',
            'glyph00003': '2',
            'glyph00004': '3',
            'glyph00005': '4',
            'glyph00006': '5',
            'glyph00007': '6',
            'glyph00008': '7',
            'glyph00009': '8',
            'glyph00010': '9',
        }

    def __setattr__(self, key, value):
        self.__parse_ttf_map(key, value)
        self.__dict__[key] = value

    def __parse_ttf_map(self, key, val):
        if key == 'base64_string' and val:
            base64_parse = ParseBase64(base64_string=val)
            self.__ttf_map = base64_parse.parse_base64()
        elif key == 'font_file_path' and val:
            font_file_parse = ParseFontFile(font_file_path=val)
            self.__ttf_map = font_file_parse.parse_font_file()
        elif key == 'font_file_handler' and val:
            font_file_parse = ParseFontFile()
            self.__ttf_map = font_file_parse.parse_font_file(font_file_handler=val)

    def get_val(self, confuse_num):
        """
        获取混淆字符对应的数字
        :param confuse_num: 网页源码里混淆的字符
        :return:
        """
        if not self.__ttf_map:
            raise MapIsNoneException('ttf_map')
        vals = confuse_num.split(';')
        vals = [x.replace('&#x', '') for x in vals if x]
        result = "".join([self.__num_map.get(self.__ttf_map.get(val)) for val in vals])
        return result
