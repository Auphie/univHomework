stream = input().split(' ')
#stream = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
odd = [int(i) for i in stream if int(i)%2 == 1]
even = [int(i) for i in stream if int(i)%2 == 0]

odd.sort()
even.sort(reverse=True)
new_stream = odd+even
print(new_stream)