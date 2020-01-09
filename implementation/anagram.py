def anagram(s1,s2):
    #string_list=list(s1)

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                break
            else:
                continue
        else:
            print("Not Anagram")
            break
    else:
        print("These are Anagrams")

anagram('abc','cba')