# @Time    : 2019/3/15 20:04
# @Author  : SuanCaiYu
# @File    : font_file_example.py
# @Software: PyCharm

from WuBaRentFont import RentFont

if __name__ == '__main__':
    # example 1 file path
    example1_rent_font = RentFont(font_file_path='./test_font.ttf')
    # example1_rent_font.font_file_path = './test_font.ttf'
    result = example1_rent_font.get_val('&#x9fa4;&#x9fa4;&#x958f;&#x9f92;')
    print(result)

    # example 2 file handler
    example2_rent_font = RentFont()
    with open('./test_font.ttf', 'rb') as fp:
        # example2_rent_font = RentFont(font_file_handler=fp)
        example1_rent_font.font_file_handler = fp
    result = example1_rent_font.get_val('&#x9fa4;&#x9fa4;&#x958f;&#x9f92;')
    print(result)
