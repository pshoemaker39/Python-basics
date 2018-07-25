
# coding: utf-8

# In[42]:


from IPython.display import Image


# In[37]:


#3.25

def amChecker(lst):
    for l in lst:
        if((ord(l[0].upper()) > 64) & (ord(l[0].upper()) < 78)):
            print(ord(l[0]))
            print(l)


# In[40]:


lst = ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin','Zebra','elk']


# In[41]:


amChecker(lst)


# In[31]:


p = "mutable types.png"
Image(filename = p, width=500, height=500)


# In[43]:


#escapes
"John\'s Book"


# In[44]:


ord('A')


# In[45]:


ord('a')


# In[63]:


#4.22
def month(m):
    mos = ['Jan',
           'Feb',
           'Mar',
           'Apr',
           'May',
           'Jun',
           'Jul',
           'Aug',
           'Sep',
           'Oct',
           'Nov',
           'Dec']
    
    mos2 = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
    mos2 = mos2.split(' ')
    
    print(mos2[m-1])
    
    return(mos[m-1])


# In[64]:


month(1)


# In[60]:


try:
    print(100)
except:
    pass


# In[67]:


#printing on same line example

def install_xxx():
    print("Installing XXX...      ", end="************", flush=True)

install_xxx()
print("[DONE]")


# In[76]:


lst = ['Alan Turing', 'Ken Thompson', 'Vint Cerf']


# In[80]:


for name in lst:
    fl = name.split()
    print('{:50} {:40}'.format(fl[0][:3], fl[1]))


# In[88]:


print('{:b}'.format(900))


# In[89]:


p = "format types.png"
Image(filename = p, width=500, height=500)


# In[92]:


print('{:7.2f}'.format(1000000000000))


# In[104]:


x = 10.0
y = 8
print('{1:<7.2f} {0:}'.format(x, y))


# In[105]:


f = open('test.txt', 'r')


# In[106]:


f


# In[107]:


f.read()


# In[108]:


txt = 'Some new text'


# In[111]:


f = open('test.txt', mode='w')


# In[112]:


f.write(txt)


# In[113]:


f.close()


# In[114]:


f = open('test.txt', mode='r')


# In[115]:


f.read()


# In[116]:


txt = '[I 20:09:12.257 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:09:24.727 NotebookApp] Saving file at /401/1 Week - Tuesday.ipynb\n[I 20:13:12.253 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:15:12.774 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:17:12.257 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:19:12.256 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:23:12.273 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:25:12.269 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:27:12.273 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n[I 20:29:12.268 NotebookApp] Saving file at /401/2 Week - Tuesday.ipynb\n'


# In[117]:


f = open('test.txt', mode='a')


# In[118]:


f.write(txt)


# In[119]:


f.close()


# In[121]:


f = open('test.txt', mode='r')


# In[122]:


f.read()


# In[123]:


p = "file modes.png"
Image(filename = p, width=500, height=500)


# In[128]:


f.close()


# In[129]:


f = open('test.txt')


# In[131]:


f.close()


# In[133]:


f = open('test.txt')


# In[134]:


f.read(1)


# In[135]:


f.readlines(3)


# In[136]:


f.close()


# In[137]:


f = open('test.txt')


# In[138]:


f.read(-1)


# In[139]:


f.read(-1)

