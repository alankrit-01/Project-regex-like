import re
import sre_parse
from anytree import Node, RenderTree

def parse_regex_to_ast(regex):
    try:
        # Parse the regex into a structured representation
        parsed = sre_parse.parse(regex)
        return parsed
    except re.error as e:
        return f"Error parsing regex: {e}"


def build_tree(parsed, parent=None):
    """
    Recursively build a tree structure from parsed regex.
    """
    if parent is None:
        parent = Node("Regex")
    
    for token in parsed:
        if isinstance(token, tuple):
            token_type, token_value = token
            node = Node(f"{token_type}: {token_value}", parent=parent)
            if token_type == "SUBPATTERN":
                _, (start, end, subpattern) = token_value
                sub_node = Node(f"Subpattern {start}-{end}", parent=node)
                build_tree(subpattern, sub_node)
            elif token_type in ("MAX_REPEAT", "MIN_REPEAT"):
                min_repeat, max_repeat, subpattern = token_value
                repeat_node = Node(f"Repeat {min_repeat}-{max_repeat}", parent=node)
                build_tree(subpattern, repeat_node)
        elif isinstance(token, list):
            build_tree(token, parent)
        else:
            Node(str(token), parent=parent)
    return parent

def visualize_regex(regex):
    """
    Parse the regex, build its AST, and render a tree visualization.
    """
    try:
        parsed = sre_parse.parse(regex)
        root = build_tree(parsed)
        for pre, _, node in RenderTree(root):
            print(f"{pre}{node.name}")
    except Exception as e:
        print(f"Error parsing regex: {e}")

# Example usage
if __name__ == "__main__":
    regex = r"[abc][def]"
    visualize_regex(regex)
    # ast = parse_regex_to_ast(regex)
    # print("Parsed AST:")
    # for component in ast:
    #     print(component)


# ^a(bc|de)*f$
    
#     Regex
# ├── AT: AT_BEGINNING
# ├── LITERAL: 97
# ├── SUBPATTERN: (1, 0, 0, [(LITERAL, 98), (LITERAL, 99)])
# │   └── Subpattern 0-0
# │       ├── LITERAL: 98
# │       └── LITERAL: 99
# ├── MAX_REPEAT: (0, MAXREPEAT, [(SUBPATTERN, (1, 0, 0, [(LITERAL, 98), (LITERAL, 99)]))])
# │   └── Repeat 0-MAXREPEAT
# │       └── SUBPATTERN: (1, 0, 0, [(LITERAL, 98), (LITERAL, 99)])
# │           └── Subpattern 0-0
# │               ├── LITERAL: 98
# │               └── LITERAL: 99
# ├── LITERAL: 102
# └── AT: AT_END 
