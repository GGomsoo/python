while True:
    words = input()
    my_stack = []

    if words == ".":
        break

    for w in words:
        if w == "(" or w == "[":
            my_stack.append(w)

        if w == ")":
            if len(my_stack) != 0 and my_stack[-1] == "(":
                my_stack.pop()
            else:
                my_stack.append(w)
        
        if w == "]":
            if len(my_stack) != 0 and my_stack[-1] == "[":
                my_stack.pop()
            else:
                my_stack.append(w)
        
        if w == ".":
            break

    if len(my_stack) == 0:
        print("yes")
    else:
        print("no")