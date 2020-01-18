import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

# The fixer API required a paid subscription for timeseries requests so I used the 'exchangerates' API for the data. However, I have inculuded the correct url for the assignment if access to their timeseries was given.

#These urls pull the exchange rates from 180 days since 25-10-2019 for USD, GBP, and JPY against EUR
correct_url = "http://data.fixer.io/api/timeseries?access_key=5ea258d3837d374b359aa4129618e53e&start_date=2019-28-04&end_date=2019-25-10&base=EUR&symbols=GBP,USD,JPY&format=1"
actual_url = "https://api.exchangeratesapi.io/history?start_at=2019-04-28&end_at=2019-10-25&symbols=USD,GBP,JPY"

#retrieve and load data as parsed information from API
response = requests.get(actual_url)
data = response.text
parsed = json.loads(data)

#print out information
print(json.dumps(parsed, indent=4))


#load data into a pandas DataFrame selecting only exchange rates
df = pd.DataFrame(parsed["rates"])
df.head()

#transponse DataFrame
dfT = df.T
dfT.head(20)

#label Data column and reset index
dfT = dfT.rename_axis('Date').reset_index()
print(dfT)


#plot each exchange rate as line graph
ax = plt.gca()

dfT.plot(kind='line',x='Date',y='GBP', ax=ax)
dfT.plot(kind='line',x='Date',y='JPY', color='red', ax=ax)
dfT.plot(kind='line',x='Date',y='USD', color='green', ax=ax)
plt.title("Exchange Rate of Currencies against Euro")
plt.ylabel("Exchange Rate to Euro")

plt.show()

#pickle DataFrame
dfT.to_pickle("./xchg_rate.pkl")
