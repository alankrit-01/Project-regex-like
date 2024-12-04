def get_part_before_repetition(regex):
    if not regex.startswith("^"):
        raise ValueError("Regex must start with ^.")
    
    stack = []  
    part_before_repetition = []
    i = 1  # Start after the '^'
    temp_list=[]
    inside=False

    while i < len(regex):
        char = regex[i]
        
        # Handle opening parenthesis
        if char == '(':
            stack.append('(')
            inside=True
            temp_list.append(char)
        
        # Handle closing parenthesis
        elif char == ')':
            if not stack:
                raise ValueError("Unmatched closing parenthesis in regex.")
            stack.append(')')
            temp_list.append(char)
            inside=False
        
        elif char == '*' and stack and stack[-1] ==')':
            break   
        
        # Add character to part_before_repetition if stack is empty or not '*'
        # elif char == '(' or (not stack and char != '*'):
        #     part_before_repetition.append(char)
        else:
            if inside:
                temp_list.append(char)
            elif not stack:
                part_before_repetition+=temp_list
                temp_list.clear()
                stack.clear()
                part_before_repetition.append(char)
            else:
                part_before_repetition.append(char) 
        i += 1

    return ''.join(part_before_repetition)

if __name__ == "__main__":
    regex = "^ab(def)g"
    result = get_part_before_repetition(regex)
    print(f"Part before repetition: {result}")
