def delete_nth(order,max_e):
    final = []
    
    for x in range(len(order)):
        if final.count(order[x]) < max_e:
            final.append(order[x])
    return final
