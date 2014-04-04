# CSVファイルを使って、人口の増加が全国平均よりも上昇傾向にある都道府県をすべて答えてください。
# -*- coding: utf-8 -*-
import csv, sys

# データを読込むメソッド：
# CSVファイルはUTF-8に変換しておく
def survey_data(filename):
  d = {}
  with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
      for row in reader:
        # 必要な部分から読み込みます。
        if reader.line_num >= 13:
          # Dictionaryに都道府県名をkeyにリストを追加
          d[row[0]] = (float(row[1]) / float(row[-1]))*100
    except csv.Error, e:
      sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

  return d

def print_pref_names(dic):
  # 全国の平均値
  average_value = dic['全　　　国']

  for pref,val in dic.iteritems():
    if val > average_value:
      print pref


print_pref_names(survey_data("mi040001.csv"))

