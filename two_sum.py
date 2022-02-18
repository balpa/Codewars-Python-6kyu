def two_sum(numbers, target):
    sum = 0
    for x in range(0,len(numbers)):
        for i in range(1,len(numbers)):
            sum = numbers[x]+numbers[i]
            if sum == target:
                return [x,i]
