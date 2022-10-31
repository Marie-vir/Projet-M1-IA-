import pandas as pd
import numpy as np


def githubcode(df):
    data = pd.read_csv(df,sep=';')
    if type(data)!= pd.DataFrame:
        print("Veillez utiliser un fichier csv")
    else: 
        data.columns = data.columns.str.lower().str.replace(' ', '_')  
        data = data.dropna(axis=0,how="any")
        lista = []
        for pr in data.columns:
            lista.append(pr)
        a =1
        k =1
        while a <= (len(lista)-1):
            k =1
            for i in data[lista[a]]:
                if type(i)==int or type(i)==float:
                    data[lista[a]] = data[lista[a]].astype(str)
                else:
                    data[lista[a]] = i.replace(" ", "_")
            a = a+1
    print(data.head())

githubcode("/Users/miguelnguemandumumangue/Documents/Projet Github/115.csv")