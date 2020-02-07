import json
import requests
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import luigi


#create Exchange Rates class and instantiate a luigi Task
class Exchange_Rates(luigi.Task):

    #set requirements
    def requires(self, url):
        self.url = url


    #output Task as a pickled file
    def output(self):
        return df.to_pickle("./xchg_rate.pkl")


    #run logic of Task
    def run(self, url):
        #get data from API and load into json file
        response = requests.get(self.url)
        data = response.text
        parsed = json.loads(data)
        #load into pandas DataFrame
        df = pd.DataFrame(parsed["rates"])

        #transponse DataFrame
        df = df.T

        #label Data column and reset index
        df = df.rename_axis('Date').reset_index()

        #plot each exchange rate as line graph
        ax = plt.gca()
        df.plot(kind='line',x='Date',y='GBP', ax=ax)
        df.plot(kind='line',x='Date',y='JPY', color='red', ax=ax)
        df.plot(kind='line',x='Date',y='USD', color='green', ax=ax)
        plt.title("Exchange Rate of Currencies against Euro")
        plt.ylabel("Exchange Rate to Euro")
        plt.show()
        return df


#run instance of Exchnage_Rates class using luigi with API url
if __name__ == '__main__':
    url = "https://api.exchangeratesapi.io/history?start_at=2019-04-28&end_at=2019-10-25&symbols=USD,GBP,JPY"
    luigi.run(main_task_cls = Exchange_Rates)
