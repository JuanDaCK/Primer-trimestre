"""Acceder a los elementos de un diccionario"""
dictionary={"a":1,
           "e":2
           }
print(dictionary)
print(f"clave a:{dictionary['a']}")
print(f"clave a:{dictionary['e']}")
dictionary={"numbers":[18,20,28],
            "groups":{"a":1,"b":2}
            }
print(dictionary)
print(f"clave numbers:{dictionary['numbers']}")
print(f"clave groups:{dictionary['groups']}")
print(f"clave numbers:{dictionary['numbers'][1]}")
print(f"clave groups:{dictionary['groups']['b']}")
print(dictionary,{'z'})