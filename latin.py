paragraphs = []
paragraph_length = []
with open('data/lorem-ipsum.txt') as t:
    for line in t:
        line = line.strip()
        if line:
            paragraphs.append(line)

for p in paragraphs:
    num_words = len(p.split(' '))
    paragraph_length.append(num_words)

print('nw:', paragraph_length)
