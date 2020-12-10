keys = []
for i in range(ord('a'), ord('z')+1):
    keys.append(chr(i))
values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
maps = dict(zip(keys, values))

inp = input().split()

result=set()
for i in inp:
    tmp=''
    for j in i:
        tmp+=maps[j]
    result.add(tmp)

print(len(result))