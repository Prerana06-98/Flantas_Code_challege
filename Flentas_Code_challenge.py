def minimumCost(price, n): 

	
	price = sorted(price) 
	totalCost = 0

	
	for i in range(n - 1, 1, -2): 
		if (i == 2): 
			totalCost += price[2] + price[0] 

		else: 

			
			price_first = price[i] + price[0] + 2 * price[1] 
			price_second = price[i] + price[i - 1] + 2 * price[0] 
			totalCost += min(price_first, price_second) 
 
	if (n == 1): 
		totalCost += price[0] 

	else: 
		totalCost += price[1] 

	return totalCost



T=int(input("Number Of Test Cases"))


while 1<=T<=10:
    price = []
    n = int(input("Enter number of Persons : "))
    if 1<=n<=100000:
        
        for i in range(0, n):
            
            ele = int(input())
            
            price.append(ele) 
            res=all(1<=ele<=1000000 for ele in price)
        
            
        if res:
            print(minimumCost(price, n))
            T=T-1
        else:
            print("Enter the valid cost of person as 1 ≤ A[i] ≤ 1000000")

    else:
        print("Enter the valid number of Persons as 1 ≤ N ≤ 100000")

    

