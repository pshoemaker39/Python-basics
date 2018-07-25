
# coding: utf-8

# In[1]:


import sys


# In[2]:


sys.version_info


# In[7]:


def ages(anniesAge, elliesAge):
    return(anniesAge - elliesAge)


# In[8]:


ages(25, 21)


# In[9]:


def totals(one, two, three):
    return(one+two+three)


# In[10]:


def area(width, length):
    return(width*length)


# In[11]:


def powers(base, exponent):
    return(base^exponent)


# In[33]:


def minimum(numList):
#     p = 0
#     for x in numList:
#         if(x<p):
#             p=x
    return(min(numList))


# In[34]:


nl = [3,1,8,-2,5,-3]
minimum(nl)


# In[16]:


def badMath():
    return(3==(4-2))


# In[17]:


badMath()


# In[18]:


def manualDivision(num, den, rem=None, case=1):
    if (case == 1):
        return((num//den)==rem)
    else:
        return((num%den)==rem)


# In[19]:


manualDivision(17,5,3)


# In[20]:


manualDivision(17,5,3, case=2)


# In[25]:


def evens(target):
    return((target%2)==0)


# In[26]:


evens(284)


# In[29]:


def both(target, divisor):
    return(evens(target), manualDivision(target, divisor))


# In[30]:


both(284, 3)


# In[36]:


target = 'fkjdfkjdkfvuieu9'


# In[38]:


"z" in target


# In[39]:


target


# In[62]:


def strElements(target):
    for x in target:
        print(x)
    
    i=len(target)
    
    while(i>0):
        print(target[i-1])
        i = i-1;
    


# In[63]:


strElements("Apple")


# In[65]:


a = [1, "kldsfks",["fdsjf",9]]


# In[66]:


b = 9


# In[70]:


c = ["fdsjf",9]


# In[68]:


b in a[2]


# In[71]:


c in a


# In[72]:


min(target)


# In[73]:


max(target)


# In[74]:


help(list)


# In[75]:


print(hex(id(target)))


# In[76]:


t = 0x108b138a0


# In[77]:


t


# In[79]:


lst = [150.05, 100.00, 80.99, 99.11, 1000.50]


# In[80]:


lst.append(900.80)


# In[81]:


lst


# In[82]:


sum(lst)/len(lst)


# In[83]:


minVal = min(lst)


# In[84]:


lst[lst.index(min(lst))]


# In[85]:


lst.sort(reverse=True)


# In[86]:


lst


# In[87]:


x ="alskfjakf"


# In[88]:


print(hex(id(x)))


# In[89]:


x = "adjfakdj"


# In[93]:


print(hex(id(x)))

