
import os
import  pandas as pd


input_file_path = "D:\\Datasets\\IPL_2024\\Data Files\\Clean_Data"
output_file_path = "D:\\Datasets\\IPL_2024\\Data Files\\Clean_Data\\Overall_Data"


def combine_data(input_file_path, output_file_path):
    os.chdir(input_file_path)
    file_list = [file for file in os.listdir() if file.endswith('.csv')]
    df_list = []
    for file in file_list:
        temp = pd.read_csv(file)
        df_list.append(temp)

    df = pd.concat(df_list,ignore_index=True)
    df = df.sort_values(by=['match_number', 'innings', 'over', 'ball'])
    return df.to_csv(output_file_path+'\\ipl2024.csv',index=False)



combine_data(input_file_path, output_file_path)

