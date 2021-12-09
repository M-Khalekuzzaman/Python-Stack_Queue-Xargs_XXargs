#Stack is a data stracture   [LIFO = Last in First out]
'''
1) Push
2) Pop
'''
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
books.append("Learn JavaScript")
print(books)

books.pop()
books.pop()
print("Now the top books is = ",books[-1])

#Queue is a data structure  [FIFO = First in First out]

from collections import  deque

bank = deque(["Khalekuzzaman","kaochar","Khairul"])
print(bank)
bank.popleft()
print(bank)
bank.pop()
bank.pop()
if not bank :
    print("No person left")



