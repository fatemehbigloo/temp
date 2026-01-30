import random

global list_chart
#متغیر
list_chart = [1,2,3,4,5,6,7,8,9]
empy_list = []
hol = 0 

for i in range(0,9,1) :
    print(f'{(i+1):4}', end='')
    if (i+1) % 3 ==0:==
        print()
#-----------------------------------------------------------------------------
#تابع
def start2():
    for i in range(len( list_chart)) :
        print(f'{list_chart[i]:4}', end='')
        if (i+1) % 3 ==0:
            print()
       
    tahlil()        
  

#-----------------------------------------------------------------------------          
def tahlil():
    global end_for2, end_for1
    end_for2 = 0
    end_for1 = 0
   
    
    
        #amod
    if end_for1 != 1:
        for i in range(3):
            c1=0
            for j in range(i, 9, 3):
                if list_chart[j] == 'o' :
                    c1+=1
                if c1 ==3 :
                    print('you are win')
                    end_for1 = 1
                   
                    break
                
                    
    if end_for1 != 1:
        #ofogh
        for i in range(0, 9,3):
            c2=0
            for j in range(i, i+3):
                if list_chart[j] == 'o' :
                    c2+=1
                if c2 ==3 :
                    print('you are win')
                    end_for1 = 1
                    
                    break
                    
                
    if end_for1 != 1:
        #movarab chap
        global movarab_chap, movarab_rast
        movarab_chap = 0
        movarab_rast = 0
        if end_for1 != 1:
            for i in range(0,9,4):
                if list_chart[i] == 'o':
                    movarab_chap += 1
                if movarab_chap == 3 :
                    print('you are win')
                    end_for1 = 1
                   
                    break
                
                
        
    if end_for1 != 1:
    #movarab rast
        for i in range(2,7,2):
            if list_chart[i] == 'o':
                movarab_rast += 1
            if movarab_rast == 3 :
                print('you are win')
                end_for1 = 1
               
                break
            

    

#.......computer
    if end_for1 != 1:
        for i in range(3):
            c1=0
            for j in range(i, 9, 3):
                if list_chart[j] == 'x' :
                    c1+=1
                if c1 ==3 :
                    print('ha ha ha I am win')
                    end_for1 = 1
                   
                    break
                
    if end_for1 != 1:
        #ofogh
        for i in range(0, 9,3):
            c2=0
            for j in range(i, i+3):
                if list_chart[j] == 'o' :
                    c2+=1
                if c2 ==3 :
                    print('ha ha ha I am win')
                    end_for1 = 1
                   
                    break
                
                
    if end_for1 != 1:
        #movarab chap
        global cmovarab_chap, cmovarab_rast
        cmovarab_chap = 0
        cmovarab_rast = 0
        if end_for1 != 1:
            for i in range(0,9,4):
                if list_chart[i] == 'o':
                    cmovarab_chap += 1
                if cmovarab_chap == 3 :
                    print('ha ha ha I am win')
                    end_for1 = 1
                    
                    break
                
                
        
    if end_for1 != 1:
    #movarab rast
        for i in range(2,7,2):
            if list_chart[i] == 'o':
                cmovarab_rast += 1
            if cmovarab_rast == 3 :
                print('ha ha ha I am win')
                end_for1 = 1
                
                break
    else:
        if end_for1 !=1:
            print('mosavi')
            
        
    
    
#---------------------------------------------------------------------------------
def start1():
    
    global rand_chart, matchin_char, user_number_chart, user_character
    matchin_char = 'x'
    user_character ='o'
  
    for i in range(1, 10, 2):
        #rand_chart = random.randint(1, 9)
        user_number_chart =int(input("please enter your number "))
        
        
        
        list_chart[user_number_chart-1] = user_character
        empy_list.append(user_number_chart)
        #start2()
        
        
        
        empy_cell = [cell for cell in list_chart if cell!='o' and cell != 'x']        
        if empy_cell :
            rand_chart = random.choice(empy_cell)
            list_chart[rand_chart-1] = matchin_char
            start2()
        else:
            print('game finished')
    return rand_chart, matchin_char, user_number_chart, user_character


#---------------------------------------------------------------------------
start1()
start2()
# print(' for playing again, enter g...  ')
# again = input()
# if again == 'g':
#     start1()
#     start2()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    