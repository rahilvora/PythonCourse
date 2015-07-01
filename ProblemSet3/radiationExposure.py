def f(x):
    import math
    return 60*math.e**(math.log(0.5)/55.6 * x)
def radiationExposure(start, stop, step):
    rng = stop - start
    noOfRect =  rng / step
    total = 0
    for a in range(0,int(noOfRect)):
        total += f(start)*step
        start += step
    return total
    
print radiationExposure(60, 120, 0.5)
