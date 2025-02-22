
# WLECOME TO ONICRAWLER RECON TOOL
# CREATED BY PURPL3S3C

import sys
import os
import time
import requests
from urllib.parse import urlparse

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

banner = (O + """
 ██████╗ ███╗   ██╗██╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔═══██╗████╗  ██║██║██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║   ██║██╔██╗ ██║██║██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║   ██║██║╚██╗██║██║██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╔╝██║ ╚████║██║╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝ v1.2   """ + B + "Made " + C + "by: " + P + "PURPL3S3C" + W)
print (banner)
def ensure_url_scheme(url):
    """Verifies (http o https)."""
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = f"https://{url}"  
    return url

def is_url_active(url):
    """Verifies"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            print(R + f"Error (código {response.status_code}){W}")
            return False
    except requests.RequestException as e:
        print(R + f"Error connecting to URL: {e}{W}")
        return False

def fetch_archived_urls(domain, filename):
    url = "https://web.archive.org/cdx/search/cdx"
    params = {
        "url": f"*.{domain}/*",
        "collapse": "urlkey",
        "output": "text",
        "fl": "original"
    }
    
    print(W + "Crawling in progress... Please wait." + W, end='', flush=True)

    # Realiza la solicitud HTTP
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    with open(filename, "w") as file:
        file.write(response.text)

def process_url():
    url = input(C + "URL to crawl : " + W)
    url = ensure_url_scheme(url)
    
    if not is_url_active(url):
        print(R + "Invalid or inactive URL!" + W)
        return
    
    filename = input(C + "Output file name: " + W)
    
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    print(O + f"CRAWLING!: {B}{url}{W}")

    start_time = time.time()  

    try:
        fetch_archived_urls(domain, filename)
        elapsed_time = time.time() - start_time  
        print(G + f"""
Domains saved in {B}{filename}{G} succesfully!{W}""")
        print(GR + f"Time: {elapsed_time:.2f} seconds" + W)  
    except requests.RequestException as e:
        print(R + f"Error Process Stopped: {e}{W}")

if __name__ == "__main__":
    process_url()
