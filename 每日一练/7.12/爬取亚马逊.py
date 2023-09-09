import requests
import re

# def change_location():
#     url = "https://www.amazon.com/portal-migration/hz/glow/address-change?actionSource=glow"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
#
#     }
#     data = {
#         "actionSource": "glow",
#         "deviceType": "web",
#         "locationType": "LOCATION_INPUT",
#         "pageType": "Detail",
#         "storeContext": "toys-and-games",
#         "zipCode": "10041"}
#     res = requests.post(url,data=data,headers=headers)
#     print(res.status_code)
def get_html(ASIN):
    base_url = "https://www.amazon.com/dp/"
    url = base_url+str(ASIN)
    headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
                "Cookie":'session-id=147-7678205-5139461; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=132-9785529-4303326; session-token="MG3AN/B9qA7HMWy4p5ml4oTDp6lqq9L37dSKtDQ+iz7EBDL3QO2/sJRxDu+b2mWx0gyhV+0KcuC727nLVIsbJN3jLbPx4qTDjhk50ejCDfo6Ikzf3Hy11sEbd7CWAAZbjLyyCpnMTy28QQfK+Wd/PkRQV6LvBsKg702owvjly52DNn/N6QIUkW3q/TPEWGwNO4tsbjUpuaG49JQRaDqNfXGGcRphnyL4raKYCl9S8EU="; csm-hit=tb:Z81HSVB11N2P928G3CXX+s-',
                'Referer':'https://www.amazon.com/dp/B09CDB63M4?th=1'
        }
    data = {
                "actionSource": "glow",
                "deviceType": "web",
                "locationType": "LOCATION_INPUT",
                "pageType": "Detail",
                "storeContext": "toys-and-games",
                "zipCode": "10041"}
    session = requests.session()
    r = session.post("https://www.amazon.com/portal-migration/hz/glow/address-change?actionSource=glow",headers=headers,data=data)
    r2 = session.get(url,headers=headers)
    coupon = re.compile("Coupon:")
    res = coupon.findall(r2.text)
    pos = re.compile("New York 10041")
    res1 = pos.findall(r.text)
    print(r2.text)

get_html("B09CDB63M4")
# headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
#         "Cookie":'session-id=147-7678205-5139461; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=132-9785529-4303326; session-token="MG3AN/B9qA7HMWy4p5ml4oTDp6lqq9L37dSKtDQ+iz7EBDL3QO2/sJRxDu+b2mWx0gyhV+0KcuC727nLVIsbJN3jLbPx4qTDjhk50ejCDfo6Ikzf3Hy11sEbd7CWAAZbjLyyCpnMTy28QQfK+Wd/PkRQV6LvBsKg702owvjly52DNn/N6QIUkW3q/TPEWGwNO4tsbjUpuaG49JQRaDqNfXGGcRphnyL4raKYCl9S8EU="; csm-hit=tb:Z81HSVB11N2P928G3CXX+s-',
#         'Referer':'https://www.amazon.com/dp/B09CDB63M4?th=1'
# }
# data = {
#                 "actionSource": "glow",
#                 "deviceType": "web",
#                 "locationType": "LOCATION_INPUT",
#                 "pageType": "Detail",
#                 "storeContext": "toys-and-games",
#                 "zipCode": "10041"
# }
# session = requests.session()
# r = requests.post("https://www.amazon.com/portal-migration/hz/glow/address-change?actionSource=glow",data=data,headers=headers)
# print(r.text)

#该项目被反爬而告终~哎