import os
import email

file = open( r"E:\xtzx\机器学习训练营\hw3\hw3\trec06c-utf8\trec06c-utf8\data_cut\000\030", "r", encoding='utf-8')
msg = email.message_from_file(file)
print(msg)

subject = msg.get("subject")
print(subject)
dh = email.header.decode_header(subject)
subject = dh[0][0].decode("gbk", "ignore") #解码subject

fromm = msg.get("from")
print(fromm)
dh = email.header.decode_header(fromm)
fromm = dh[0][0].decode("gbk", "ignore")#解码from
print("subject: ", subject)
print("from: ", fromm, ' ', email.utils.parseaddr(msg.get("from"))[1])
print("to: ", email.utils.parseaddr(msg.get("to"))[1])

#subject = msg.get("subject")
#dh=email.header.decode_header(subject)#开始解析
#print(dh[0])
#print(dh[0][1])#获取编码
#print("Subject:",dh[0][0].decode("gbk","ignore"))#开始解码
#print("From",email.utils.parseaddr(msg.get("from"))[1])#获取邮件来
#print("To",email.utils.parseaddr(msg["to"])[1])#获取邮件发送

file.close()

import jieba
seg_list = jieba.cut(subject, cut_all = False) #分词
print(" ".join(seg_list))



