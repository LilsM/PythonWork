'''
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Function Description

It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s): s: an array of integers, the numbers on each of the squares of chocolate d: an integer, Ron's birth day m: an integer, Ron's birth month
'''
def birthday(s, d, m):
    way = 0
    segment = []
   # s=list(map(s).strip().split())
    for i in range(len(s)):
        for j in range(1,(len(s))+1):
            segment = (s[i:j])
            if len(segment) == m and sum(segment)==d:
                way = way+1
                #print("month: ",len(segment))
                #print("day: ",d)
    return (way,"ways of dividing the chocolate")

def main():
    s = []
    n = eval(input("Enter number of items in array:"))
    for i in range (n):
        s.append(eval(input("Enter your number:")))
    d = int(input("Enter date of birth: "))
    m = int(input("Enter month of birth: "))
    print(birthday(s,d,m))
main()


