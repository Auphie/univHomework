A = 'This is a book That is a cook' #input()
P = 'This' #input()
Q = 'These' #input()

B = A.split(' ')
A1 = [Q if i==P else i for i in B]
print(' '.join(A1))
A2 = [Q+' '+P if i==P else i for i in B]
print(' '.join(A2))
A3 = [i for i in B if i != P]
print(' '.join(A3))

#A1 = ' '+A+' '
#print(A1.replace(' {} '.format(P), ' {} '.format(Q)).strip())
#print(A1.replace(' {} '.format(P), ' {Q} {P} '.format(P=P, Q=Q)).strip())
#print(A1.replace(' {} '.format(P), ' ').strip())