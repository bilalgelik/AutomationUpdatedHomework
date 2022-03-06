class WebPush:
    def __init__(self, platform , optin , global_frequency_capping , start_date , end_date , language , push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date  = end_date 
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print(f"{self.push_type} gönderildi..")
    
class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type , trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type )
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type , send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type) 
        self.send_date = send_date

class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type , segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name

class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
    
    def discoun_price(self , price_info , discount_rate):
        self.price_info = price_info
        self.discount_rate = discount_rate
        print(price_info - (price_info * discount_rate))


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

    def stock_update(self , stock_info):
        self.stock_info = stock_info
           
        if stock_info == True:
            stock_info = False
            print(stock_info)

        elif stock_info == False:
            stock_info = True
            print(stock_info)

        return stock_info

trigger_push_nesnesi = TriggerPush("Mozilla" , True , 4 , "01.01.2022" , "01.01.2023" , "EN", "TriggerPush" , "Home Page")
print(trigger_push_nesnesi.trigger_page)
trigger_push_nesnesi.send_push()

bulk_push_nesnesi = BulkPush("Chrome" , True , 4 , "01.01.2022" , "01.01.2023" , "EN", "BulkPush" , "02.02.2024")
print(bulk_push_nesnesi.send_date)
bulk_push_nesnesi.send_push()

segment_push_nesnesi = SegmentPush("Mozilla" , True , 4 , "01.01.2022" , "01.01.2023" , "EN", "SegmentPush" , "Segment-c2400")
print(segment_push_nesnesi.segment_name)
segment_push_nesnesi.send_push()

price_alertPush_nesnesi = PriceAlertPush("Mozilla" , True , 4 , "01.01.2022" , "01.01.2023" , "EN", "PriceAlertPush")
price_alertPush_nesnesi.discoun_price(200 , 0.2)
price_alertPush_nesnesi.send_push()

instock_push_nesnesi = InstockPush("Mozilla" , True , 4 , "01.01.2022" , "01.01.2023" , "EN", "InStockPush")
instock_push_nesnesi.stock_update(True)
instock_push_nesnesi.send_push()