#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import time
import random


st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

list = ["正能量，满满滴!", "优抚人，都自强!", "干的漂亮!", "来，一起背一遍社会主义核心价值观: 富强、民主、文明、和谐， 自由、平等、公正、法治， 爱国、敬业、诚信、友善"]

print st

class MyWXBot(WXBot):

    nnn = 1
    #mesg = "从"+st+"至今，共点赞"+str(self.nnn)+"次, send by www.kongfan.org automatically"

    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 3 and '[Strong]' in msg['content']['data'] :
            mesg = "从"+st+"至今，本群共点赞"+str(self.nnn)+"次 ,"+random.choice(list)  #send by www.kongfan.org automatically"
            if self.nnn % 10 == 0:
                self.send_msg_by_uid('[Strong]' * random.randint(3,6), msg['user']['id'])

                if self.nnn % 10 == 0:
                    self.send_msg_by_uid(mesg, msg['user']['id'])
            self.nnn= self.nnn+1
            print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",self.nnn
            print mesg
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''

def main():
    bot = MyWXBot()
    bot.DEBUG = False
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    main()
