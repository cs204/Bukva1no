s = input('Сколько футов:')
x1 = s.replace('ft', '')

x2= float(x1)/float(3.28073993)

print('Это будет',round(x2, 2),'метров.')