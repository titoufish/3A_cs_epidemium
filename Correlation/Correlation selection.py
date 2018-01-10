import pandas as pd, numpy as np        # Data manipulation 

def correlation_matrix(dataset):

    """"Function that returns the correlation matrix of a dataset """

    #Select only numerical columns
    numerical_columns = list(dataset.select_dtypes(include=[np.number]).columns)

    # Select variables to plot for the correlation matrix
    corr_matrix_vars = numerical_columns

    # Only select the requested columns
    df_corr_matrix = dataset[corr_matrix_vars]

    # This computes the Pearson coefficient for all couples
    corr = df_corr_matrix.corr()

    # This takes the absolute value of all coefficients
    corr = np.absolute(corr)

    return corr


def return_name(df,code):
    """"Function that returns the name of a variable from its code """

    name = df.loc[df["Code"] == code]['Indicator Name'].values[0]
    return name

def script_correlation(df,code_names,threshold):

    bool = True
    while bool == True:
        corr_mat = correlation_matrix(df)
        print(len(list(corr_mat)))
        delete = []
        stop = False
        for i, row in enumerate(corr_mat.values):
            # print("i" + str(i))
            for j in range(0, i):
                # print("j" + str(j))
                if row[j] > threshold:
                    delete = [i, j]
                    print(delete)
                    stop = True
                    break
            if stop:
                break
        if not stop:  # No value below threshold was found
            bool = False
        else:
            col_del_code = (list(corr_mat)[delete[0]], list(corr_mat)[delete[1]])

            col_del_name = (return_name(code_names, col_del_code[0]), return_name(code_names, col_del_code[1]))
            col_del_nan = (df[col_del_code[0]].isnull().sum(),df[col_del_code[1]].isnull().sum())
            print( str(col_del_name[0]) + ": " + str(col_del_nan[0]) + " NaN" + ", " + str(col_del_name[1]) + ": " + str(col_del_nan[1]) + " NaN")
            a = input("Quelle colonne supprimer ? (1/2)")
            if a == "1":
                df = df.drop(columns=[col_del_code[0]])
            if a == "2":
                df = df.drop(columns=[col_del_code[1]])
            else:
                "Wrong input"
                pass

    df.to_csv("C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/new_df.csv", sep=',')


### SCRIPT ###

df = pd.read_csv("C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Datasets/WORLDBANK_Valid80.csv")
df = df.drop(columns = ['year'])

code_names = pd.read_csv("C:/Users/titou/Desktop/Centrale/Option OSY/Projet/Correlation analysis/WorldBank_Indicators.csv")
code_names = code_names[["Code","Indicator Name"]]

script_correlation(df, code_names, 0.5)