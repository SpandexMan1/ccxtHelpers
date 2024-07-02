import ccxt.pro as ccxtpro
import pandas as pd

def get_exchange_capabilities(exchange_name):
    exchange_class = getattr(ccxtpro,exchange_name.lower())
    exchange_instance = exchange_class()
    capabilities = exchange_instance.has
    return capabilities

def main():
    exchange_list = ccxtpro.exchanges
    data = []
    for exchange_name in exchange_list:
        capabilties = get_exchange_capabilities(exchange_name)
        data.append(capabilties)
    df_excg_name = pd.DataFrame(exchange_list, columns = ["Exchange"])
    df_capabilities = pd.DataFrame(data)
    df_combined = pd.concat([df_excg_name,df_capabilities], axis = 1)
    df_combined.to_csv("ExchangeHas.csv", index = False)

if __name__=='__main__':
    main()