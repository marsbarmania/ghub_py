# -*- coding: utf-8 -*-
import sys

class MyCode(object):
  # リストを２つ用意
  base = []
  sorted = []
  # 出力用インデックス
  start = 0
  end = 0

  # ファイル読み込み、base/sortedにセットする
  def push_to_list(self,filepath):
    with open(filepath) as f:
      for line in f:
        self.base.append(int(line.rstrip()))
        self.sorted.append(int(line.rstrip()))

  # 出力する関数
  def range_output(self):
    self.ins_sort()

    if(self.base != self.sorted):
      # 開始位置を検索
      num = 0
      while(self.base[num] == self.sorted[num]):
        num += 1
      self.start = num + 1

      # 醜虜位置を検索
      num = len(self.sorted) - 1
      while(self.base[num] == self.sorted[num]):
        num -= 1
      self.end = num +1

      # 結果の出力
      print("%d..%d" % (self.start, self.end))
    else:
      # 結果の出力
      print(0)


  # 挿入ソートする
  def ins_sort(self):
    # 左端からソート
    for n in range(1, len(self.sorted)):
      val = self.sorted[n]
      i = n -1
      # 挿入ソートの入れ替え処理部分
      while (i >= 0) and (self.sorted[i] > val):
        # 値の入れ替え
        self.sorted[i+1] = self.sorted[i]
        i = i - 1
      self.sorted[i+1] = val

  def current_py_version(self):
    print("The Python version is %s.%s.%s" % sys.version_info[:3])

# 実行例
me = MyCode()
me.current_py_version()
me.push_to_list("./sort/input_case_5.txt")
me.range_output()

