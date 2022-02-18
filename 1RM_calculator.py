def calculate_1RM(w, r):
    epley = round(w*(1 + (r/30)))
    mcglothin = round((100*w)/(101.3-(2.67123*r)))
    lombardi = round(w*(r**0.1))
    list = [epley,mcglothin,lombardi]
    if r == 1:
        return w
    elif r == 0:
        return 0
    else:
        return max(list)
