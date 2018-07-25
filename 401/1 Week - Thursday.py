
# coding: utf-8

# In[28]:


import math


# # Class Example
# 
# Poblem 1
# 
# (Function)
# 
# Interest on a credit card’s unpaid balance is calculated using the average daily balance. Suppose that the netBalance is the balance shown in the bill, payment is the payment made. d1 is the number of days in the billing cycle, and d2 is the number of days’ payment is made before the billing cycle. Then, the average daily balance is:
# 
# averageDailyBalance = (netBalance * d1 – payment * d2)/d1
# 
# if the interest rate per month is, say 0.0152, then the interest on the unpaid balance is:
# 
# interest = averageDailyBalance * 0.0152
# 
# Write a program that accepts as input netBalance, payment, d1, d2, and interest rate per month. The program outputs the interest.
# 
# The program must use a function, calAverageDailyBal, to calculate and return averageDailyBalance.
# 
# Problem2
# 
# (If/else)
# 
# A box of cookies can hold 24 cookies, and a container can hold 75 boxes of cookies. 
# Write a program that prompts the user to enter the total number of cookies. 
# The program then outputs the number of boxes and the number of containers to ship the cookies. 
# If the last box is not a full box, discard it and output the number of leftover cookies. 
# Similarly, if the last container contains less than the number of specified boxes, you can discard it and output the number of leftover boxes

# In[2]:


#Problem 1
def getBalanceData():
    'gets balance data from user'
    
    netBalance = input("Enter balance: ")
    if(netBalance =='exit'):
        return None
    else:
        netBalance = float(netBalance)
    payment = float(input("Enter payment: "))
    d1 = int(input("Days in cycle: "))
    d2 = int(input("Days before billing cycle: "))
    interest = float(input("Interest: "))
    
    calAverageDailyBal(netBalance, payment, d1, d2, interest)

def calAverageDailyBal(netBalance, payment, d1, d2, interest):
    'returns interest amount based on user input'

    averageDailyBalance = ((netBalance*d1)-(payment*d2))/d1
    
    interestAmount = averageDailyBalance*interest
    
    print("net balance: {}, interest amount: {}".format(netBalance, interestAmount))    
    
    return(interestAmount)

getBalanceData()


# In[ ]:


getBalanceData()


# In[12]:


#Problem 2

def getCookies():
    typeCorrect = False
    while(typeCorrect != True):
        cookies = input("Total number of cookies? ")
        try:
            cookies = int(cookies)
            typeCorrect = True
        except:
            typeCorrect = False
    return (cookies)
            
def cookieCalculator(cookies):
    boxSize = 24
    containerSize = 75
    
    boxes = (cookies//boxSize)
    lo_boxes = (cookies%boxSize)
    
    containers = (boxes//containerSize)
    lo_containers = (boxes%containerSize)
    
    return("Complete Boxes: {}, Left Over Cookies: {}, Complete Containers: {}, Left Over Boxes: {}".format(boxes, lo_boxes, containers, lo_containers))


cookieCalculator(getCookies())


# In[14]:


def tuples(c,d):
    return(c*10, d*10)

a,b = tuples(5, 10)


# In[15]:


print(a)
print(b)


# In[13]:


x = input("check types: ")
print(type(x))


# In[5]:


x = 5
y = int(6)


# In[6]:


x*y


# In[11]:


z = y/x
print(z)


# In[9]:


x**z


# In[10]:


x*z


# In[12]:


b = int()


# In[13]:


b


# In[14]:


price = 5.9


# In[15]:


price2 = int(price)


# In[20]:


r = int(price2/price)


# In[21]:


r


# In[22]:


float(r)


# In[25]:


myString = 'String'


# In[41]:


x = list()
i = 0
r = ''

while(i<len(myString)):
    print(myString[i])
    x.append(myString[i])
    i=i+1

x.reverse()

for y in x:
    r=r+y

print(r)
    


# In[42]:


a = 3


# In[43]:


b = 4


# In[52]:


c = math.sqrt(a**2 + b**2)


# In[45]:


c


# In[56]:


type(c) == float


# In[109]:


#for i in range(begin, end(<), increment)
for value in range(2,16,100):
    print(value)


# In[116]:


name = 'hello'
for char in range(len(name)-1,-1,-1):
    print(name[char])


# In[3]:


a = 9


# In[4]:


b = a


# In[5]:


b = 10


# In[6]:


a


# In[1]:


b

