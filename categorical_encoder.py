import pandas as pd

df = pd.read_csv()

def categorical_encoding(df):
    """" Function to encode categorical values to numerical values"""
    #Keeping only categorical features
    categorical_columns = list(df.select_dtypes(include=[object]).columns)

    for feature in categorical_columns:
        #Keeping unique values
        values = list(set(df[feature].values()))
        for value in values:
            name = "{0} : {1}".format(str(feature),str(value))
            df[name] = (df[feature] == value).astype(float)
        del df[feature]
        print('Categorical feature {0} encoded'.format(str(feature)))

    return df