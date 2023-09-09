import re
import requests
url = "https://haohuo.jinritemai.com/ecommerce/trade/detail/index.html?id=3632065023494484598"

id = re.search("id=(\d+)&{0,1}", url).group(1)

print(id)


def get_detail_info(id,platform):
    params = {
        "product_id":id,
        "platform":platform
    }
    detail_api = "https://www.reduxingtui.com/api/douke/view"
    resu = requests.get(detail_api,params=params)
    json_resu = resu.json()
    if json_resu["status"] != 200:
        return ['因商家调整，该商品暂无法购买',"","","","","",""]
    kol_cos_ratio = json_resu["data"]["kol_cos_ratio"]
    convert_url = json_resu["data"]["url"]
    leiji_sales = json_resu["data"]["sales"]
    tuiguang = json_resu["data"]["kol_num"]
    day_sales = json_resu["data"]["sales_24"]
    week_dingdan = json_resu["data"]["order_week"]
    month_dingdan = json_resu["data"]["order_num"]

    return [convert_url,kol_cos_ratio,leiji_sales,tuiguang,day_sales,week_dingdan,month_dingdan]

douyin = get_detail_info(3607946595393472767,"douyin")
print(douyin)
kuaishou = get_detail_info(3632065023494484598,"kuaishou")
print(kuaishou)


def douyin(url):
    params = {
        "page": 1,
        "title": url,
        "platform": "douyin",
    }
    url_data = requests.get("https://www.reduxingtui.com/api/douke/search", params=params).json()
    if not url_data["data"]:
        return "没有找到对应抖音链接"
    if "url" in url_data["data"][0]:
        detail_url = url_data["data"][0]["url"]
    elif "detail_url" in url_data["data"][0]:
        # #print("没有url但有detail_url")
        detail_url = url_data["data"][0]["detail_url"]
    else:
        return "没有找到对应抖音链接"
    true_url = "https://haohuo.jinritemai.com/views/product/detail?" + str(detail_url.split("?")[1])
    return true_url


def kuaishou(url):
    params = {
        "page": 1,
        "title": url,
        "platform": "kuaishou",
    }
    url_data = requests.get("https://www.reduxingtui.com/api/douke/search", params=params).json()
    if not url_data["data"]:
        return "没有找到对应快手链接"
    if "url" in url_data["data"][0]:
        detail_url = url_data["data"][0]["url"]
    elif "detail_url" in url_data["data"][0]:
        # #print("没有url但有detail_url")
        detail_url = url_data["data"][0]["detail_url"]
    else:
        return "没有找到对应快手链接"
    true_url = "https://haohuo.jinritemai.com/views/product/detail?" + str(detail_url.split("?")[1])
    return true_url