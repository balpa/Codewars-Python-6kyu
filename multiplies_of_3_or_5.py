def solution(number):
    store = []
    for i in range(0,number):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 and i % 5 == 0:
                store.append(i)
            else:
                store.append(i)
    return sum(store)
