# _*_ coding : utf-8 _*_


import requests

r = requests.get(url='http://1.202.247.200/netreport/reportInfor/reportInfor?ar'
                 'eaPath=%25E6%25B9%2596%25E5%258C%2597%25E7%259C%2581%25E9%25B'
                 'B%2584%25E5%2586%2588%25E5%25B8%2582%25E6%25B5%25A0%25E6%25B0'
                 '%25B4%25E5%258E%25BF&city=%25E9%25BB%2584%25E5%2586%2588%25E5'
                 '%25B8%2582')

print(r.status_code)
r.encoding = 'utf-8'
print r.url
print(r.text), "\n"
#print r.json(), "nihao"
