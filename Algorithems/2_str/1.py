l=str(input())
t=str(input())
for i in range(len(t)):
    sim = t[i]
    if sim in l:
        l = l.replace(sim, '', 1)
    else:
        print(sim)
        break