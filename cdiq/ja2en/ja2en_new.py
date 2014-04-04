# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 解答の関数
def ja2enCountryName(name):
  # 関数の本体、解答を記述する部分
  origin = name
  table = {'日本':'Japan',
            '米国':'America',
            '英国':'Britain',
            '仏国':'France',
            '露国':'Russia',
            '中国':'China'
  }
  
  for k, v in table.items():
      name = name.replace(k,v)
  name = table.has_key(origin) and name or '?'
  return name
#
# print("The Python version is %s.%s.%s" % sys.version_info[:3])
# print(ja2enCountryName('日本'))

for name in ['日本','米国', '英国', '仏国', '露国', '中国', '宇宙']:
  print(ja2enCountryName(name))
