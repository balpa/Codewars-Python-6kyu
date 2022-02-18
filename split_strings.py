def solution(s):
    chunks = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(s)>0:
        if len(chunks[-1]) == 1:
            chunks[-1] = f"{chunks[-1]}_"
    return chunks
