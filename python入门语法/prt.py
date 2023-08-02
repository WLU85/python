name = "tencen"
stock_price = 18.88
stock_code = "0354"
daily_growth = 1.01
growth_day = 7
print(f"公司名为{name},股票代码为{stock_code},当前股价为{stock_price}")
print("每日增长系数为%.2f,增长时间为%d,股价到达了%.2f"%(daily_growth,growth_day,18.88*(1.01**7)))