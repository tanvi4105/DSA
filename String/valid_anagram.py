s1=input().upper()
s2=input().upper()
def check_Anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    freq=[0]*26
    for ch in s1:
        freq[ord(ch)-ord('A')]+=1
    for ch in s2:
        freq[ord(ch)-ord('A')]-=1  

    for i in freq:
        if i!=0:
            return False
    return True    
print(check_Anagram(s1,s2))    