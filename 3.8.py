from collections import Counter, defaultdict
def  anagram_check(keywords):
  anagrams = defaultdict(list)
  for i in keywords:
   histogram = tuple(Counter(i).items())
   anagrams[histogram].append(i)
  return list(anagrams.values())
keywords = ("000","123!!","happy","987","654","123")
print(anagram_check(keywords))

def comb(L):      
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if (i!=j and j!=k and i!=k):
                    print("[",L[i],",",L[j],",",L[k],"]")
list=[]
r=int(input("Range : "))
for i in range(r):
    i=int(input("Enter : "))
    list.append(i)
comb(list)
