# find the minimum and maximum number
seq = [] 
  
# number inputs 
n = int(input("Enter number of inputs : ")) 
   
for i in range(0, n): 
    nlist = int(input())  
    seq.append(nlist) # adding the inputs to the list

max = seq[0]
min = seq[0]

for i in range(1, n):
    if max < seq[i]:
        max = seq[i]
        
    if min < seq[i]:
        min = min
        
    else:
        max = max
        min = seq[i]

print('max =' , max)  # maximum number
print('min =' , min)  # minimum number
    
            
     



