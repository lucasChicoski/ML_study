import urllib.request
import zipfile
import pandas as pd
import os

class ReadFile:
    PATH_ARCHIVE: str = "files/dataset"
    
    
    def __init__(self):
        self.filename = ''
        pass
    
    def readCSV(self) -> pd.DataFrame:
        asd = os.listdir(path=self.PATH_ARCHIVE)
        self.filename = asd[1]
        return pd.read_csv(f'{self.PATH_ARCHIVE}/{self.filename}')
        
    
    def fetch_data(self, url:str):
        urllib.request.urlretrieve(url, f'{self.PATH_ARCHIVE}/dataset.zip')
        zipfile.ZipFile(f'{self.PATH_ARCHIVE}/dataset.zip').extractall(path=self.PATH_ARCHIVE)
        asd = os.listdir(path=self.PATH_ARCHIVE)
        self.filename = asd[1]
        print(asd[1])
        # tarfile.open('files/dataset/best-games-of-all-time.zip').extractall(path=self.PATH_ARCHIVE)
        
    def verify_path(self) -> bool:
        return bool(os.listdir(self.PATH_ARCHIVE))
        
        
        