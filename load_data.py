import urllib.request
import json


class LoadData:

    @staticmethod
    def load(path):
        with urllib.request.urlopen(path) as url:
            data = json.load(url)
            return data
