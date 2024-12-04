# s = "ab[cd]pqde(de(o*q)*np(ab(cd)))*ape"
s = "^(cat).*$"

i1 = -1 
i2 = -1 
istart = -1
count = 0
flag = False
cursedflag = False
starter = ''

flag_start = False
flag_end = False 



# Check if the string starts with '^'
if len(s)>0 and s.startswith('^'):
    flag_start = True

# Check if the string ends with '$'
if len(s)>0 and s.endswith('$'):
    flag_end = True

if len(s)==0:
        s=" "

if flag_start==True:
     s = s[1:]
if flag_end==True:
   s = s[:-1]

like_s2 = ""
# Iterate over the string from the end (backwards)
# for i in range(len(s) - 1, -1,-1):
i = len(s) - 1  # Initialize i here to handle manually in the loop

while i >= 0:
    # print(i)
    # If the character is '*' or '+'
    if s[i] == '*' or s[i] == '+':
        i1 = max(i, i1)
        
        # If the character before '*' or '+' is not `]` or `)`, set istart to i-1
        if s[i - 1] != ']' and s[i - 1] != ')':
            istart = i - 1
            i -= 1  # Decrement i as we are skipping over the `*` or `+`
            continue
        else:
            # If it is `]` or `)`, find the matching `[` or `(`
            starter = s[i - 1]  # The character before the `*` or `+` is either `]` or `)`
            i -= 1  # Move back one step to get the character before `*`
            if starter == ']':
                c_starter = '['
            else:
                c_starter = '('

            # Move backward to find the matching bracket
            while True:
                if s[i] == starter:
                    count += 1
                elif s[i] == c_starter:
                    count -= 1
                if count == 0:
                    istart = i
                    break
                i -= 1  # Continue backward
    else:
        # Handling closing parentheses ')' or closing square brackets ']'
        if s[i] == ')':
            flag = True
            temp = i
        
            while True:
                if s[i] == '^' or s[i] == '*' or s[i] == '+':
                    cursedflag = True
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                if count == 0:
                    if cursedflag:
                        istart = i
                        i1 = max(i1, temp)
                        cursedflag=False
                    flag = False
                    break
                i -= 1
        elif s[i] == ']':
            flag = True
            temp = i
            
            while True:
                if s[i] == '^' or s[i] == '*' or s[i] == '+':
                    cursedflag = True
                if s[i] == '[':
                    count += 1
                elif s[i] == ']':
                    count -= 1
                if count == 0:
                    if cursedflag:
                        istart = i
                        i1 = max(i1, temp)
                        cursedflag=False
                    flag = False
                    break
                i -= 1
    i-=1
# Output the results
print(f"istart: {istart}, i1: {i1}")


# Initialize strings

regex_s = s
# s = s.strip('^').strip('$') 
like_s = s

# Check conditions for i1 and istart
if i1 == -1 and istart == -1:
    regex_s = ""

# If istart is at the start of the string
elif istart == 0:
    if i1 != len(s) - 1:
        like_s = ""
        like_s2 =  s[i1 + 1:]  # Substring from i1+1 to end
    else:
        like_s = ""

# If i1 is at the end of the string
elif i1 == len(s) - 1:
    like_s = s[:istart]   # Substring from 0 to istart, then add '%'

# If both i1 and istart are somewhere in the middle
elif i1 != len(s) - 1 and istart != 0:
    like_s = s[:istart]  # Substring from 0 to istart, then add '%'
    like_s2 = s[i1 + 1:]  # Substring from i1+1 to end, then add '%'



print('\n')
print("regex_s = " + regex_s)
print("like_s = " +like_s)
print("like_s2 = " +like_s2)
print('\n')