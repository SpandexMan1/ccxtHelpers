import pandas as pd
import asyncio
import ccxt.pro as ccxtpro

exchange = ccxtpro.binance({
                  'apiKey': <YOUR_API_KEY>,
                  'secret' : <YOUR_API_SECRET>
})

async def main():
    fees = await (exchange.fetch_trading_fees())
    await exchange.close()
    df = pd.DataFrame(fees)
    df_fees = df.T
    
    zero_maker = df_fees[df_fees["maker"] == 0]
    maker_file =  "MakerZeroFees.csv"
    zero_maker.to_csv(maker_file, index=False)
    zero_maker = pd.read_csv(file_path_maker)
    zero_maker["symbol"].to_csv(maker_file, index=False, header=True)

    zero_taker = df_fees[df_fees["taker"] == 0]
    taker_file = "TakerZeroFees.csv"
    zero_taker.to_csv(taker_file, index=False)
    zero_taker = pd.read_csv(taker_file)
    zero_taker["symbol"].to_csv(taker_file, index=False, header=True)
    


if __name__=='__main__':
    asyncio.run(main())
