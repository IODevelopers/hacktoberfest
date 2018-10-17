from pycapital.pycapital import capital

print("     ******************************")
print("*  KNOW THE CAPITAL CITY OF A COUNTRY  *")
print("       Type stop to Quit\n  ")

while True:
		#declaration of variable and accepting user input
		countryName=input("Enter name of country: ")
		#Terminate the program
		if countryName.lower()=='stop':
			break
		elif capital(countryName)==False:
			print("The country '{0}' you provided is not valid or not included in our list of countries!".format(countryName))
		#checking if field is empty!  
		else:
			#Display the country with it corresponding capital
			print("The capital city of {} is {} \n".format(countryName,capital(countryName)))