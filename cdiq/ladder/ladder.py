# -*- coding: utf-8 -*-
# Version Python 2.7.2
import random

class Ladder(object):
  # 各線の位置を格納するDictionaryデータ
  route_map = {}
  # 線間のデータ
  spans = ['AB','BC','CD']

  ###################################################
  # コンストラクタ
  ###################################################
  def __init__(self,atari):
    """ アタリを設定 """
    self.atari = atari
    """ アタリに基づいてくじを作成 """
    self.make_kuji_map()
    """ アタリスタートポイントを設定 """
    next_point = self.route_map['line4'].strip(self.atari.upper())
    self.start_to_atari = self.set_atari_value('line4',next_point)

  ###################################################
  # 再帰的にアタリルートを探り、アタリスタート値を返すメソッド
  ###################################################
  def set_atari_value(self,line_start,next):
    """ スパン文字(AB,BC,CD)から次のポイントを割り出す """
    next_excluded = [i for i in self.route_map if self.route_map[i].find(next)!=-1 ]
    result = filter(lambda x: x < line_start, next_excluded)
    """
      結果から、0の場合、1の場合はスパン文字(AB,BC,CD)からアタリスタートがわかる
      それ以外は再帰的に同処理をする
    """
    if len(result) == 0:
      return next
    elif len(result) == 1:
      return self.route_map[result[0]].strip(next)
    else:
      return self.set_atari_value(result[0],self.route_map[result[0]].strip(next))

  ###################################################
  # あみだくじの横線を[AB BC CD]どれかに配置するメソッド
  # （4本なのでループなしで実装してしまう）
  ###################################################
  def make_kuji_map(self):
    """ 線4のスパン """
    self.route_map['line4'] = self.last_step_position(self.atari)

    """ 線1：ランダム選択にきめる """
    self.route_map['line1'] = random.choice(self.spans)

    """ 線2 """
    if self.route_map['line1']==self.route_map['line4']:
      others = filter(lambda x: x != self.route_map['line1'], self.spans)
      self.route_map['line2'] = random.choice(others)
    else:
      self.route_map['line2'] = random.choice(self.spans)

    """ 線3 """
    if self.route_map['line1']==self.route_map['line4']:
      self.route_map['line3'] = filter(lambda y: y != self.route_map['line2'],
        filter(lambda x: x != self.route_map['line1'], self.spans))[0]
    else:
      if self.route_map['line1']==self.route_map['line2'] or self.route_map['line2']==self.route_map['line4']:
        for val in self.spans:
          if not val in self.route_map.values():
            self.route_map['line3'] = val
      else:
        self.route_map['line3'] = random.choice(self.spans)

  ###################################################
  # アタリ値から４番目の線の配置される線間を決めるメソッド
  ###################################################
  def last_step_position(self,atari):
    return {
      'a': 'AB',
      'b': random.choice(['AB','BC']),
      'c': random.choice(['BC','CD']),
      'd': 'CD'
    }[atari]

  ###################################################
  # 引数がアタリかどうかの判定メソッド
  ###################################################
  def is_atari(self,str):
    return True if str.upper() == self.start_to_atari else False


# Test
lad = Ladder(random.choice('abcd'))
# print(lad.route_map)
# print('atari=> '+lad.atari+' point=> '+lad.start_to_atari)
# print(lad.is_atari(random.choice(['A','B','C','D'])))

