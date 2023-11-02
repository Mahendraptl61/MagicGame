import random
import sys
import time
lst=[[8,9,10,
     11,12,13,
     14,15,24,
     25,26,27,
     28,29,30   
     ],
    [4,5,6,
     7,12,13,
     14,15,20,
     21,21,23,
     28,29,30,     
     ],
     [2,3,6,
      7,10,11,
      14,15,18,
      19,22,23,
      26,27,30,
      ],
      [1,3,5,
       7,9,11,
       13,15,17,
       19,21,23,
       25,27,29,
       ],
      
      [ 16,17,18,
        19,20,21,
        22,23,24,
        25,26,27,
        28,29,30
      ],
      [4,22,22,
        22,22,22,
        22,22,22,
        22,22,22,
        22,22,22
      ]
      ]



print ("\nWelcome to Magic Game ......")
print ("\n\nConsider Any Number In Between 1 to 30......")
Flag=input('Do you considered number then press Y or N')
star=''
magicNumber=0
count=0
if Flag.lower()=='y': 
   random.shuffle(lst) 
   for data  in lst: 
       
      print (data)
      print ("\n\nIs Your number In The above set then press Y "),
      choice=input('')   
      if choice.lower()=='y':
         magicNumber=magicNumber+data[0] 
   print ("\n\nWe will be finding your number....")  
   time.sleep(5)       
   print ("Your considered number is ",magicNumber )         
   
   
else:
    print ("No you have not considered any number in between 1 to 30, game will exit... ")
    sys.exit(0)
#for data in lst:
       














