import urllib.request
import zipfile
import pandas as pd
import os

class ReadFile:
    PATH_ARCHIVE: str = "files/dataset"
    
    def __init__(self):
        pass
    
    def readCSV(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.PATH_ARCHIVE}/Best_Games_of_All_Time.csv')
        
    
    def fetch_data(self, url:str):
        urllib.request.urlretrieve(url, 'files/dataset/best-games-of-all-time.zip')
        zipfile.ZipFile('files/dataset/best-games-of-all-time.zip').extractall(path=self.PATH_ARCHIVE)
        # tarfile.open('files/dataset/best-games-of-all-time.zip').extractall(path=self.PATH_ARCHIVE)
        
    def verify_path(self) -> bool:
        return bool(os.listdir(self.PATH_ARCHIVE))
        
        
        