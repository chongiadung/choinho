# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class Product(Item):
    # define the fields for your item here like:
    # name = Field()
    source = Field()
    url = Field()
    name = Field()
    norm_name = Field()
    price = Field()
    category = Field()
    description = Field()
    images = Field()    
    base_url = Field()
    timestamp = Field()
    canonical = Field()
    origin_url = Field()
    origin_price = Field()
    expired = Field()
    raw_url = Field()
    brand = Field()
    model = Field()
    property = Field()

    def isValid(self):
        if 'name' in self:
            return self['url'] and self['name']
