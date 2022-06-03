# *
# **
# ***
# ****
# *****

#Çift döngü ile
rows=5
for i in range(0,rows):
  for j in range(0,i+1):
    print("*" ,end="")
  print()

#Tek döngü ile
rows = 5
for i in range(1, rows + 1):
  print("*" * i)


# *****
# ****
# ***
# **
# *

#Çift döngü ile
row=5
for i in range (rows,0,-1):
  for j in range(0,i):
    print("*",end="")
  print()

#Tek döngü ile
rows=5
for i in range(rows,0,-1):
  print("*"*i)


#      *
#     **
#    ***
#   ****
#  *****

#Çift döngü ile
rows=5
for i in range (0,rows):
  for j in range(0,i+1):
    if j ==0:
      print(" "*(rows-i)+"*",end="")
    else: print("*",end="")
  print()

#Tek döngü ile
rows=5
for i in range(1,rows+1):
  print(" "*(rows-i)+"*"


  #             **
  #            ****
  #           ******
  #          ********
  #         **********
  #        ************
  #       **************
  #      ****************
  #     ******************
  #    ********************

rows=10
for i in range(0,rows+1):
  print(" "*(rows-i)+"*"*2*i)

  #               *
  #              * *
  #             * * *
  #            * * * *
  #           * * * * *
  #          * * * * * *
  #           * * * * *
  #            * * * *
  #             * * *
  #              * *
  #               *

rows = 6
for row in range(1, rows + 1):
  print(' ' * (rows - row), '* ' * row)

for row in range(rows - 1, 0, -1):
  print(' ' * (rows - row), '* ' * row)