# @Time    : 2019/3/15 19:31
# @Author  : SuanCaiYu
# @File    : Exceptions.py
# @Software: PyCharm


class ValueIsNoneException(Exception):

    def __init__(self, value, error_info=None):
        super().__init__(self)
        self.err_info = error_info
        self.value = value
        if not self.err_info:
            self.err_info = 'Cannot be None'

    def __str__(self):
        return "%s %s" % (self.value, self.err_info)


class MapIsNoneException(Exception):
    def __init__(self, val, error_info=None):
        super().__init__(self)
        self.err_info = error_info
        self.value = val
        if not self.err_info:
            self.err_info = '请指定base64_string或font_file_path，用以获得字体映射map'

    def __str__(self):
        return "%s %s" % (self.value, self.err_info)
