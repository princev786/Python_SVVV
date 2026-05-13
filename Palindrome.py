def palindrome(s):
    #abccba -> 0 1 2 3 4 
    n = len(s)
    for i in range(0,(n-1)//2+1):
        if s[i]!=s[n-1-i]:
            print("Not Palindrome...")
            return
    print("Palindrome String...")

def countfrequency(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

def anagram(s1,s2):
    d1 = countfrequency(s1)
    d2 = countfrequency(s2)

    for i in d1:
        if i not in d2 or  d1[i]!=d2[i]:
            return False
        else:
            d2.pop(i)

    if len(d2.keys())==0:
        return True
    else:
        return False
            
s1 = input("Enter a String :")
s2 = input("Enter a String :")
print(anagram(s1,s2))
