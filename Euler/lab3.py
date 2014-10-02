total = 0

#loop from 1 to 1000
for i in range(1,1000):
  #if remender is 0 after dividing by 3 or 5
  if i %3 == 0 or i%5 == 0:
    #i is added to total
    total= i + total

print(total)
      
