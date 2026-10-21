a = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
def lookup(word):
    if word in a:
        return a[word]
    else:
        return None
print(a.get('a'))