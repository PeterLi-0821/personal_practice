from bilibili_api import search, sync


async def test_f_search_by_order():
    return await search.search_by_type("小马宝莉", search_type=search.SearchObjectType.VIDEO,
                                       order_type=search.OrderVideo.SCORES, time_range=10,
                                       topic_type=search.TopicType.AnimeMMD, page=1, debug_param_func=print)


res = sync(test_f_search_by_order())
print(res)
