ans = input('Input your string: ') + ' '
ans = ans.lower()
words = []
ind = []
k = 0

for i in range(len(ans)-1):
    if ans[i] != ' ':
        k += 1
    if ans[i+1] == ' ':
        words.append(ans[i-k+1:i+1])
        k = 0

flag = 0
for i in range(len(words)):
    for j in range(len(words[i]) - 1):
        for k in range(j+1, len(words[i])):
            if words[i][j] == words[i][k]:
                ind.append(i)
                flag = 1
                break
        if flag == 1:
            break

i = len(ind) - 1
while i >= 0:
    words.pop(ind[i])
    i -= 1

fmax = len(words[0])
for i in words:
    if fmax < len(i):
        fmax = len(i)

print('The biggest word(s) is')
for i in words:
    if len(i) == fmax:
        print(i)
input()
