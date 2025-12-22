### *args allows a function to accept any number of positional arguments.

##### args is a tuple.


def total_sum(*args):  
    print(sum(args))  

total_sum(1, 2, 3)      # 6  
total_sum(5, 10, 15)    # 30  


### **kwargs allows a function to accept any number of keyword arguments.

#### **kwargs is ALWAYS a dictionary.  

Python automatically does this behind the scenes:  
Collects all keyword arguments  
Stores them in a dictionary  
Assigns that dictionary to the name kwargs  

❗ Important clarification  
❌ kwargs is NOT special syntax by itself  
This:  
  
kwargs  

   
is just a variable name.  
  
✅ The magic is in **  
  
*args → tuple  
  
**kwargs → dictionary  

