import json
import os
import urllib
import zipfile
from symbol import get_all_symbols


for symbols in type:
    print(symbols)
dir_name = 'E:/binance-public-data/python/data/spot/monthly/trades'
extension = ".zip"
# change directory from working dir to dir with files
file_name = dir_name + "/" + symbols

for item in os.listdir(dir_name):  # loop through items in dir
    if item.endswith(extension):  # check for ".zip" extension
        file_name = os.path.abspath(item)  # get full path of files
        zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
        zip_ref.extractall(dir_name)  # extract file to dir
        zip_ref.close()  # close file
        os.remove(file_name)  # delete zipped file
