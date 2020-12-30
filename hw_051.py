from functools import reduce

def clean_punctuation(words):
    clean_data = []
    for i in words:
        chars = reduce(lambda x,y: x+ (y if y.isalnum() else ''), i)
        clean_data.append(chars)
    return clean_data

#a="I WISH to WISH the WISH you WISH to WISH, but if you WISH the WISH the witch wishes, I won't WISH the wish you wish to WISH.|wish,you"
a=input()
parag, banned = a.lower().split('|')
clean_parag = clean_punctuation(parag.split())
clean_banned = clean_punctuation(banned.split(','))
filtered = list(filter(lambda x: x not in clean_banned, clean_parag))

counts={}
for i in filtered:
    counts[i]= counts.get(i,0)+1

ans= sorted(counts.items(),key=lambda x:x[1],reverse=True)
print(ans[0][0])