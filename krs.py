field=[[None,None,None],[None,None,None],[None,None,None]]
#Ввод данных
player="X"
Game=True
while Game :
 print(*field,sep='\n')
 if player=='X':
  strk=int(input('Игрок '+ player +' введите номер строки (1-3)\n'))
  if 3>=strk>=1 :
   print('Выбрана строка '+ str(strk))
  else:
   print('Число за пределами игрового поля')
  stlb=int(input('Введите номер столбика(1-3)\n'))
  if 3>=stlb>=1:
    print('Выбрана строка '+ str(strk)+ '\n''Выбран столбик ' +str(stlb))
    field[strk-1][stlb-1]='X'
    print('Переход хода\n')
    player="O"
    print(*field,sep='\n')
  else:
    print('Число за пределами игрового поля')

 if field[0][0]==player and field[1][0]==player and field[2][0]==player:
   print('Игрок '+player+" Победил!")   
   Game=False 
   break
 if player=='O':
  strk=int(input('Игрок '+ player +' введите номер строки (1-3)\n'))
  if 3>=strk>=1:
   print('Выбрана строка '+ str(strk))
  else:
   print('Число за пределами игрового поля')

  stlb=int(input('Введите номер столбика(1-3)\n'))
  if 3>=stlb>=1:
    print('Выбрана строка '+ str(strk)+ '\n''Выбран столбик ' +str(stlb))
    field[strk-1][stlb-1]='O'
    print('Переход хода\n')
    player="X"
    print(*field,sep='\n')
  else:
    print('Число за пределами игрового поля') 
       
 if field[0][0]==player and field[1][0]==player and field[2][0]==player:
  print('Игрок '+player+" Победил!")  
  Game=False 
  break