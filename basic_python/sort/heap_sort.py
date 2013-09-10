import math

def heap_sort(heap):
   # 末尾の位置を2で割ったsize/2が末尾の親になる
  num = math.floor(len(heap)/2)+1
  # heapを構築する
  for i in range(num)[::-1]: down_heap(heap,i,len(heap)-1)
  # ヒープ構造にする
  print(heap)

  num = len(heap)
  # Pythonのrangeの範囲に注意
  for i in range(num)[::-1]:
    # tmpに最後尾を代入する
    tmp = heap[i]
    # ルートノード（最大値）をはずし、現在の最後尾と入れ替え
    heap[i] = heap[0]
    heap[0] = tmp
    # ヒープを再構築する
    down_heap(heap,0,i-1)
    print(heap)

def down_heap(heap,p,n):
  # pが親のインデックスで左の子のインデックスをきめる
  c = p * 2
  # 子のインデックス（c）がヒープ最後尾インデックスより大きい場合は終了
  if c > n:
    return
  # 右の子が存在しかつ左の子の値より大きい場合
  if c+1 <= n and heap[c+1] > heap[c]:
    # 右の子のインデックスを左の子インデックスとする
    c += 1

  # 親の値の方が子の値より小さい場合は、値を入れ替え
  # 再帰的に入れ替え処理を行う
  if heap[p] < heap[c]:
    tmp = heap[p]
    heap[p] = heap[c]
    heap[c] = tmp
    down_heap(heap,c,n)



h1 = [5, 1, 3, 6, 7, 8, 9, 0, 2, 4]
h2 = [3, 2, 5, 6, 1, 7, 4, 9, 0, 8]
h3 = [3, 2, 5, 6, 1]

heap_sort(h1)

