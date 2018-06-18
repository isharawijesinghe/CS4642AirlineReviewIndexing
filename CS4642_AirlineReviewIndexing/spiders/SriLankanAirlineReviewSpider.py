import scrapy
import cssutils

class SriLankanAirlineReviewSpider(scrapy.Spider):
    name = "SriLankanAirlineReviewSpider"
    allowed_domains = ["airlineratings.come"]
    start_urls = ["https://www.airlineratings.com/passenger-reviews/srilankan-airlines/"]


    def parse(self,response):

        for titles in response.xpath("//div[@class='td-post-content']/div[@class='passenger_review']"):
            item ={
                'name': titles.select("div[@class='passenger_review_header']/h3/text()").extract()[0],
                'review_from': titles.select("div[@class='passenger_review_header']/p/text()").extract()[0],
                'review_date': titles.select("div[@class='passenger_review_header']/p/span[@class='review_date']/text()").extract()[0],
                'trvelling_class': titles.select("div[@class='passenger_review_header']/p[@class='cabin_flown']/text()").extract()[0],
                'overall_rating': cssutils.parseStyle(titles.select("div[@class='passenger_ratings']/div[@class='passenger_rating_overall']/div[@class='ten_star_rating']/div[@class='rating']/@style").extract()[0]).width,
                'value_for_money_rating': cssutils.parseStyle(titles.select("div[@class='passenger_ratings']/ul/li/div[@class='five_star_rating']/div[@class='rating']/@style").extract()[0]).width,
                'seat_and_cabing_space_rating': cssutils.parseStyle(titles.select("div[@class='passenger_ratings']/ul/li/div[@class='five_star_rating']/div[@class='rating']/@style").extract()[1]).width,
                'customer_service_rating': cssutils.parseStyle(titles.select("div[@class='passenger_ratings']/ul/li/div[@class='five_star_rating']/div[@class='rating']/@style").extract()[2]).width,
                'entertainment_in_flight_rating': cssutils.parseStyle(titles.select("div[@class='passenger_ratings']/ul/li/div[@class='five_star_rating']/div[@class='rating']/@style").extract()[3]).width,
                'meal_and_beverage_rating': cssutils.parseStyle(titles.select("div[@class='passenger_ratings']/ul/li/div[@class='five_star_rating']/div[@class='rating']/@style").extract()[4]).width,
                'recomended': titles.select("div[@class='passenger_ratings']/ul/li/div[@class='passenger_recommendation']/span/text()").extract()[0],
                'comment': titles.select("div[@class='passenger_review_body']/p/text()").extract()
            }

            yield item


        next_page_url = response.xpath("//div[@class='alignright']/a/@href").extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            print(next_page_url)
            yield scrapy.Request(url=next_page_url,callback=self.parse,dont_filter=True)



