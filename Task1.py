outlist = []
def lister(li):
    for i in li:
        if type(i) is list:
            lister(i)
        else:
            outlist.append(i)
    return outlist
