def isInterleaving(s1,s2,s3,i1,i2,i3):
    if i3 == len(s3):
        if (i1 != len(s1) or i2 != len(s2)):
            return False
        else:
            return True
    else:
        if i1 != len(s1) and s3[i3] == s1[i1] and isInterleaving (s1,s2,s3,i1+1,i2,i3+1):
            return True
        elif i2 != len(s2) and s3[i3] == s2[i2] and isInterleaving (s1,s2,s3,i1,i2+1,i3+1):
            return True
        else:
            return False



str1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
str2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
str3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
print (isInterleaving(str1,str2,str3,0,0,0))
