field=[[None,None,None],[None,None,None],[None,None,None]]
#Ввод данных
player='X'
step=0
while step<=8  :
 print(*field,sep='\n')
 if player=='X':
  strk=int(input('Игрок '+ player +' введите номер строки (1-3)\n'))
  if 3>=strk>=1:
   print('Выбрана строка '+ str(strk))
  else:
   print('Число за пределами игрового поля')
  stlb=int(input('Введите номер столбика(1-3)\n'))
  if 3>=stlb>=1:
    print('Выбрана строка '+ str(strk)+ '\n''Выбран столбик ' +str(stlb))
    field[strk-1][stlb-1]='X'
    print('Переход хода')
    player="O"
    print(*field,sep='\n')
    step=step+1
    print(step)
  else:
    print('Число за пределами игрового поля')
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
    print('Переход хода')
    player="X"
    print(*field,sep='\n')
    step=step+1
    print(step)
  else:
    print('Число за пределами игрового поля')    
else :
  print('Game over')    
