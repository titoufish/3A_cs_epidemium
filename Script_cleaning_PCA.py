from PCA import transform_pca
from categorical_encoder import categorical_encoding
from Missing_values_remover import remove_na
import pandas as pd




df = pd.read_csv("C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/FAOSTAT_Replaced_Countries_prepared.csv", header= 1)

print(df.columns)
countries = df['area']
# country_codes = df['area_code']
years = df['year']
for i in range(2):
    print(df.columns[i])
    df = df.drop(df.columns[i], axis= 1)
df = df.drop(columns=['area'])

#Removing na values
df = remove_na(df,0.5)

#Fitting PCA
df = transform_pca(df)

df.insert(0, 'year', years)
df.insert(0, 'area', countries)
# df.insert(0, 'area_code', country_codes)

df.to_csv("C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/FAO50_PCA.csv")