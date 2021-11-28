import urllib.request
import json
import os
import time
import datetime

class LoadData:

    @staticmethod
    def load(path):
        with urllib.request.urlopen(path) as url:
            data = json.load(url)
            return data

    @staticmethod
    def get_data_from_file(path):
        old_time = os.path.getctime(path)
        old_date = time.ctime(old_time)
        old_date = datetime.datetime.strptime(
            old_date, "%a %b %d %H:%M:%S %Y")
        return old_date.strftime("%d-%m-%YT%H:%M")