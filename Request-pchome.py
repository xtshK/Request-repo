import requests

res =requests.get('https://24h.pchome.com.tw/search/?q=viewsonic&scope=all&sortParm=rnk&sortOrder=dc&cateId=DSABEX')

print(res.text)