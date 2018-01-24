import pandas as pd
import csv
import collections

# Recipe inputs

data_WORLDBANK_df = pd.read_csv('C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/Worldbank_Mortality_50_PCA.csv')
mortality_aggregate_df = pd.read_csv('C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/FAO50_PCA.csv')

data_output = pd.merge(mortality_aggregate_df, data_WORLDBANK_df, how = 'inner', on = ['area', 'year'])

data_output.to_csv('C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/M_WB_FAO_50_PCA.csv')