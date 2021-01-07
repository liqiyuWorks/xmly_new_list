import scrapy
import json
import logging
logger = logging.getLogger(__name__)
start_url = "http://m.ximalaya.com/business-content-sort-mobile-web/sortrule/192/contents/pagination/ts-1609905726513?device=iPhone&needFullVo=1&pageNum={}&pageSize=100&version="

class XmlyNewListDetailSpider(scrapy.Spider):
    name = 'xmly_new_list_detail'
    start_urls = [start_url.format(1)]

    def parse(self, response):
        res_content = response.body.decode()
        res_json = json.loads(res_content)
        data_list = res_json.get('data').get('data')
        # print('data_list=', data_list)
        for data in data_list:
            item = {}
            item["contentId"] = data.get('contentId')
            item['title'] = data.get('context').get('title')
            item['price'] = data.get('context').get('price')
            item['discountedPrice'] = data.get('context').get('discountedPrice')
            item['priceTypeId'] = data.get('context').get('priceTypeId')
            item['isPaid'] = data.get('context').get('isPaid')
            item['customerTitle'] = data.get('context').get('customerTitle')
            item['playCount'] = data.get('context').get('playCount')
            item['cover'] = data.get('context').get('cover')
            item['saleTypeId'] = data.get('context').get('saleTypeId')
            item['albumType'] = data.get('context').get('albumType')
            item['hasPermission'] = data.get('context').get('hasPermission')
            item['expireTime'] = data.get('context').get('expireTime')
            item['isSubscribed'] = data.get('context').get('isSubscribed')
            item['supportVipDiscount'] = data.get('context').get('supportVipDiscount')

            yield item
            break

        # 进行翻页
        next_page = 2
        while data_list != []:
            logger.info('-----此时是第{}页'.format(next_page))
            yield scrapy.Request(start_url.format(next_page), callback=self.parse)

            next_page += 1
