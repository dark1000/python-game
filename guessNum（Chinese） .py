#-*- coding: gb2312 -*-
import random
punish=['��ƨƨ','���Ϲ���Ȧ','�ܹ����Ц����']
award=['����һ��','���ҽŵĻ���','�ҵ�һ�������ڿ�','һ�ξ�������ԵĻ���']
guesses_made=0
name=raw_input('����޴������࣬����ΰ�����ǵ��˹�����Python����\n�ܸ��߱��������������?\n')
print '\n'
number=random.randint(1,20)
pun_num=random.randint(0,2)
awd_num=random.randint(0,3)
print '�ܺ�,{0},�����������и����֣����ķ�Χ���㵽��ʮ�����²°ɡ� ��ס����ֻ�����λ���Ŷ��\n'.format(name)

while guesses_made < 6:
     guess=int(raw_input('��Ļش�:'))
     guesses_made+=1

     if guess <number:
         print '�����̫С��\n'

     if guess>number:
         print '����ô�������\n'

     if guess==number:
         break

if guess==number:
    print '�ɵúã� {0}, �㹲����{1}�ξͲ����ˣ�����!�ر�����{2}\n'.format(name,guesses_made,award[awd_num])
else:
    print '�������꿩�������е�����{0} ��,���γͷ���{1} �ټ�������\n'.format(number,punish[pun_num])
    
    
