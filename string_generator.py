import itertools
import oracledb
import time

from Full_Traversal_Cursed import regex_s,like_s,like_s2,i1,i2,s,flag_end,flag_start

# Replace these with your actual values
user = "SYS"    # Your Oracle username
password = "mypassword1"  # Your Oracle password
dsn = "localhost:1521/ORCLCDB"  # DSN (e.g., "localhost:1521/orclpdb1")

# Establish the connection
connection = oracledb.connect(user=user, password=password, dsn=dsn, mode=oracledb.SYSDBA)





# Function to generate all possible combinations from a regex pattern with character classes
def generate_combinations_from_regex(regex):
    # Strip the starting (^) and ending ($) anchors
    regex = regex.strip('^').strip('$')
    
    # Step 1: Find all the character classes in the regex
    char_classes = []
    index = 0
    
    while index < len(regex):
        if regex[index] == '[':
            # Find the end of the character class
            end_index = regex.find(']', index)
            if end_index != -1:
                char_classes.append(regex[index + 1:end_index])  # Capture the characters inside []
                index = end_index
        index += 1
    
    # Step 2: Generate all combinations of characters inside each class
    combinations = []
    for char_class in char_classes:
        combinations.append(list(char_class))  # Each class is just a list of possible chars
    
    # Step 3: Use itertools.product to generate all possible combinations from the lists
    all_combinations = list(itertools.product(*combinations))

    # Step 4: Rebuild the strings by replacing the character classes with each combination
    generated_strings = []
    for combo in all_combinations:
        result_string = regex
        for i, char_class in enumerate(char_classes):
            # Replace each character class with the combination value
            result_string = result_string.replace(f"[{char_class}]", combo[i], 1)
        generated_strings.append(result_string)
    
    return generated_strings

# Test with the regex '^ab[de]e[fk]$'
# regex = '^ab[de]*e[fk]*$'  # Matches strings like abdef, abeef, abdek, abeek


start_time = time.time()

query = "SELECT count(*) FROM Q1 WHERE "


# Generate combinations and print the result
if len(like_s)>0:
    generated_strings = generate_combinations_from_regex(like_s)
    print("Generated strings:")
    for string in generated_strings:
        print(string)
    if i1!=-1:
        if flag_start == True:
            like_conditions = [f"NAME LIKE '{string}%'" for string in generated_strings]
           
        else:
            like_conditions = [f"NAME LIKE '%{string}%'" for string in generated_strings]

    else:
        if flag_start == True:
            if flag_end == True:
                like_conditions = [f"NAME LIKE '{string}'" for string in generated_strings]
            else:
                like_conditions = [f"NAME LIKE '{string}%'" for string in generated_strings]
        else:
            if flag_end == True:
                like_conditions = [f"NAME LIKE '%{string}'" for string in generated_strings]
            else:
                like_conditions = [f"NAME LIKE '%{string}%'" for string in generated_strings]

    # query = "SELECT * FROM SAMPLE_TABLE WHERE (" + " OR ".join(like_conditions)
    query = query + '( '
    query2 = query+ " OR ".join(like_conditions)
    query2=query2 + ')'
    query = query2





if len(like_s2)>0:
    generated_strings2= generate_combinations_from_regex(like_s2)
    print("Generated strings2 :")
    for string in generated_strings2:
        print(string)

    # if i1!=-1: 
    #     if flag_end == True:
    #         like2_conditions = [f"NAME LIKE '{string}'" for string in generated_strings2]
    #     else:
    #         like2_conditions = [f"NAME LIKE '%{string}%'" for string in generated_strings2]
    # else:
    if flag_end == True:
        like2_conditions = [f"NAME LIKE '%{string}'" for string in generated_strings2]
    else:
        like2_conditions = [f"NAME LIKE '%{string}%'" for string in generated_strings2]

    
    if(len(like_s)>0):
        query = query + ' AND ('
    else: 
        query = query + ' ('

    query2= query + " OR ".join(like2_conditions)

    query2 = query2 + ')'
    query = query2












if len(regex_s)>0:
    if len(like_s)!=0 or len(like_s2)!=0 :
        query=query + " AND REGEXP_LIKE(NAME,'" + regex_s + "')"
    else :
        query = query + " REGEXP_LIKE(NAME,'" + regex_s + "') "


# Print the query to check if it's correct
print("Generated Query:")
print(query)


print('\n')




# def star_checking(regex):
#     # Find the index of the first occurrence of '*'
#     first_star_index = regex.find('*')

#     # Find the index of the last occurrence of '*'
#     last_star_index = regex.rfind('*')

#     # Print the results
#     print(f"First occurrence of '*' is at index: {first_star_index}")
#     print(f"Last occurrence of '*' is at index: {last_star_index}")


#     # Check if '*' is found
#     if first_star_index != -1:
#         # Check if the character before '*' is ']'
#         if first_star_index > 0 and regex[first_star_index - 1] == ']':
#             # Find the nearest '[' before the '*' (search backward)
#             open_bracket_index = regex.rfind('[', 0, first_star_index)
        
#             # If '[' is found before the '*', return its index
#             if open_bracket_index != -1:
#                 print(f"Nearest '[' before '*' is at index: {open_bracket_index}")
#             else:
#                 print("No '[' found before '*'")
#         else:
#             # If '*' is not preceded by ']', return index - 1
#             print(f"Character before '*' is not ']', returning index-1: {first_star_index - 1}")
#     else:
#         print("The character '*' is not present in the string.")







# Execute the query
cursor = connection.cursor()
cursor.execute(query)
result_like = cursor.fetchall()
end_time = time.time()

Time_Like = end_time - start_time
print("Query for Like :" + query)
print("Time taken by Like : " + str(Time_Like))
print('\n')
# print(result_like)

#Time for regex direct Regex
start_time = time.time()
regex_query =  f"select count(*) from Q1 where REGEXP_LIKE(NAME, '{s}')"
cursor.execute(regex_query)
result_regex=cursor.fetchall()
end_time = time.time()

Time_Regex = end_time - start_time 
print("Query for Regex : " + str(regex_query))
print("Time taken by regex: " + str(Time_Regex))
print('\n')

print("No. of rows in Result : "+str(result_regex[0][0]))
print('\n')

Total_rows=  f"select count(*) from Q1"
cursor.execute(Total_rows)
result_total=cursor.fetchall()

print("No. of rows in Table : "+str(result_total[0][0]))
print('\n')


print(flag_start)
print(flag_end)

# Q1 - SCHEMA(NAME-varchar(10000)) Selectivity- 0.25 
# s = "a[bc]de(ab)*fgr*hq"

#  Follows-  abdeababababababababababababababababababababababfgrrrhq
# Not follows- abdeababababababababababababababababababababababfgrrrhp
# Not follows- abdeabababababababababababababababababababababafgrrrhp
# Not follows- abdababababababababababababababababababababababfgrrrhp


# Q2 - SCHEMA(NAME,varchar(10000)) Selectivity- 1.0 

# s = "a[bc]de(ab)*fgr*hq"
#  Follows-  abdeababababababababababababababababababababababfgrrrhq