# IMAP_Bruteforce

IMAP（Internet Mail Access Protocol）以前称作交互邮件访问协议（Interactive Mail Access Protocol），是一个应用层协议。IMAP是斯坦福大学在1986年开发的一种邮件获取协议。它的主要作用是邮件客户端可以通过这种协议从邮件服务器上获取邮件的信息，下载邮件等。当前的权威定义是RFC3501。IMAP协议运行在TCP/IP协议之上，使用的端口是143。它与POP3协议的主要区别是用户可以不用把所有的邮件全部下载，可以通过客户端直接对服务器上的邮件进行操作。----来源于百度百科

目前的知名企业邮箱（如腾讯企业邮箱）均支持该协议，许多人喜欢用邮件客户端或者手机收发邮件，则大多数会选择开启该服务。在大多数情况下适用。（文末有脚本下载地址）。

该脚本使用Python开发，2和3版本均可运行。

```
usage: imap-bruteforce.py [-h] [-s SERVER] [-p PORT] -d DOMAIN [-u USER]
                          [-o [OUTPUT]]

OPTIONS:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        imap host
  -p PORT, --port PORT  port
  -d DOMAIN, --domain DOMAIN
                        domain
  -u USER, --user USER  user
  -o [OUTPUT], --output [OUTPUT]
                        save the result to text file
```

-s SERVER

imap 服务器地址，默认是imap.exmail.qq.com

-p PORT

imap 服务器端口，默认是imaps的993端口

-d DOMAIN

要爆破的企业域名，该项为必须

-u USER

要爆破的用户名，或者存有用户名的文件列表（一行一个），默认读取当前目录下的email.txt

-o [OUTPUT]

输出的结果文件，默认保存在result.txt

除此之外，在当前目录下生成logs.txt文件，保存错误以及验证失败的日志信息。方便分析情况。

