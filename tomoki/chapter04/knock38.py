#NO38(ヒストグラム)
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
result = []
sentence = []
with open("neko.txt.mecab") as f:
  for line in f:
    l1 = line.split("\t")
    if len(l1) == 2:
      l2 = l1[1].split(",")
    #list out of rangeを防ぐ(エラーが起きたときは、基本形に表層形を利用する)
      try:
        #l1は表層形のみを含む　l2は[0:品詞 1:品詞細分類1・・・のようになっている]
        sentence.append({"surface": l1[0], "base": l2[7], "pos": l2[0], "pos1": l2[1]})
      except IndexError:
        sentence.append({"surface": l1[0], "base": l1[0], "pos": l2[0], "pos1": l2[1]})

      if l2[1] == "句点":
        result.append(sentence)
        sentence = []
result
text2 = []
#resultはネスト(listのなかにdictという多重構造)になっているため、2回for文を回す必用がある。
for lis in result:
  for dic in lis:
    #""以外の時、リストに追加する
    if dic["surface"] != "":
      text2.append(dic["surface"])
 
count = Counter(text2)
#*を忘れずに(今回は２つの値[文字:文字の数]が入っている)
target, counts= zip(*count.most_common())
#Figure 描画領域全体
#Axes 描画領域の中のグラフ(一つ一つのプロットを描く領域（座標軸）)
#subplotsの引数を省略すると、サブプロットが１つだけ生成される(ex ２×３個のサブプロットを作成をする場合　(2,3))
fig, ax = plt.subplots()
ax.hist(counts, range=(1, 10))
#ラベルをつけると分かりやすくなる
plt.xlabel("出現頻度")
plt.ylabel("種類数")
#tkinterのinstallをするとplt.show()がうまく利用できる
plt.show()