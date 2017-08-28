This README.md for Eclipse project to delevop scrapy

===================================================================

Environment:

1. Mac OS Yosemite 10.10.5
2. Python 2.7
3. Scrapy

===================================================================

<<<<<<< HEAD
Describtion:

=======
Description:
>>>>>>> a7d55916d670f1aeb60f80149aee720a56acffa2
This spider project only crawl：http://movie.mtime.com/79055/posters_and_images/posters/hot.html <飞屋环游记 UP> photos, total 283 photos（剧照，工作照，宣传照等）

===================================================================

Process:

setting.py -> items.py -> mtime.py -> pipelines.py

setting.py
1. Add below config to debug program, usual to see HTTPError 400(bad request), 403(IP mask) fail
- LOG_LEVEL= 'DEBUG'
- LOG_FILE ='log.txt'

mtime.py
1. Using response.xpath(....).re(pattern) to parse image URL

pipelines.py:
- #1. Using urllib2.Request and urllib.urlopen to get image binary data and write them to .jpg file
1. Using requests.get to get image binary data and write them to .jpg file
2. Add time.sleep(0.5) to avoid my IP was masked by mtime server
3. Judge if get file size less than 2KB will write it's URL to pic2KB.txt

===================================================================

exec process:

1. cd ../E0819_mtime_test/S0819Mtime_tiantang
2. scrapy crawl mtime

===================================================================
