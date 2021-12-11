def solution(S):
    stack_of_brackets = [] * len(S)
    for character in S:
        if character == "(" or character == "{" or character == "[":
            stack_of_brackets.append(character)
        elif character == "]" or character == "}" or character == ")":
            if len(stack_of_brackets) <= 0:
                return 0
            elif character == "]" and stack_of_brackets[-1] == "[" or character == "}" and stack_of_brackets[-1] == "{" \
                    or character == ")" and stack_of_brackets[-1] == "(":
                stack_of_brackets.pop()
    if len(stack_of_brackets) == 0:
        return 1
    else:
        return 0
