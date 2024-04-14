#--------------------------------necessary Declarations and importings------------------------------------
import random
space=100
# sizes=['-',17,'-',11,'-',18]
# positions=[0,15,32,45,56,82,100]
last_allocated=-1

# sizes=[11, 4, 17, '-', 11, '-', 18]
# positions=[0, 11, 15, 32, 45, 56, 82, 100]

sizes=['-']
positions=[0,100]

#-------------------------------------Functions-----------------------------------------------------
#Function for printing the processes
def print_processes(processes):
    for process in processes:
        print('|',end='')
        print('-'*(process//2),process,'-'*(process//2),end='')
    print('|')

#Functions for allocation
def next_fit(process):
    global last_allocated
    print('Process Size: ',process)
    for i in range(last_allocated+1,len(positions)):
        if i== len(positions)-1:
            break
        if sizes[i]=='-' and (positions[i+1]-positions[i])>=process:
            last_allocated=i
            last_allocated=last_allocated % len(positions)
            print('last_allocated :',last_allocated)
            return i,positions[i]       
    return -1,-1

def worst_fit(process):
    print('Process Size: ',process)
    largest_position=-1
    largest_index=-1
    largest_size=-1
    for i,position in enumerate(positions):
        if i== len(positions)-1:
            break
        if sizes[i]=='-' and (positions[i+1]-positions[i])>=process:
            if positions[i+1]-positions[i] > largest_size:
                largest_size=positions[i+1]-positions[i]
                largest_index=i
                largest_position=position
    return largest_index,largest_position

def first_fit(process):
    print('Process Size: ',process)
    for i,position in enumerate(positions):
        if i== len(positions)-1:
            break
        if sizes[i]=='-' and (positions[i+1]-positions[i])>=process:
            return i,position
    return -1,-1

def best_fit(process):
    print('Process Size: ',process)
    smallest_position=-1
    smallest_index=-1
    smallest_size=10000
    for i,position in enumerate(positions):
        if i== len(positions)-1:
            break
        if sizes[i]=='-' and (positions[i+1]-positions[i])>=process:
            if positions[i+1]-positions[i] < smallest_size:
                smallest_size=positions[i+1]-positions[i]
                smallest_index=i
                smallest_position=position
    return smallest_index,smallest_position

#function for updating the size and position array after the allocation
def insert(process,i,position):
    print('Position Selected: ',position,'Size of block: ',positions[i+1]-positions[i])
    if sizes[i]=='-' and (positions[i+1]-positions[i])==process:
        sizes[i]=process
    elif sizes[i]=='-' and (positions[i+1]-positions[i])>process:
        sizes[i]=process
        pos=position+process
        positions.insert(i+1,pos)
        # space= positions[i+2]-positions[i+1]
        space='-'
        sizes.insert(i+1,space)

def remove():
    while True:
        random_index = random.randint(0, len(positions) - 2) #randomly selecting index from 0 to 2nd last element
        if sizes[random_index]!='-':
            sizes[random_index]='-'
            break

# def remove():
#         random_index = random.randint(0, len(positions) - 2) #randomly selecting index from 0 to 2nd last element
#         if sizes[random_index]!='-':
#             sizes[random_index]='-'

def compact():
    global positions
    global sizes
    i=0
    j=i
    while i in range(len(sizes)):
      if sizes[i]!='-':
        sizes[i],sizes[j]=sizes[j],sizes[i]
        i=i+1
        j=j+1
      else:
        i=i+1

    sizes = sizes[0:j]+['-']
    positions=[0]
    for pos in sizes:
      if pos=='-':
        positions.append(100)
      else:
        element=positions[-1]+pos
        positions.append(element)
    
    print('position: ',positions,'sizes: ',sizes)

    global last_allocated
    last_allocated=-1

while True:
    print('Choose the allocation type : ','1 : Best Fit','2 : First Fit','3 : Worst Fit','4 : Next Fit',end='\n')
    choice=input()
    while True:
      process = random.randint(1,100)
      if choice=='1':
        i,position=best_fit(process)
      elif choice=='2':
        i,position=first_fit(process)
      elif choice=='3':
        i,position=worst_fit(process)
      elif choice=='4':
        i,position=next_fit(process)

      if i==-1:
        print('Miss')
        print('1 : Compact','2 : Stop', end='\n')
        ch=input()
        if ch=='1':
          compact()
          continue
        else:
          break

      insert(process,i,position)
      print('position: ',positions,'sizes: ',sizes)
      remove()
      print('Eliminating a process randomly')
      print('position: ',positions,'sizes: ',sizes)
      print('\n')


































# i,position=worst_fit(11)
# print(i,position)
# insert(11,i,position)
# print(positions,sizes)

    # #perfroming compaction
    # compact=[]
    # new_positions=[]
    # while i in range(len(positions)):
    #     if sizes[i]=='-':
    #         start=positions[i]
    #         while sizes[i]!='-':
    #             i=i+1
    #         end=positions[i-1]
    #         compact.append('-')
    #         new_positions.append(start)
    #         new_positions.append(end)
    #     else:
    #         compact.append(sizes[i])
    #         new_positions.append(positions[i])



# for i,position in enumerate(positions):
#     print(i)





# process = random.randint(1,100)
# def insert(process,positions,sizes):
#     print(process)
#     for i,position in enumerate(positions):
#         if i== len(positions)-1:
#             break
#         if sizes[i]=='-' and (positions[i+1]-positions[i])==process:
#             sizes[i]=process
#             break
#         elif sizes[i]=='-' and (positions[i+1]-positions[i])>process:
#             sizes[i]=process
#             pos=position+process
#             positions.insert(i+1,pos)
#             space= positions[i+2]-positions[i+1]
#             sizes.insert(i+1,space)
#             break

# insert(11,positions,sizes)
# print(positions,sizes)