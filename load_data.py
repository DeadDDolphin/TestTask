import urllib.request
import json
import os
import time
import datetime


class LoadData:
    """
    Class for static methods

    Methods
    -------
    load(path):
        load data from url and return it
    get_date_from_file(path):
        find date in file and return in the required format
    """

    @staticmethod
    def load(path):
        """
        connect to url and load data
        :param path: url
        :type path: str
        :rtype: list
        :return: list of dicts
        """
        with urllib.request.urlopen(path) as url:
            data = json.load(url)
            return data

    @staticmethod
    def get_date_from_file(path):
        """
        Find date in file. Return it in the required format.
        :param path: path to file
        :type path: str
        :rtype: str
        :return: date in the required format
        """
        old_time = os.path.getctime(path)
        old_date = time.ctime(old_time)
        old_date = datetime.datetime.strptime(
            old_date, "%a %b %d %H:%M:%S %Y")
        return old_date.strftime("%d-%m-%YT%H:%M")