import requests
import zstandard
import csv
import io

class PuzzleDatabaseDownloader:
    
    def __init__(self, url: str):
        self.url = url

    
    def streams_rows(self):
        with requests.get(self.url, stream=True) as response:
            response.raise_for_status()
            descompress = zstandard.ZstdDecompressor().stream_reader(response.raw)
            text = io.TextIOWrapper(descompress, encoding='utf-8')
            dict_reader = csv.DictReader(text)
            yield from dict_reader

        