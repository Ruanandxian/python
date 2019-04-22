def name (L):
    if L==[]:
        return None,None
    else:
        min=L[0]
        max=L[0]
        for x in L:
            if x>max:
                max=x
            if x<min:
                    min=x
        return max,min
