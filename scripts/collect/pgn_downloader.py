import requests
import zipfile
import io

class PgnDownloader:

    def __init__(self, url: str):
        self.url = url

    def download(self) -> str:
        zip_content = requests.get(self.url).content
        with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_fiel:
            file_name = zip_fiel.namelist()[0]
            return zip_fiel.read(file_name).decode('utf-8')