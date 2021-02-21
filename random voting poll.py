import random , time
num = int(input('enter numbers of candidates : '))
cand = input(f'enter {num} candidates now (name with a space): ').split()
print('voting is live..... please wait for the results..')
time.sleep(3)

print('here are the final result')

votes = []
for x in range(0,num):
    c = random.randrange(1,100,3)
    votes.append(c)
for i in range(num):
    print(cand[i],':', votes[i])

print('hence the winner is...')
maximum = max(votes)
count = 0

for r  in range(num):
    if votes[r]==maximum:
        count = r 
print(cand[count],':', maximum)