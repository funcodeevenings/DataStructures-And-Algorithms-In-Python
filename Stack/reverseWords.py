def reverseWords(string):
    lst = string.split()
    for word in lst:
        print(word[::-1]) 

reverseWords("hello how are you baby")