def tower_builder(n_floors):
    res = []
    n = " "
    x = "*"
    c = 1
    empt = n_floors-1
    if n_floors <= 1:
        return ['*']
    else:
        for a in range(1,(n_floors+1)):
            res.append(f"{empt*n}{x*c}{empt*n}")
            c += 2
            empt -= 1
        return res
