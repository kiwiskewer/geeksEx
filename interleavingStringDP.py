def isInterleaving(s1,s2,s3):
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    if l1 + l2 != l3:
        return False
    if l1 == 0:
        return s3 == s2
    if l2 == 0:
        return s3 == s1
    i = 0
    j = 0
    start = -1
    end = -1
    last_start = -1
    last_end = l2
    while i < l1+1:
        while j < l2+1:
            if j>0 :
                if s3[i+j-1] == s2[j-1]:
                    if start == -1:
                        start = j
                    end = j
                    j += 1
                else:
                    if start != -1:
                        break
                    j += 1
            elif i > 0:
                if s3[i-1] == s1[i-1]:
                    start = 0
                    end = 0
                else:
                    start = -1
                    end = 1
                j+=1
            else:
                j += 1
                start = 0
                end = 0
            #print(i,j,start,end)
        j = 0
        if end < last_start or start>last_end:
            return False
        last_start = start
        last_end = end
        i += 1
    return True






str1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
str2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
str3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
#str1 = 'aa'
#str2 = 'bb'
#str3 = 'abab'
print (isInterleaving(str1,str2,str3))
