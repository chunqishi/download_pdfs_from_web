DPW ( download_pdfs_from_web)
===


An introduction about tools useful for grab all PDF files from one URL link or web page. 


## Getting Started

### Solution 1 (default)
* Install and use Chrome install Chrome extension "[Download Master](https://chrome.google.com/webstore/detail/download-master-free-down/laepcndcehndnjndpfjdcdgbneoimdgg)". 
* Open Download Master Chrome extension
* Click and select "PDF" check-box 
* Start download

![chrome_extension_download_master](.\docs\static\chrome_extension_download_master.png)



### Solution 2 

* Install [python](https://docs.anaconda.com/anaconda/install/index.html) and install [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments.html) package 
* Download this tool
```bash
git clone https://github.com/chunqishi/download_pdfs_from_web.git
```
* Run python script
```bash
cd ./download_pdfs_from_web/python
pip install -r requirements.txt
python pyget.py
```


### Solution 3 (Strong Recommended)

* Download this tool
```bash
git clone https://github.com/chunqishi/download_pdfs_from_web.git
```
* Run script

1. Windows
    1.1. Edit urls.txt
    1.2. Double click [web2pdf.bat](.\bin\windows\web2pdf.bat)
   
2. Linux
```bash
cd download_pdfs_from_web/bin/linux
sh web2pdf.sh $url
```



## Usage

* Download this tool
```bash
git clone https://github.com/chunqishi/download_pdfs_from_web.git
```


## License

MIT License

Copyright (c) 2021 Chunqi Shi (scq830@163.com)



## Changelog

### Version 0.1 2021-11-11

