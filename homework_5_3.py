import string
hashtag = input("Please enter hashtag: ")
hashtag_1 = hashtag.title()
hashtag_2 = ''.join([x for x in hashtag_1 if x not in string.punctuation and x != " "])
if len(hashtag_2) > 140:
    hashtag_2 = hashtag_2[:140]
hashtag_2 = "#" + hashtag_2
print(hashtag_2)