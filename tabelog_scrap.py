import requests
import lxml.html
import re
from bs4 import BeautifulSoup

#コメント
#数値
#エクセルファイルに出力


url = "https://tabelog.com/tokyo/A1305/A130504/R10705/rstLst/?select_sort_flg=1"
#次の20件を押した先にあるリンク
#https://tabelog.com/tokyo/A1305/A130504/R10705/rstLst/2/?select_sort_flg=1
#ここを動的に動かす。
#注意するときは終わる時。どういう挙動を起こすかが大事。
#tryexept,if文

#URLにリクエストを送りHTMLを取得
#相手のサーバーにリクエストを送ってレスポンスをゲットしちゃう。
response = requests.get(url)
#レスポンスからオブジェクトを作成
#parser=わかりにくい情報をわかりやすく簡単な構造にしてくれるよ
soup = BeautifulSoup(response.content, "html.parser")

"""
url_review = 
soup2 = BeautifulSoup(response.content, "html.parser")
"""



store_names = soup.find_all("h4", class_="list-rst__rst-name")
for store_name in store_names:
    print(store_name.getText())

rates = soup.find_all("span", class_="list-rst__rating-val")
for rate in rates:
    print(rate.text)

reviews = soup.find_all("a", class_="list-rst__rvw-count-target")
for review in reviews:
    print(review.text)

review_links = soup.find_all("a", class_="list-rst__rvw-count-target")
for review_link in review_links:
    print(review_link.attrs['href'])

#レビューページのリスト化、これに何の意味があるのかは謎、まあこれでfor文かけやすくなるのかな？
#review_links = [review_link.attrs['href'] for review_link in review_links]
#print(review_links)















#コメントの件数のリンク
<a class="list-rst__rvw-count-target" data-url="https://tabelog.com/tokyo/A1305/A130504/13010869/dtlrvwlst/" data-rd-pos="rvcnt" data-list-dest="item_rvw_list" href="https://tabelog.com/tokyo/A1305/A130504/13010869/dtlrvwlst/"><em class="list-rst__rvw-count-num cpy-review-count">12</em>件</a>

<a class="list-rst__rvw-count-target" data-url="https://tabelog.com/tokyo/A1305/A130504/13010870/dtlrvwlst/" data-rd-pos="rvcnt" data-list-dest="item_rvw_list" href="https://tabelog.com/tokyo/A1305/A130504/13010870/dtlrvwlst/"><em class="list-rst__rvw-count-num cpy-review-count">139</em>件</a>







#<a class="list-rst__rst-name-target cpy-rst-name" target="_blank" data-list-dest="item_top" href="https://tabelog.com/tokyo/A1305/A130504/13204540/">きなり</a>


#<a class="list-rst__rst-name-target cpy-rst-name" target="_blank" data-list-dest="item_top" href="https://tabelog.com/tokyo/A1305/A130504/13220654/">京料理 たん熊北店 Directed by M.Kurisu</a>log

#<a href="https://tabelog.com/tokyo/A1305/A130504/R10705/rstLst/2/?select_sort_flg=1" class="c-pagination__num">2</a>

#<a href="https://tabelog.com/tokyo/A1305/A130504/R10705/rstLst/3/?select_sort_flg=1" class="c-pagination__num">3</a>
#rstLst以降の数字が違うだけ
#次のページも見てみる

#<a href="https://tabelog.com/tokyo/A1305/A130504/R10705/rstLst/1/?select_sort_flg=1" class="c-pagination__num">1</a>