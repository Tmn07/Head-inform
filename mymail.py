#coding:utf-8 
import smtplib 
from email.header import Header
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr


import os

ddir = os.path.split(os.path.realpath(__file__))[0]

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))



def sendMail(sender,receiver,subject): 
    smtpserver = 'smtp.sina.com' 
    username = "qq519043202@sina.com"
    # 写上你的stmp服务
    password = "xxxxx"

    msg = MIMEMultipart('alternative') 
    msg['Subject'] = Header(subject,'utf-8')

    msg['From'] = _format_addr(u'zwd <%s>' % sender)
    msg['To'] = _format_addr(u' <%s>' % receiver)

#html格式构造

    html =  """
    <html> 
      <body> 
        <p> 你好啊<br> 
          我的头像变了呀～现在是这样紫的<br>
          <img src="cid:image1"></br> 
        </p> 
      </body> 
    </html> 
    """ 
    htm = MIMEText(html,'html','utf-8') 
    msg.attach(htm)

 

#构造图片

    fp = open(ddir+'/pic.jpg','rb') 
    msgImage = MIMEImage(fp.read()) 
    fp.close()

    msgImage.add_header('Content-ID','<image1>') 
    msg.attach(msgImage)


    smtp = smtplib.SMTP() 
    smtp.connect("smtp.sina.com") 
    smtp.login(username,password) 

    msg['From'] = _format_addr(u'zwd <%s>' % sender)
    smtp.sendmail(sender,[receiver],msg.as_string()) 
    smtp.quit()




sender = "qq519043202@sina.com"
# 修改receiver
subject = 'zwd的头像变了啊～' 

def send():
  # sendMail(sender,receiver,subject)
  sendMail(sender,"519043202@qq.com",subject)