from IPython.display import display, Math
display('4 + 3 = 7')
display('4 + 3 = '+ str(4+3))
display(Math('4 + 3 = 7'))

x=4
y = 3
display(Math(str(x)+ ' + '+ str(y) + ' = ' + str(x+y)))

display(Math('%g+%g=%g' %(x,y,x+y)))

