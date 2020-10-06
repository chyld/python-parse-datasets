import json

lines = []
with open('data/coffee-tweets.json') as f:
    for line in f:
        d = json.loads(line)
        lines.append(d)

for line in lines:
    print(line['place']['full_name'].split(',')[-1])
# aggregate a count of all the states
# CA : 3
# TX : 2
# TN : 9

for line in lines:
    print(line['user']['lang'])

# count all languages used
