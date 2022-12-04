import pandas as pd
import fundamentalanalysis as fa

api_key = "f1ae8ba37c1321bd179bbe33dbddc3ef"

#empty data structure
bulkData = pd.DataFrame(columns = ['symbol', 'npmData'])

#show the available tickers
allTickers = fa.available_companies(api_key)


#get unique exchange names
allExchanges = allTickers.exchangeShortName.unique()
print(allExchanges)

#get all ticker data on single exhange
print()
print("Companies On Exchange:")
companiesOnExchange = allTickers[(allTickers.exchangeShortName == 'NASDAQ') &
                               (allTickers.type == 'stock')]
print(companiesOnExchange[:25])

#accessing the stock symbols 
symbols = list(companiesOnExchange[:25].index)
print(symbols)

#for each symbol in list
for i in symbols:
    #request most recent npm data
    financial_ratios_annually = fa.financial_ratios(
                               i, api_key, period="annual") 
    #get net profit margin data
    npmData = financial_ratios_annually[financial_ratios_annually.columns[0]
                                       ].loc['netProfitMargin']
    #save to DataFrame 
    bulkData.loc[len(bulkData)] = [i, npmData]

#sort Dataframe 
bulkData = bulkData.sort_values(
                    'npmData', ascending = False, ignore_index = True)
print(bulkData)


#get top 10 companies by net profit margin
print()
print("Top 10 Companies On Exchange:")
TopTen = bulkData.head(10)
print(TopTen)


