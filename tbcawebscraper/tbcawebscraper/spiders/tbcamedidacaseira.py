import scrapy
from scrapy.item import Item, Field
import unicodedata

class AlimentoItem(Item):
    nome = Field()
    energia = Field()
    umidade = Field()
    carboidratoTotal = Field()
    carboidratoDisponível = Field()
    proteina = Field()
    lipidios = Field()
    fibraAlimentar = Field()
    colesterol = Field()
    acidosGraxosSaturados = Field()
    acidosGraxosMonoInsaturados = Field()
    acidosGraxosPoliInsaturados = Field()
    acidosGraxosTrans = Field()
    calcio = Field()
    ferro = Field()
    sodio = Field()
    magnesio = Field()
    fosforo = Field()
    potassio = Field()
    zinco = Field()
    cobre = Field()
    selenio = Field()
    vitaminaARE = Field()
    vitaminaARAE = Field()
    vitaminaD = Field()
    vitaminaE = Field()
    tiamina = Field()
    riboflavina = Field()
    niacina = Field()
    vitaminaB6 = Field()
    vitaminaB12 = Field()
    vitaminaC = Field()
    equivalenteFolato = Field()

class TbcamedidacaseiraSpider(scrapy.Spider):
    name = 'tbcamedidacaseira'
    start_urls = ['http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina=1&atuald=1']
 
    def parse(self, response):
        for row in response.xpath('//*[@class="table table-striped"]//tbody/tr'):
            item = AlimentoItem()
            item["nome"] = self.remove_pontuacao(row.xpath('td[2]//text()').getall()),

            if row.xpath('td[2]//@href').extract_first() is not None:
                url_str = ''.join(map(str, row.xpath('td[2]//@href').extract_first()))
                next_page = response.urljoin(url_str)          
                request = scrapy.Request(next_page, callback=self.parse_alimento)
                request.meta['item'] = item
                yield request
            
            prox_page = response.xpath('//div[@id="block_2"]/a[contains(text(),"pr")]/@href')[0]
            if prox_page is not None:
                yield response.follow(prox_page, callback=self.parse, dont_filter = True)


    def parse_alimento(self, response):
        item = response.meta['item']
        for index, row in enumerate(response.xpath('//*[@id="tabela1"]//tbody/tr')):
            match index:
                case 1 :
                    item['energia'] = row.xpath('td[3]//text()').extract_first()
                case 2 :  
                    item['umidade'] = row.xpath('td[3]//text()').extract_first()
                case 3 :
                    item['carboidratoTotal'] = row.xpath('td[3]//text()').extract_first()
                case 4 :
                    item['carboidratoDisponível'] = row.xpath('td[3]//text()').extract_first()
                case 5 :
                    item['proteina'] = row.xpath('td[3]//text()').extract_first()
                case 6 :
                    item['lipidios'] = row.xpath('td[3]//text()').extract_first()
                case 7 :
                    item['fibraAlimentar'] = row.xpath('td[3]//text()').extract_first()
                case 8 :
                    item['colesterol'] = row.xpath('td[3]//text()').extract_first()
                case 9 :
                    item['acidosGraxosSaturados'] = row.xpath('td[3]//text()').extract_first()
                case 10 :
                    item['acidosGraxosMonoInsaturados'] = row.xpath('td[3]//text()').extract_first()
                case 11 :
                    item['acidosGraxosPoliInsaturados'] = row.xpath('td[3]//text()').extract_first()
                case 12 :
                    item['acidosGraxosTrans'] = row.xpath('td[3]//text()').extract_first()
                case 13 :
                    item['calcio'] = row.xpath('td[3]//text()').extract_first()
                case 14 :
                    item['ferro'] = row.xpath('td[3]//text()').extract_first()
                case 15 :
                    item['sodio'] = row.xpath('td[3]//text()').extract_first()
                case 16 :
                    item['magnesio'] = row.xpath('td[3]//text()').extract_first()
                case 17 :
                    item['fosforo'] = row.xpath('td[3]//text()').extract_first()
                case 18 :
                    item['potassio'] = row.xpath('td[3]//text()').extract_first()
                case 19 :
                    item['zinco'] = row.xpath('td[3]//text()').extract_first()
                case 20 :
                    item['cobre'] = row.xpath('td[3]//text()').extract_first()
                case 21 :
                    item['selenio'] = row.xpath('td[3]//text()').extract_first()
                case 22 :
                    item['vitaminaARE'] = row.xpath('td[3]//text()').extract_first()
                case 23 :
                    item['vitaminaARAE'] = row.xpath('td[3]//text()').extract_first()
                case 24 :
                    item['vitaminaD'] = row.xpath('td[3]//text()').extract_first()
                case 25 :
                    item['vitaminaE'] = row.xpath('td[3]//text()').extract_first()
                case 26 :
                    item['tiamina'] = row.xpath('td[3]//text()').extract_first()
                case 27 :
                    item['riboflavina'] = row.xpath('td[3]//text()').extract_first()
                case 28 :
                    item['niacina'] = row.xpath('td[3]//text()').extract_first()
                case 29 :
                    item['vitaminaB6'] = row.xpath('td[3]//text()').extract_first()
                case 30 :
                    item['vitaminaB12'] = row.xpath('td[3]//text()').extract_first()
                case 31 :
                    item['vitaminaC'] = row.xpath('td[3]//text()').extract_first()
                case 32 :
                    item['equivalenteFolato'] = row.xpath('td[3]//text()').extract_first()
        yield item

    def remove_pontuacao(self, nome):
        result = ''.join(nome)
        text = unicodedata.normalize('NFD', result)\
            .encode('ascii', 'ignore')\
            .decode("utf-8")

        return str(text)
