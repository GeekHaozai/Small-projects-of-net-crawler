import requests
from urllib.parse import urlparse, parse_qs
import json
import csv

#原本正常运行
def get_and_save(cookie, param_url):
    api_url = "https://api.youshu.youcloud.com/graphql"
    headers = {
        "X-Operation-Name": "getProductList",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": cookie
    }
    query = """

                query getProductList (
                    $unitId: String
                    $shopId: String
                    $sellerCompanyId: String
                    $sloganDigest: String
                    $keyword: String
                    $site_id: String
                    $category: String
                    $promotionType: String
                    $shopType: String
                    $hasBrand: String
                    $isNew: Boolean
                    $startDate: String
                    $endDate: String
                    $min_price: String
                    $max_price: String
                    $min_qs_incr_24h: String
                    $max_qs_incr_24h: String
                    $min_qs_incr_12h: String
                    $max_qs_incr_12h: String
                    $min_qs_incr_6h: String
                    $max_qs_incr_6h: String
                    $min_qs_total: String
                    $max_qs_total: String
                    $min_qs_total_amount: String
                    $max_qs_total_amount: String
                    $min_comment_count: String
                    $max_comment_count: String
                    $min_applause_rate: String
                    $max_applause_rate: String
                    $min_qs_incr_day: String
                    $max_qs_incr_day: String
                    $min_qs_incr_amount_day: String
                    $max_qs_incr_amount_day: String
                    $sort: ProductListSort!
                    $page: Int!
                    $min_measure: String
                    $max_measure: String
                    $trend: String
                    $startMonitor: String
                    $endMonitor: String
                    $isExport: Boolean!
                    $isExact: Boolean
                    $product_id_lst: [String]
                ) {
                    productList (
                        unitId: $unitId
                        shopId: $shopId
                        company_id: $sellerCompanyId
                        sloganDigest: $sloganDigest
                        keyword: $keyword
                        site_id: $site_id
                        category: $category
                        promotionType: $promotionType
                        shopType: $shopType
                        hasBrand: $hasBrand
                        isNew: $isNew
                        startDate: $startDate
                        endDate: $endDate
                        min_price: $min_price
                        max_price: $max_price
                        min_qs_incr_24h: $min_qs_incr_24h
                        max_qs_incr_24h: $max_qs_incr_24h
                        min_qs_incr_12h: $min_qs_incr_12h
                        max_qs_incr_12h: $max_qs_incr_12h
                        min_qs_incr_6h: $min_qs_incr_6h
                        max_qs_incr_6h: $max_qs_incr_6h
                        min_qs_total: $min_qs_total
                        max_qs_total: $max_qs_total
                        min_qs_total_amount: $min_qs_total_amount
                        max_qs_total_amount: $max_qs_total_amount
                        min_comment_count: $min_comment_count
                        max_comment_count: $max_comment_count
                        min_applause_rate: $min_applause_rate
                        max_applause_rate: $max_applause_rate
                        min_qs_incr_day: $min_qs_incr_day
                        max_qs_incr_day: $max_qs_incr_day
                        min_qs_incr_amount_day: $min_qs_incr_amount_day
                        max_qs_incr_amount_day: $max_qs_incr_amount_day
                        sort: $sort
                        page: $page
                        min_measure: $min_measure
                        max_measure: $max_measure
                        trend: $trend
                        startMonitor: $startMonitor
                        endMonitor: $endMonitor
                        isExport: $isExport
                        isExact: $isExact
                        product_id_lst: $product_id_lst
                    ) {

            data {
                product {

        id @skip(if: $isExport)
        category @skip(if: $isExport) {

        id
        name

        }
        header_image @skip(if: $isExport) {

        path

        }
        url
        title
        price
        site {

        id
        name
        icon

        }
        shop {

        id
        name
        qualification_url
        dsr

            has_brand
            talent {

        uid
        avatar_url
        nickname

                track_url
            }
        }
        seller_company {

        id
        screenName

        }
        first_monitor_time
        modify_time
        isNew @skip(if: $isExport)

                }
                promotionType {

        id
        name
        shortName

                }
                qs_incr_24h
                qs_incr_24h_ratio
                qs_total
                highlight

                measureValue
                qs_incr
                qs_amount_incr
                comment_count
                applause_rate

            }
            maxTotal
            page
            total
            limit

                    }
                }

    """

    # variables = {
    #         "endDate": "2023-08-12",
    #         "isExact": False,
    #         "isExport": False,
    #         "isNew": False,
    #         "page": 2,
    #         "sort": "qs_incr_amount_xday",
    #         "startDate": "2023-08-06"
    #     }
    variables = url_to_variable(param_url)
    variables['isExport'] = False

    data = {
        "operationName": "getProductList",
        "query": query,
        "variables": variables
    }
    print(variables)

    response = requests.post(api_url, json=data, headers=headers)
    response.encoding = "utf-8"
    print(response.text)
    result = response.json()

    limit = result["data"]["productList"]["limit"]
    total = result["data"]["productList"]["total"]
    total_page = total // limit if (total % limit) == 0 else total // limit + 1
    with open("数据.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["商品", "价格", "新增销量", "24h新增销量", "24h新增销量百分比", "链接", "抖音链接", "快手链接"])

    for i in range(1, total_page + 1):
        print(i)
        variables["page"] = i
        each_response = requests.post(api_url, json=data, headers=headers)
        each_response.encoding = "utf-8"
        each_result = each_response.json()
        each_products = each_result["data"]["productList"]["data"]
        for product in each_products:
            # product = products[0]
            title = product["product"]["title"]
            price = product["product"]["price"]
            new_increse = product["qs_incr"]
            day_new_increase = product["qs_incr_24h"]
            ratio = product["qs_incr_24h_ratio"]
            product_url = product["product"]["url"]
            goto_url = requests.utils.unquote(product_url.split("goto=")[1])

            # douyin_url = douyin(goto_url)
            # kuaishou_url = kuaishou(goto_url)

            douyin_url = "待测试"
            kuaishou_url = "待测试"

            info = {
                "商品": title,
                "价格": price,
                "新增销量": new_increse,
                "24h新增销量": day_new_increase,
                "24h新增销量百分比": ratio,
                "链接": goto_url,
                "抖音链接": douyin_url,
                "快手链接": kuaishou_url,
            }

            print("[INFO]:", info)
            with open("数据.csv", "a", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [title, price, new_increse, day_new_increase, ratio, goto_url, douyin_url, kuaishou_url])


def url_to_variable(url):
    url = requests.utils.unquote(url)
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    params_dict = {
        "isNew": False,
        "page": 1,
        "sort": "qs_incr_amount_xday",
        "isExact": False
    }
    for key, value in query_params.items():
        # Since parse_qs returns a list for each parameter, we only take the first value
        if value[0] == 'false':
            value[0] = False
        if value[0] == 'true':
            value[0] = True
        params_dict[key] = value[0]
    if 'tableSelect' in params_dict:
        del params_dict['tableSelect']
    if 'timeType' in params_dict:
        del params_dict['timeType']
    if 'daterange' in params_dict:
        del params_dict['daterange']
    params_dict['page'] = 1
    if 'extraFilter' in params_dict:
        extra_dic = json.loads(params_dict["extraFilter"])
        for key in extra_dic:
            extra_key = key
            extra_value = extra_dic[key]
        del params_dict['extraFilter']
        match extra_value[0]:
            case "range":
                max_key = "max_" + str(extra_key)
                params_dict[max_key] = str(extra_value[1][1])
                min_key = "min_" + str(extra_key)
                params_dict[min_key] = str(extra_value[1][0])
            case "gte":
                min_key = "min_" + str(extra_key)
                params_dict[min_key] = str(extra_value[1][0])
            case "lte":
                max_key = "max_" + str(extra_key)
                params_dict[max_key] = str(extra_value[1][0])
    if 'measure' in params_dict:
        max_measure = params_dict["measure"].split(",")[1]
        min_measure = params_dict["measure"].split(",")[0]
        if max_measure:
            params_dict["max_measure"] = max_measure
        if min_measure:
            params_dict["min_measure"] = min_measure
    return params_dict


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
        # print("没有url但有detail_url")
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
        # print("没有url但有detail_url")
        detail_url = url_data["data"][0]["detail_url"]
    else:
        return "没有找到对应快手链接"
    true_url = "https://haohuo.jinritemai.com/views/product/detail?" + str(detail_url.split("?")[1])
    return true_url


if __name__ == '__main__':
    cookie = "_ga=GA1.1.1712430838.1691671940; MEIQIA_TRACK_ID=2TnGvoqEB5qZSGmtp1snN9vPdwz; localeLanguage=zh; MEIQIA_VISIT_ID=2TnGvqYUTQezHfJhTrlpt4Tk1MU; sessionId=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJqdGkiOiI1MU44NTM4NDAyNjBBNjRkOGFhY2QwOWVkOSIsImV4cCI6MTY5MjUyNTkwMSwic3ViIjoiODgyMjY4In0.v7em2k1lno8J8QbP3drNmnLJTN1aQNO4HFgj77UmSc8lTdf69uCeivvBfMBuu06gi4PM6G0F8ahUNl-T6SA_2w; _ga_QNB91PL4C6=GS1.1.1691921096.2.0.1691921101.0.0.0; ph_oEY7uwNI-BrLK7aN1Al8D1-abXKFEeENlm9zn5gOvzM_posthog=%7B%22distinct_id%22%3A%22882268%22%2C%22%24device_id%22%3A%22189df7d0fbed6c-075464a9f5060b-26031c51-144000-189df7d0fbffc9%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22%24referrer%22%3A%22https%3A%2F%2Fauth.youcloud.com%2Flogin%3Fapp_id%3Dyoushu%26goto%3Dhttps%253A%252F%252Fconsole.youshu.youcloud.com%252Fgoods%252Fsale%22%2C%22%24referring_domain%22%3A%22auth.youcloud.com%22%2C%22app_release%22%3A%22v2.2.2-youshu%22%2C%22language%22%3A%22zh-CN%22%2C%22document_lang%22%3A%22zh-CN%22%2C%22%24session_recording_enabled%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24user_id%22%3A%22882268%22%7D; _ga_SFG2Z62L10=GS1.1.1691921091.4.1.1691921104.0.0.0"
    param_url = "https://console.youshu.youcloud.com/goods/sale?startDate=2023-08-07&endDate=2023-08-13&daterange=-6,0"
    get_and_save(cookie, param_url)
