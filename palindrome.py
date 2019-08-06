#!/usr/bin/python

def isPalindrome(s, start , end):
    if start == end:
        print "String is an odd palindrome"
        return True 
    elif s[start+1] == s[end]:
        print "String is an even palindrome"
        return True
    else:
        if s[start] == s[end]:
            isPalindrome(s, start+1, end-1)
        else: 
            print "String is not a palindrome!"
            return False

# For a given string calculate the longest possible substring from each character position
def create_substr(s):  
    str_len = len(s)
    # iterate over the string length
    for i in range(str_len):
        #print "\nAt char:" + s[i] 
        if i == 0:
            #substr_palindrome(s, 0, 1)
            print ""
        elif i == str_len -1:
            #substr_palindrome(s, str_len -2, str_len -1)
            print ""
        else:
            # calculate the minimum characters on each side of the current character
            boundary_odd = min(i-0, str_len - i -1)
            boundary_even = min(i-0, str_len - i -2 )
            odd_str =  s [ i - boundary_odd  : i + boundary_odd + 1]
            even_str = s [ i - boundary_even : i + boundary_even + 2]
            substr_palindrome (odd_str, 0, len(odd_str)-1)
            #substr_palindrome (even_str, 0, len(odd_str)-1)

# Prints all possible palindromes in a list from a given string
def substr_palindrome(s, start , end):
    p_list =[]
    e_list = []
    # even length string
    if len(s) % 2 == 0:
        mid = (len(s))/2
        for i in range(0,mid):
            print mid-i-1
            if s[mid-i-1] == s[mid+i]:
                e_list.append(s[mid-i-1: mid+i+1])
    # odd length strings
    else:
        mid = len(s) /2       
        for i in range(0,mid):
            # match character on every side of string mid goimg outward till the end of the string
            if s[mid-i-1] == s[mid+i+1]:
                p_list.append(s[mid-i-1:mid+i+2])
            else:
                break
    
    print e_list
        









s = raw_input("Enter string\n")
start_s = 0
end_s = len(s) - 1
#isPalindrome(s,start_s,end_s)
substr_palindrome(s,start_s,end_s)
#create_substr(s)


    

