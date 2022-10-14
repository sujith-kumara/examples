def calculation(plastic,glass,total,exchange):
    no_bottles = 0
    while(total > 0):
        if total > 0 and total >= glass:
            no_bottles += 1
            total -= glass
            total += exchange
        elif total > 0 and total >= plastic:
            no_bottles += 1
            total -= plastic
        else:
            return no_bottles
    
ans = calculation(5,10,100,2)
print(ans)