import pprint

message = 'If curiosity killed the cat, then I’m in a heck of a lot of trouble. I love coding because it requires tenacity, creativity, and curiosity.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#pprint.pprint(count) displays the dictionary value cleanly

#pformat() returns a string value of this output
myquote = pprint.pformat(count)
print (myquote)
