txt = input()

words  = txt.split()

a = 0
longest = words[0]

while ( a <= (len(words)-2)):

    if (len(longest) > len(words[a+1])):
        longest = longest
        
    elif (len(longest) <= len(words[a+1])):
        longest = words[a+1]
        
    a = a + 1
