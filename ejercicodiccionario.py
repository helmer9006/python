
def count_char(word):
  my_dict = {}
  tamamo = len(word)
  for i in range(tamamo):
    my_dict[word[i]] = word.count(word[i])

  return my_dict
  # YOUR CODE HERE!

print(count_char('presupuesto'))

# deberia ser algo como {p:2, r:1, e:2 ...}



    #diccionario = {}    
    #diccionario['cadena'] = word  
   # for i   
   # print(diccionario['cadena'])
# YOUR CODE HERE!

#print(count_char('presupuesto'))
# deberia ser algo como {p:2, r:1, e:2 ...}clea
