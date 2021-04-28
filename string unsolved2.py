def remove_char(str,n):
    f=str[:n]
    l=str[n+1:]
    return f+l
print(remove_char('python',3))
