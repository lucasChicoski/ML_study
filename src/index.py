from core.read_file import ReadFile
import pandas as pd


if(__name__  == '__main__'):

    readFile: ReadFile = ReadFile()
    
    if readFile.verify_path() == False:
        readFile.fetch_data('https://www.kaggle.com/api/v1/datasets/download/arnavtomar18/best-games-of-all-time')
    
    
    data_set:pd.DataFrame = readFile.readCSV()
    
    print(data_set.head())
    print(data_set.columns)
    
    print(readFile.verify_path())



