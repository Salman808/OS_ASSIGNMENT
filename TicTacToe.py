#usr/bin/python3

board = [' ' ,  ' ' , ' ' , ' ' ,  ' ' , ' ' , ' ' , ' ' , ' ' ]
win =0
f = bool(1)
turn= 0;
while(f):
  print ' ___ ___ ___'
  print '|', board[0] ,'|', board[1] ,'|', board[2] ,'|'
  print ' ___ ___ ___'
  print '|', board[3] ,'|', board[4] ,'|', board[5] ,'|'
  print ' ___ ___ ___'
  print '|', board[6] ,'|', board[7] ,'|', board[8] ,'|'
  print ' ___ ___ ___'
  x=10
  if turn%2==0:
      x=input(" 1st Player Turn\n Enter Location<1-9> ")
      if 0>x and x>9 :
          print " You Enterend invalid locatin "
          exit()
      x=x-1
      while board[x]=='T' or board[x]=='X':
        x=input("\nLocation is alreay filled. Choose another location :")
        x=x-1
      board[x]='T'
  else:
      x=input(" 2st Player Turn\n Enter Location<1-9> ")
      if 0>x and x>9 :
          print " You Enterend invalid locatin "
          exit()
      x=x-1
      while board[x]=='T' or board[x]=='X':
        x=input("\nLocation is alreay filled. Choose another location :")
        x=x-1
      board[x]='X'
  turn=turn+1
  if board[0]=='T' and board[1]=='T' and board[2]=='T':
    win=1
    f=0
  elif board[0]=='T' and board[3]=='T' and board[6]=='T':
    win=1
    f=0
  elif board[6]=='T' and board[7]=='T' and board[8]=='T':
    win=1
    f=0
  elif board[8]=='T' and board[5]=='T' and board[2]=='T':
    win=1
    f=0
  elif board[3]=='T' and board[4]=='T' and board[5]=='T':
    win=1
    f=0
  elif board[0]=='T' and board[4]=='T' and board[8]=='T':
    win=1
    f=0
  elif board[2]=='T' and board[6]=='T' and board[4]=='T':
    win=1
    f=0
  elif board[0]=='X' and board[1]=='X' and board[2]=='X':
    win=2
    f=0
  elif board[0]=='X' and board[3]=='X' and board[6]=='X':
    win=2
    f=0
  elif board[6]=='X' and board[7]=='X' and board[8]=='X':
    win=2
    f=0
  elif board[8]=='X' and board[5]=='X' and board[2]=='X':
    win=2
    f=0
  elif board[3]=='X' and board[4]=='X' and board[5]=='X':
    win=2
    f=0
  elif board[0]=='X' and board[4]=='X' and board[8]=='X':
    win=2
    f=0
  elif board[2]=='X' and board[6]=='X' and board[4]=='X':
    win=2
    f=0
if win==1 :
  print "\n Player 1 is Winner . "
elif win==2 :
  print "\n Player 2 is Winner . "
else:
  print "\n Error ! Game is Stopped. Run Again. "
