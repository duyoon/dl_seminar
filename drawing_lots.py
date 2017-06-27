import random

lists = ['bona', 'daeung', 'jaewoo', 'jeongmin', 'junhwan',
         'kyubo', 'minkyu', 'seokmin', 'sigue', 'soyoung']

print('Lets figure out whos gonna be the one!!')

print('count start!!')

count = 5

for i in range(50000000):
    if i % 10000000 == 0:
        print('      %d ' % count)
        count -= 1


random.shuffle(lists)

print('Today\'s presenter is ' + lists[0])
