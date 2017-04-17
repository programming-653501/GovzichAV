answer = input('Input your string: ') + ' '
answer = answer.lower()
words = []
indexes_of_repeats = []
letters = 0

for i in range(len(answer)-1):
    if answer[i] != ' ':
        letters += 1
    if answer[i+1] == ' ':
        words.append(answer[i-letters+1:i+1])
        letters = 0

flag = 0
for i in range(len(words)):
    for j in range(len(words[i]) - 1):
        for k in range(j+1, len(words[i])):
            if words[i][j] == words[i][k]:
                indexes_of_repeats.append(i)
                flag = 1
                break
        if flag == 1:
            break

quantity_of_repeats = len(indexes_of_repeats) - 1
while quantity_of_repeats >= 0:
    words.pop(indexes_of_repeats[quantity_of_repeats])
    quantity_of_repeats -= 1

find_max_len = len(words[0])
for word in words:
    if find_max_len < len(word):
        find_max_len = len(word)

print('The biggest word(s) is')
for word in words:
    if len(word) == find_max_len:
        print(word)
input()
