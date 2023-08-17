yearlydividend = [] #user input
for i in range(5):
    value = float(input("enter yearly dividends:"))
    yearlydividend.append(value)
    if len(yearlydividend) == 5:
        break
#print(yearlydividend)
eps = [] #user input
for i in range(5):
    value = float(input("enter yearly eps:"))
    eps.append(value)
    if len(eps) == 5:
        break
#print(eps)
dividendpayoutratio = [a/b for a, b in zip(yearlydividend, eps)]


epsgrowthrate = [(eps[i+1]-eps[i])/eps[i] for i in range(len(eps)-1)]

averageepsgrowthrate = sum(epsgrowthrate)/len(epsgrowthrate)

averagegrowthdividendpayout = sum(dividendpayoutratio)/len(dividendpayoutratio)

lasteps = eps[-1]
forecastedeps = [lasteps]


for _ in range(5):
    next_eps = forecastedeps[-1] * (1+averageepsgrowthrate)
    forecastedeps.append(next_eps)
#print(forecastedeps)

forecateddividend= [averagegrowthdividendpayout] * 5


forecateddividend.insert(0,dividendpayoutratio[-1])
#print(forecateddividend)

estimatedcashdividend = [a*b for a, b in zip(forecastedeps, forecateddividend)]

presentvaluefactor = float(input("risk free rate: ")) # user input
numberofperiod= 6 
discountrates = []
discountrates.append(1)

for i in range (1,numberofperiod):
    discount = discountrates[i-1]/(1+presentvaluefactor)
    discountrates.append(discount)

#print(discountrates)

discounteddividendpresent = [a*b for a, b in zip(estimatedcashdividend, discountrates)]

#print(discounteddividendpresent)

estimatedpresent = sum(discounteddividendpresent[1:6])

#print(sum(discounteddividendpresent[1:6]))

pEratio = [] #user input
for i in range(5):
    value = float(input("enter yearly eps:"))
    pEratio.append(value)
    if len(pEratio) == 5:
        break
averagepE = sum(pEratio)/len(pEratio)
#print(averagepE)

presentvaalueinfive = forecastedeps[-1] * averagepE * discountrates[-1]

#print(presentvaalueinfive)

intrinsicvalue = estimatedpresent + presentvaalueinfive

print(intrinsicvalue)

