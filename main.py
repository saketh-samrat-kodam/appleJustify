def appleJustify(paraString,pageWidth):
        index = 0
        string = []
        while index<len(paraString):
            tmp, l, cur = [], 0, ''
            while index<len(paraString) and l+len(paraString[index])+len(tmp)<=pageWidth:
                tmp.append(paraString[index])
                l += len(paraString[index])
                index += 1
            m = len(tmp)-1   # the number of spaces in between words of a page line
            if m!=0:         # distribute the spaces evenly in between words to justify
                q, r = divmod(pageWidth-l, m)
                sp = [q+(1 if j<r else 0) for j in range(m)]
                for j in range(m):
                    cur += tmp[j] + ' '*sp[j]
                cur += tmp[-1]
            elif m==0:       # for lines with only one word
                q = pageWidth-l
                cur += tmp[0] + ' '*q
            string.append(cur)
        return string

ps=input('Please enter a paragraph string:')
pw=int(input('Also enter the page width:'))
ps = ps.strip('\"')
psl=ps.split()
max_word_len = len(max(psl, key = len))
if max_word_len > pw:
    print("words longer that page width exist. please choose a valid page width.")
else:
    aj=appleJustify(psl,pw)
    #print(len(aj))              # number of paragraph line in the page
    for i in range(len(aj)):
        print("Array [" +str(i+1)+"] = \"",str(aj[i]) + "\"", sep='')
