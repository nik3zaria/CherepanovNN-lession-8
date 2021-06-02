import re
from os import path
import requests

file_url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

def main(file_name):
    if not path.exists(file_name):
        download_file(file_name)
    file_analysis(file_name)

def download_file(file_name):
    response = requests.get(file_url)
    with open(file_name, 'wb') as file:
        for list in response:
            file.write(list)


def file_analysis(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for log_string in file:
            splitting_a_string = log_string.split()
            splitting_a_string = ' '.join(splitting_a_string)
            regex = r'(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)).*\[(.*)\].*\"([A-Z]+)\ (\/.+?) ([\d]{1,3}) (\d+)'
            displaying_a_list_of_data = re.findall(regex, splitting_a_string)
            print(displaying_a_list_of_data)


if __name__ == '__main__':
    file_name = 'text_url.txt'
    main(file_name)