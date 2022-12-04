import pandas as pd
import fundamentalanalysis as fa
# from fmpSecret import fmpSecret as api key

ticker = "MSFT"
api_key = "f1ae8ba37c1321bd179bbe33dbddc3ef"

# Show a large set of in-depth ratios
# financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")

# print(financial_ratios_annually[2021])

# Show Key Metrics
# key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
# print(key_metrics_annually)

# Obtain DCFs over time
dcf_annually = fa.discounted_cash_flow(ticker, api_key, period="annual")
#print('discounted_cash_flow', dcf_annually)

# roic = key_metrics_annually["2021"].loc["roic"]
# print("ROIC")
# print( roic)
# print(dcf_annually.tail())
growthFS = fa.financial_statement_growth(ticker, api_key, period="annual")
growthFS([1])

print(growthFS)
