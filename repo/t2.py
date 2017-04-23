import time
import random

nnn = 100
st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
list = ["正能量，满满滴!", "优抚人，都自强!", "干的漂亮!", "来，一起背一遍社会主义核心价值观: 富强、民主、文明、和谐， 自由、平等、公正、法治， 爱国、敬业、诚信、友善"]
a = "从"+st+"至今，共点赞"+str(nnn)+"次, "+random.choice(list)
print a
