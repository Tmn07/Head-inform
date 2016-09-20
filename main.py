# coding:UTF-8

import requests
import mymail

import os

ddir = os.path.split(os.path.realpath(__file__))[0]

# print(ddir)

class head_inform(object):
	"""docstring for head_inform"""
	def __init__(self, qnum):
		super(head_inform, self).__init__()
		self.qurl = "http://q.qlogo.cn/g?b=qq&s=160&nk=" + qnum
		self.s = requests.Session()

	def get_modified_time(self):
		with open(ddir+'/data.txt') as f:
			t = f.readline()
		return t

	def run(self):
		try:
			headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Host':'q.qlogo.cn',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36'
			}

			r = self.s.get(self.qurl,headers=headers)
			print r.status_code
			if r.headers["Last-Modified"] != self.get_modified_time():

				with open(ddir+"/pic.jpg","wb") as f:
					f.write(r.content)

				with open(ddir+'/data.txt','w') as f:
					f.write(r.headers["Last-Modified"])
				mymail.send()
			else:
				print("no change~")

		except Exception as e:
			raise e



def main():
	c1 = head_inform("519043202")
	c1.run()

if __name__ == '__main__':
	main()