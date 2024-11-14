s=str(input())
count=""
for i in range(len(s)):
    if s[i] not in count:
        count=count+s[i]
        print(count)
        
print(len(count))
    
