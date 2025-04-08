import subprocess
import time
from selenium import webdriver
from rimager import *


def run_mitmproxy():
    mitmproxy_cmd = [
        "mitmdump", 
        "--listen-port", "8080", 
        "--mode", "regular", 
        "-s", "PATH_TO_capture_response"
    ]
    return subprocess.Popen(mitmproxy_cmd)


mitmproxy_process = run_mitmproxy()
print(f"Started proxy with PID: {mitmproxy_process.pid} || Kill using kill -9 {mitmproxy_process.pid}\n")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://127.0.0.1:8080')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--cert-type=pkcs12')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://dineoncampus.com/northwestern')

time.sleep(15) 

driver.quit()

mitmproxy_process.terminate()
