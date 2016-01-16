#encoding:UTF-8
import urllib.request
import urllib.parse
import datetime, time

url = "http://127.0.0.1:8000/hw/check_sub_email/?"
args = urllib.parse.urlencode({'key': '23345fafaafjadljkffalwofal;/.afan.nq==+)+0='})  
url += args
last_hour = -1

while True:
	now = datetime.datetime.now()
	hour = now.hour
	if hour != last_hour:
		last_hour = hour
		data = urllib.request.urlopen(url).read()
		data = data.decode('UTF-8')
		print(data)
		# time.sleep(3600-now.second)
	
	# print('now is: {0}h {1}m {2}s'.format(now.hour, now.minute, now.second))
	time.sleep(5)

