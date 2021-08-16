import scrapy
from ..items import ImdbItem


class ImdbSpider(scrapy.Spider):
    name = 'Imdb'
    start_urls = [
        'https://www.imdb.com/title/tt0000001/'
        ]


    def parse(self,response):
        item = ImdbItem()
        item['id'] = response.request.url.split('/')[-2]
        try:
            item['Title'] = response.css('.TitleHeader__TitleText-sc-1wu6n3d-0').css('::text').extract()[0]
        except:
            pass
        try:
            item['Avg_rating'] = response.css('.AggregateRatingButton__RatingScore-sc-1ll29m0-1.iTLWoV').css('::text').extract()[0]
        except:
            pass
        try:
            item['total_ratings'] = response.css('.AggregateRatingButton__TotalRatingAmount-sc-1ll29m0-3.jkCVKJ').css('::text').extract()[0]
        except:
            pass
        r = response.css('.score').css('::text').extract()
        if len(r) == 2:
            item['user_reviews'] = r[0]
            item['critic_reviews'] = r[1]

        try:
            item['description'] = response.css('.GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0.dcFkRD').css('::text').extract()[0]
        except:
            pass
        infos = response.css('li.ipc-metadata-list__item')
        # print(item.keys())
        keys = ['Country_of_origin','Aspect_ratio','Sound_mix','Runtime','Budget','Production_companies','Language','Release_date','Certificate','Genres','Writer','Director','Stars']
        for info in infos:
            info = info.css('::text').extract()

            info[0] = info[0].replace(' ','_')
            if info[0] in keys:

                item[info[0]] = ' , '.join(info[1:])
        yield item

        for i in range(2,1001):
            if i < 10:
                i = '000'+str(i)
            elif i < 100:
                i = '00'+str(i)
            elif i <1000:
                i = '0'+str(i)
            url = f'https://www.imdb.com/title/tt0000{i}/'
            yield response.follow(url,callback=self.parse)
