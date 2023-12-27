import twder

name_list=twder.currencies() # 擷取目前所有幣別
name_dict=twder.currency_name_dict()
print(name_list)
print(name_dict)

price=twder.now("USD") # 擷取目前特定幣別報價
print(price)
price_all=twder.now_all() # 擷取目前所有幣別報價
print(price_all)
price_past=twder.past_day("USD") # 擷取昨天報價
print(price_past)
price_past6=twder.past_six_month("USD") # 擷取前六個月報價
print(price_past6)
price_spec=twder.specify_month("USD",2022,6) # 擷取特定年月報價
print(price_spec)