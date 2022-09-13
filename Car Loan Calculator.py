print("Welcome to our car loan calculator, insert details below to begin")
vehicleprice = float(input("enter vehicle price"))
tradeinvalue = float(input("enter trade in value"))
downpayment = float(input("enter down payment"))
termofloan = int(input("enter term of loan in months"))
totalprice = vehicleprice - tradeinvalue - downpayment
monthlypayment = totalprice/termofloan
print ("This is your total price and monthly payment based on the values given")
print ("\n" "vehicle price" + str(vehicleprice))
print ("\n" "tradeinvalue" + str(tradeinvalue))
print ("\n" "downpayment" + str(downpayment))
print ("\n" "termofloan" + str(termofloan))
print ("\n" "totalprice" + str(totalprice))
print ("\n" "monthly payment" + str(monthlypayment))       
