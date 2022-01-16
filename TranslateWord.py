import csv
import re
import time
import psutil

start = time.time()
a = open("find_words.txt", "r")
words = a.read()
a.close()
wordslist = words.split()


frequency = {}
shakespeare = open("t8.shakespeare.txt", 'r')
ts = shakespeare.read().lower()
mp = re.findall(r'\b[a-z]{3,15}\b', ts)

with open('french_dictionary.csv', mode='r') as input:
    reader = csv.reader(input)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}
    
    
total_english = []
for word in mp:
    if word in wordslist:
        total_english.append(word)
english = set(total_english)
english = list(english)

french = []
for x in english:
    for key, value in dict_from_csv.items():
        if x in key:
            french.append(value)


frequency = {}
for y in total_english:
    count = frequency.get(y, 0)
    frequency[y] = count + 1

fl = frequency.keys()
f = []
for z in fl:
    f.append(frequency[z])
    

last = list(zip(english, french, f))

heading = ['English Word', 'French Word', 'Frequency']
with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(heading)
    for row in last:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')

test_str = text_string
print("The original string is : " + str(test_str))
lookp_dict = dict_from_csv

temp = test_str.split()
res = []
for wrd in temp:
    res.append(lookp_dict.get(wrd, wrd))

res = ' '.join(res)

f = open("t8.shakespeare.translated.txt", "w")
f.write(str(res))
f.close()

time_taken = time.time() - start
memory_taken = psutil.cpu_percent(time_taken)
f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()

