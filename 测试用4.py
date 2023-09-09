import requests
import aiofiles
import aiohttp
import asyncio
from datetime import timedelta
import datetime

tasks = []
async def get_info(company,start,end):
    # url = "https://twitter.com/i/api/graphql/3Ej-6N7xXONuEp5eJa1TdQ/SearchTimeline?variables=%7B%22rawQuery%22%3A%22SES%20AI%20Corp%20until%3A2015-01-04%20since%3A2015-01-03%22%2C%22count%22%3A20%2C%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22Top%22%7D&features=%7B%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Afalse%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
    url = "https://twitter.com/i/api/graphql/3Ej-6N7xXONuEp5eJa1TdQ/SearchTimeline"
    query_params = {
        "variables": "{" + f'"rawQuery":"{company} until:{end} since:{start}","count":20,"querySource":"typed_query","product":"Top"' + "}"
    }
    features_params = {
        "features": '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}'
    }
    params = {**query_params, **features_params}
    headers = {
    'Cookie':'g_state={"i_l":0}; at_check=true; lang=en; _gid=GA1.2.694648533.1693891668; mbox=session#ada4e4ba4b524b0fb108d88b8d09eddf#1693894982|PC#ada4e4ba4b524b0fb108d88b8d09eddf.34_0#1757137922; _ga_BYKEBDM7DS=GS1.1.1693893131.1.0.1693893134.0.0.0; _ga=GA1.2.1944397240.1691036487; guest_id=v1%3A169389315392851451; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCLdc5mOKAToMY3NyZl9p%250AZCIlNDNmODlkYzYwMDg2NGQwYTk5N2UxMWVhMTk5YjEzMjI6B2lkIiU0OGYw%250AY2M5ZjM2YTk3MWI2NGM0NWVjM2YwNmUwYjdlNw%253D%253D--d29e096d9606363a1e3a0fdfa12c3111bf0b0704; kdt=XrTOAAusMpWU0vneSAe4GTuPfS17qF0O2vAxINru; auth_token=a07f520609b88892898c5efb12a8b6bfecce55a6; ct0=904a1fe5edae3ae3137f83c32663d72bd1576c94ecf99cb06dadbc7b9a12ff826b5a9741ba7ae07d32717cbc66f401b297b114bd192d3e49baffa0534043d2774daedad8f572785f6698540ea39b7245; guest_id_ads=v1%3A169389315392851451; guest_id_marketing=v1%3A169389315392851451; twid=u%3D1698937702270287872; personalization_id="v1_PlAhAdfPS7qmXfhtl0Zxqw=="',
    'Referer':'https://twitter.com/search?q=SES%20AI%20Corp%20until%3A2015-01-04%20since%3A2015-01-03&src=typed_query&f=top',
    'X-Client-Transaction-Id':'OdAWxQb1ET5sPM2STuKIB/aUPZcNHJXtMVlsBtuG6UsCB+jNe2IUXX878iso7D6QIvVfnjmrlxFoUIAIaEOxPTtyeuSCOA',
    'X-Client-Uuid':'954334ca-30cd-4f97-a346-b7341f8bb791',
    'X-Csrf-Token':'904a1fe5edae3ae3137f83c32663d72bd1576c94ecf99cb06dadbc7b9a12ff826b5a9741ba7ae07d32717cbc66f401b297b114bd192d3e49baffa0534043d2774daedad8f572785f6698540ea39b7245',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51',
    'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers,params=params) as r:
            res = await r.json()
            print(r)
            contents = res['data']['search_by_raw_query']['search_timeline']['timeline']['instructions'][0]['entries']
            for content in contents:
                if "tweet" in content["entryId"]:
                    full_text = content['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
                    name = content['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['name']
                    print("[INFO]:用户",name)
                    print(full_text)
                    print("===========================================================")

async def xunhuan():
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2015, 1, 2)
    global tasks
    while start.date() <= end.date():
        end_day = start + timedelta(days=1)
        task = asyncio.create_task(get_info("SES AI Corp",start.strftime("%Y-%m-%d"),end_day.strftime("%Y-%m-%d")))
        tasks.append(task)
        # if len(tasks) == 1:
        #     await asyncio.wait(tasks)
        #     tasks = []
        # get_info("SES AI Corp",start.strftime("%Y-%m-%d"),end_day.strftime("%Y-%m-%d"))
        print(start.strftime("%Y-%m-%d"), "-", end_day.strftime("%Y-%m-%d"))

        start = end_day
    await asyncio.wait(tasks)

asyncio.run(xunhuan())