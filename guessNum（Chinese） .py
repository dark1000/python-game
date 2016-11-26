#-*- coding: gb2312 -*-
import random
punish=['打屁屁','地上滚两圈','很鬼畜地笑两声']
award=['飞吻一个','舔我脚的机会','我的一条陈年内裤','一次尽情玩电脑的机会']
guesses_made=0
name=raw_input('你好愚蠢的人类，我是伟大而睿智的人工智能Python酱！\n能告诉本智能你的名字吗?\n')
print '\n'
number=random.randint(1,20)
pun_num=random.randint(0,2)
awd_num=random.randint(0,3)
print '很好,{0},现在我心中有个数字，它的范围是零到二十，来猜猜吧。 记住，你只有六次机会哦！\n'.format(name)

while guesses_made < 6:
     guess=int(raw_input('你的回答:'))
     guesses_made+=1

     if guess <number:
         print '这个数太小了\n'

     if guess>number:
         print '猜那么大干嘛啦\n'

     if guess==number:
         break

if guess==number:
    print '干得好！ {0}, 你共用了{1}次就猜中了！嘻嘻!特别奖励你{2}\n'.format(name,guesses_made,award[awd_num])
else:
    print '机会用完咯，我心中的数是{0} ！,本次惩罚是{1} 再见，笨蛋\n'.format(number,punish[pun_num])
raw_input()
    
    
