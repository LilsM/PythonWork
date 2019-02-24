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


