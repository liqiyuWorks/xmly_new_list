# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import datetime

class XmlyNewListPipeline:
    def open_spider(self, spider):
        try:
            host = spider.settings.get('MYSQL_HOST')
            user = spider.settings.get('MYSQL_USER')
            password = spider.settings.get('MYSQL_PASSWORD')
            database = spider.settings.get('MYSQL_DATABASE')
            charset = spider.settings.get('MYSQL_CHARSET')
            spider.logger.info('open spider')
            # 连接数据库
            self.conn = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)
            # 创建游标
            self.cursor = self.conn.cursor()
            spider.logger.info("start_time:{}".format(datetime.datetime.now()))
        except:
            self.open_spider(spider)
        else:
            spider.logger.info('MySQL:connected')

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
        spider.logger.info("end_time:{}".format(datetime.datetime.now()))
        spider.logger.info('close spider')

    def process_item(self, item, spider):
        spider.logger.info('item={}'.format(item))

        sql = """insert into xmly_new_list(contentId,title,price,discountedPrice,priceTypeId,isPaid,customerTitle,playCount,cover,saleTypeId,albumType,hasPermission,expireTime,isSubscribed,supportVipDiscount)
                       values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update
                        contentId = values(contentId),
                        title = values(title),
                        price = values(price),
                        discountedPrice = values(discountedPrice),
                        priceTypeId = values(priceTypeId),
                        isPaid = values(isPaid),
                        customerTitle = values(customerTitle),
                        playCount = values(playCount),
                        cover = values(cover),
                        saleTypeId = values(saleTypeId),
                        albumType = values(albumType),
                        hasPermission = values(hasPermission),
                        expireTime = values(expireTime),
                        isSubscribed = values(isSubscribed),
                        supportVipDiscount = values(supportVipDiscount)"""
        values = (
            item['contentId'],
            item['title'],
            item['price'],
            item['discountedPrice'],
            item['priceTypeId'],
            item['isPaid'],
            item['customerTitle'],
            item['playCount'],
            item['cover'],
            item['saleTypeId'],
            item['albumType'],
            item['hasPermission'],
            item['expireTime'],
            item['isSubscribed'],
            item['supportVipDiscount'])

        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            return item
        except Exception as e:
            spider.logger.info(repr(e))
            self.open_spider(spider)
