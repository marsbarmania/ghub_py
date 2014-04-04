# -*- coding: utf-8 -*-
def ja2enCountryName(name):
    en_name = ''
    if name == '日本':
        en_name = 'Japan'
    elif name == '米国':
        en_name = 'America'
    elif name == '英国':
        en_name = 'Britain'
    elif name == '仏国':
        en_name = 'France'
    elif name == '露国':
        en_name = 'Russia'
    elif name == '中国':
        en_name = 'China'

    # 省略…

    else:
        en_name = '?'
    return en_name

print(ja2enCountryName('日本'))
print(ja2enCountryName('米国'))
print(ja2enCountryName('英国'))
print(ja2enCountryName('仏国'))
