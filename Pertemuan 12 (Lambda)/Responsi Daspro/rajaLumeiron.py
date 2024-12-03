def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def IsEmpty(L):
    return L == []

def EvaluateExpression(S):
    if IsEmpty(S):
        return []
    elif FirstElmt(S) == '+':
        return (FirstElmt(Tail(S))) + (LastElmt(S))
    elif FirstElmt(S) == '-':
        if FirstElmt(Tail(S)) > LastElmt(S):
            return FirstElmt(Tail(S)) - LastElmt(S)
        else:
            return LastElmt(S) - FirstElmt(Tail(S))
    elif FirstElmt(S) == '*':
        return (FirstElmt(Tail(S))) * (LastElmt(S))
    elif FirstElmt(S) == '/':
        if FirstElmt(Tail(S)) > LastElmt(S):
            return FirstElmt(Tail(S)) / LastElmt(S)
        else:
            return LastElmt(S) / FirstElmt(Tail(S))
    
print(eval(input()))