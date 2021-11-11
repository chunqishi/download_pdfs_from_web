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
import socket, sys, time

socket.setdefaulttimeout(60 * 3)  # 60 seconds


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time + 1
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / (total_size + 1))
    sys.stdout.write("\r\t...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def get(url: str, folder: str):
    response = urllib.request.urlopen(url).read()
    # import requests
    # response = requests.get(url).content
    soup = BeautifulSoup(response, "html.parser")
    from tqdm import tqdm
    links = [urljoin(url, link['href']) for link in soup.select("a[href$='.pdf']")]
    for i, link in enumerate(links):
        print(i, link)

    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f'Create folder {os.path.abspath(folder)}')

    for link in tqdm(links):
        # print(link)
        if os.path.exists(folder):
            filename = link.split('/')[-1]
            realfile = os.path.join(folder, filename)
            tempfile = os.path.join(folder, f"~{filename}")
            if not os.path.exists(realfile):
                if os.path.exists(tempfile):
                    os.remove(tempfile)

                # print(link, tempfile)
                urllib.request.urlretrieve(link, tempfile, reporthook)
                # print(tempfile, realfile)
                os.rename(tempfile, realfile)


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
