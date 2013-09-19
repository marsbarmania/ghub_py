def insertion_sort(arry):
  # 大きなループは要素数と同値なのでforでまわす
  for j in range(1, len(arry)):
    # 隣の値を変数に格納する
    next_val = arry[j]
    # 現在の値のindex値
    i = j - 1
    # indexが０以上でかつ次の値より大きいときに入れ替えする
    # その処理をすべての値に対して行う
    while (i >= 0) and (arry[i] > next_val):
      # 入れ替え処理
      arry[i+1] = arry[i]
      # indexを戻す
      i = i - 1
    arry[i+1] = next_val
