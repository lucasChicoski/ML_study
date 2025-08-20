from core.read_file import ReadFile
import pandas as pd
import matplotlib.pyplot as plt

if(__name__  == '__main__'):

    readFile: ReadFile = ReadFile()
    
    if readFile.verify_path() == False:
        readFile.fetch_data('https://www.kaggle.com/api/v1/datasets/download/arnavtomar18/best-games-of-all-time')
    
    
    data_set:pd.DataFrame = readFile.readCSV()
    
    data_set['Launch_date'] = pd.to_datetime(data_set['Launch_date'])
    data_set["Year"] = data_set['Launch_date'].dt.year
    
    data_set.plot(kind='line', x="Year", y="Metascore", figsize=(10,5) )
    plt.show()
    
    # print(data_set['Launch_date'])
    # print(data_set.head())
    # print(data_set.columns)
    
    # print(readFile.verify_path())



