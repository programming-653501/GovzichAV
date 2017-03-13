my_file = open("textfile.txt", 'r')
text = my_file.read()
text = text.lower()
words = {}
k = 0
r = ' !\".\n,—'

for i in range(len(text)-2):
    if r.find(text[i]) == -1:
        k += 1
    if r.find(text[i+1]) != -1 and k != 0:
        if words.get(text[i - k + 1:i + 1]) == None:
            words[(text[i - k + 1:i + 1])] = 1
        else:
            words[(text[i - k + 1:i + 1])] += 1
        k = 0
        i += 1

print(words)

fmax = 0
for key in words:
    if words[key] > fmax:
        fmax = words[key]

print('Top-20 words: ')
i = 0
while i < 20:
    for key in words:
        if words[key] == fmax:
            print(key, words[key])
            i += 1
            if i == 20:
                break
    fmax -= 1


my_file.close()