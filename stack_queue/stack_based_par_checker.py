def par_checker(symbol):
    stack=[]
    result=True
    for item in symbol:
        if item in '([{':
            stack.append(item)
        else:
            if item in ')]}' and len(stack)>0:
                top=stack.pop()
                if not matches(top,item):
                    result=False
                    break

            elif item in ')]}' and len(stack)==0:
                result=False
                break
    else:
        if len(stack)>0:
            result=False
        elif len(stack)==0:
            result=True

    return result

def matches(open,close):
    openers='[{('
    closers=']})'
    return openers.index(open)==closers.index(close)

print(par_checker('[{()]'))