#coding:utf-8
import csv

class Katayan(object):

  # コンストラクタ
  def __init__(self, wordList=None):
    # 一致した文字要素のタプル格納用リスト
    self.answer = []
    # 文字リストをリストデータにするためのリスト
    # ２次元リストで位置を設定する
    if wordList is None:
      self.wordList = []
    else:
      self.wordList = wordList

  # ファイルを詠込みリストデータに変換する
  def set_wordbox(self,filepath):
    with open(filepath,'r') as f:
      for row in csv.reader(f):
        self.wordList.append(row)

  # 与えられた文字列の文字を収集する
  def collect_letters(self,text):
    for ch in text:
      self.find_pos(ch)

  # 各文字の位置を見つけて、検索済みとする
  def find_pos(self,ch):
    stop = False
    for x,lisst in enumerate(self.wordList):
      for y,val in enumerate(lisst):
        if val==ch:
          # タプルデータとしてリストに格納
          self.answer.append((x+1,y+1))
          # 検索済みとして、-1をいれてしまう
          self.wordList[x][y] = -1
          stop = True
          break
      # 見つかった時点でループ処理はしない
      if stop:
        break

  def output(self):
    for tup in self.answer:
      print(str(tup)[1:-1])



# 実際の使い方
s = "STAY HUNGRY, STAY FOOLISH"
kata = Katayan()
kata.set_wordbox('./gutenberg/gutenberg.csv')
kata.collect_letters(s)
kata.output()
