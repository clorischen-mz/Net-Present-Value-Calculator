#Flow Control

#before loop
print ('Welcome to the Net Present Value Calculator!')
print('')
print('What is your initial investment?')
C0 = input() # This is the initial investment amount
print('What is the discount rate?')
k = input() # This is the discount rate
Sum = 0 # The initial sum for (B-C)/(1+k)**i is set to be 0

#during loop
for i in range(1,4,1):
    print('What is your benefit in year ' + str(i)+ '?')
    B = input() # This is benefit in year i
    print('What is your cost in year ' + str(i)+ '?')
    C = input() # This is cost in year i
    Sum = (B-C)/(1+k)**i + Sum
    

#after loop
NPV = -C0 + Sum
print ('The NPV for your IT project is ' + str(NPV)) # This is NPV amount!
#Determine if the project is accepted, rejected or indifferent
if NPV > 0:
    print('The project may be accepted!')
elif NPV == 0:
    print ('We should be indifferent in the decision whether to accept or reject the project.')
elif NPV < 0:
    print ('The project may be rejected!')
print('Have a nice day!')
