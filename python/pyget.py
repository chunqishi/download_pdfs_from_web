#!/usr/bin/env python

"""
Download all the pdf links on a given webpage

@Usage:
    python pyget.py --help

@Requirements

    pip install beautifulsoup4
    pip install tqdm

"""

__author__ = 'Chunqi SHI <scq830@163.com>'
__license__ = 'MIT'
__version__ = '0.1.1'

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def get(url: str, folder: str):
    # response = requests.get(url)
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), "html.parser")
    from tqdm import tqdm
    for link in tqdm(soup.select("a[href$='.pdf']")):
        if not os.path.exists(folder):
            os.mkdir(folder)
        if os.path.exists(folder):
            filename = os.path.join(folder, link['href'].split('/')[-1])
            # with open(filename, 'wb') as f:
            #     f.write(requests.get(urljoin(url, link['href'])).content)
            urllib.request.urlretrieve(urljoin(url, link['href']), filename)

def main(args):
    try:
        if os.path.exists(args.url_list_file):
            with open(args.url_list_file, 'r') as f:
                lines = f.readlines()
                for url in lines:
                    get(url, args.download_directory)
        elif args.url.lower().startswith('http://'):
            get(args.url, args.download_directory)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-dd', '--download-directory', help="Specify the save directory.", type=str,
                        default='./download_pdfs')
    parser.add_argument('-u', '--url', help="Specify the input url.", type=str, default='')
    parser.add_argument('-f', '--url-list-file', help="Specify txt file with url in each line.", type=str,
                        default='urls.txt')
    args = parser.parse_args()
    main(args)
