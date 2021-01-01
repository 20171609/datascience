import sys
from collections import Counter
import re


counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in re.split('[^A-Za-z0-9]+', line)
                  if word)


for word, number in counter.most_common(1000):
    print(f"{word}\t{number}")





#실패한 시도들.
# frequency = {}
#
# sys.stdin = open('sss.txt', 'r')
#
# text_string = sys.stdin.read().lower()
#
# remove_special = re.sub('[=+_~!@#$%^&*()\[\]{}\'\":;`\-]', " ", text_string)
# remove_space = re.sub('  ',"",remove_special)
#
# word_list = re.split(" ",remove_space)
#
# for word in word_list:
#     count = frequency.get(word,0)
#     frequency[word] = count + 1
#
# frequency_list = frequency.keys()
#
# for words in frequency_list:
#     print words, frequency[words]



# counter = Counter(word.lower()
#                   for line in sys.stdin
#                   for words in re.sub('[=+_~!@#$%^&*()\[\]{}\'\":;`\-]'," ", line)
#                   for word in words.split()
#                   if word)


# for line in sys.stdin:
#     line = line.lower()
#     line = line.strip()
#     line = re.sub(' +', ' ', line)
#     line = re.split('[^A-Za-z0-9]+', line)
#     counter += Counter(word for word in line
#                        if word)