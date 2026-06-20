import requests
import zstandard
import csv
import io

class PuzzleDatabaseDownloader:
    
    def __init__(self, url: str):
        self.url = url

    
    def streams_rows(self):
        request = requests.get(self.url, stream=True)
        descompress = zstandard.ZstdDecompressor().stream_reader(request.raw)
        text = io.TextIOWrapper(descompress, encoding='utf-8')
        dict_reader = csv.DictReader(text)
        yield from dict_reader

        