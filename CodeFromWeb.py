def search_products(self, keyword, max_page=1, shop='全部', sort='有貨優先', price_min=-1, price_max=-1, is_store_pickup=False, is_ipost_pickup=False):
    """搜尋商品

    :param keyword: 搜尋關鍵字
    :param max_page: 抓取最大頁數
    :param shop: 賣場類別 (全部、24h購物、24h書店、廠商出貨、PChome旅遊)
    :param sort: 商品排序 (有貨優先、精準度、價錢由高至低、價錢由低至高、新上市)
    :param price_min: 篩選"最低價" (需與 price_max 同時用)
    :param price_max: 篩選"最高價" (需與 price_min 同時用)
    :param is_store_pickup: 篩選"超商取貨"
    :param is_ipost_pickup: 篩選"i 郵箱取貨"
    :return products: 搜尋結果商品
    """
    products = []
    all_shop = {
        '全部': 'all',
        '24h購物': '24h',
        '24h書店': '24b',
        '廠商出貨': 'vdr',
        'PChome旅遊': 'tour',
    }
    all_sort = {
        '有貨優先': 'sale/dc',
        '精準度': 'rnk/dc',
        '價錢由高至低': 'prc/dc',
        '價錢由低至高': 'prc/ac',
        '新上市': 'new/dc',
    }

    url = f'https://ecshweb.pchome.com.tw/search/v3.3/{all_shop[shop]}/results'
    params = {
        'q': keyword,
        'sort': all_sort[sort],
        'page': 0
    }
    if price_min >= 0 and price_max >= 0:
        params['price'] = f'{price_min}-{price_max}'
    if is_store_pickup:
        params['cvs'] = 'all'   # 超商取貨
    if is_ipost_pickup:
        params['ipost'] = 'Y'   # i 郵箱取貨

    while params['page'] < max_page:
        params['page'] += 1
        data = self.request_get(url, params)
        if not data:
            print(f'請求發生錯誤：{url}{params}')
            break
        if data['totalRows'] <= 0:
            print('找不到有關的產品')
            break
        products.extend(data['prods'])
        if data['totalPage'] <= params['page']:
            break
    return products


def get_products_sale_status(self, products_id):
    """取得商品販售狀態

    :param products_id: 商品 ID
    :return data: 商品販售狀態資料
    """
    if type(products_id) == list:
        products_id = ','.join(products_id)
    url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id={products_id}'
    data = self.request_get(url)
    if not data:
        print(f'請求發生錯誤：{url}')
        return []
    return data
