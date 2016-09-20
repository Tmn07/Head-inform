# coding:UTF-8

import requests
import mymail

class head_inform(object):
	"""docstring for head_inform"""
	def __init__(self, qnum):
		super(head_inform, self).__init__()
		self.qurl = "http://q.qlogo.cn/g?b=qq&s=100&nk=" + qnum
		self.s = requests.Session()

	def get_modified_time(self):
		with open('data.txt') as f:
			t = f.readline()
		return t

	def run(self):
		try:
			r = self.s.get(self.qurl)
			if r.headers["Last-Modified"] != self.get_modified_time():

				with open("pic.jpg","wb") as f:
					f.write(r.content)

				with open('data.txt','w') as f:
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