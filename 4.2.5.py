my_file = open("textfile.txt", 'r')
text = my_file.read()
text = text.lower()
words = {}
letters = 0
separator = ' !\".\n,—'

for i in range(len(text)-2):
    if separator.find(text[i]) == -1:
        letters += 1
    if separator.find(text[i+1]) != -1 and letters != 0:
        if words.get(text[i - letters + 1:i + 1]) == None:
            words[(text[i - letters + 1:i + 1])] = 1
        else:
            words[(text[i - letters + 1:i + 1])] += 1
        letters = 0
        i += 1

print(words)

max_repeat = 0
for key in words:
    if words[key] > max_repeat:
        max_repeat = words[key]

print('Top-20 words: ')
top_words = 0
while top_words < 20:
    for key in words:
        if words[key] == max_repeat:
            print(key, words[key])
            top_words += 1
            if top_words == 20:
                break
    max_repeat -= 1


my_file.close()