# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:31:41 2018

@author: Victor
"""

#Python foi criado por Guido Van Rossum

    help()
    quit

#Seleciona o que quer e Ctrl+Enter para rodar

    4+5
    # ' ; ' separa comandos numa mesma linha
    # 4+5
    # 5+4
    # 4+5 ; 5+4

#Intro
    
    #print() é usado para visualizar o argumento
    
        print('Hello, World!') 

        weight = 99
        height = 1.72

        bmi = weight/(height**2)

        print(bmi)

    #types() retorna qual o tipo da variável

        type(bmi) #float = real numbers
        x = 5
        type(x) #int = integers
        y = 'risos'
        type(y) #str = string
        z = True
        type(z) #bool = boolean = true or false

    #How the code behaves depends on the TYPE you're working with
    
        bool() #muda argumento para boolean
        str() #muda argumento para string
        float() #muda argumenoto para float
        int() #muda argumento para string
    
    #Mixing types together
    
        "I can add integers, like " + str(5) + " to strings." #ok!
    
        "I said " + ("Hey " * 2) + "Hey!" #ok!
    
        True + False #ok!
    
        "The correct answer to this exercise is answer number " + 2 # nope
    
#Pyhton Lists
    
    #Outro tipo de variavel
    #Listas podem conter listas
    #Podem conter variaveis de diferentes tipos ao mesmo tempo
    
        eu = [weight, height]
    
        print(eu)
    
        eu = [["weight", weight],
          ["height", height]]
    
        print(eu)
    
    #Subsetting Lists
    
    # [['weight', 99], ['height', 1.72]]
    #       0                1
    #       -2              -1
    
        eu[0]
        eu[1]
        eu[-1]
        eu[-2]
    
    #Slicing Lists
    
    #[      start    :   end     ]
    #     inclusive   exclusive 
    
    #[               : end      ]
    #    all up to    inclusive
    
    #[      start    :         ]
    #     inclusive   all up to
    
        lista = ['oi', 'tchau', 'que', 'show', 'tranq', 'risos']
        
        lista[2:5]
        lista[:5]
        lista[1:]
    
        print(lista[0]+lista[-1])
        
        eu
        eu[1]
        eu[1][1] #Subsetting o subset
        
    #Manipulating Lists
    
    #Changing Elements
        
        lista
        lista[1] = 'xau'
        lista
        lista[0:1] = ["hi", "bye"]
        lista
    
    #Adding & Removing Elements
    
        lista
        lista = lista + ["esteban"]
        lista
        
        del(lista[0]) #remove hi
        lista
        
        del(lista[0]) #remove bye
        lista
    
    #Behind the Scenes
    
    #Se quero copiar uma lista para uma nova variavel
    #Nao basta usar o operador '='
    #Pois listas armazenam na memoria o conteudo
    #Entao se faco eu = eu2
    #'eu2' vai armazenar os mesmos dados que 'eu'
    #Caso altere um elemento de 'eu2', este tambem sera alterado em 'eu'
    
        eu2 = eu #Se mexer em um, mexo no outro automaticamente
    
        eu2 = list(eu) #Agora 'eu2' fica independente de 'eu'
        eu2 = eu[:] #Outra maneira
    
#Functions
    
    #Piece os reusable code
    #Solves particular task
    #Call function instead of writing the code
    
        max(eu) #Retorna o valor máximo do argumento
    
        round(1.68, 1) #Numero que quero arredondar, numero de casas decimais
        round(1.68) #Settado em 0
        help(round)
    
        len(eu) #Length da lista
        len(lista) #Length da lista
    
        complex(3) #Create a complex number from a real part and an optional imaginary part.
              #This is equivalent to (real + imag*1j) where imag defaults to 0.
        complex(3,1)

        sorted(eu) #Return a new list containing all items from the iterable in ascending order.
               #A custom key function can be supplied to customise the sort order, and the
               #reverse flag can be set to request the result in descending order
               sorted(eu, reverse=1)           
    
    #Methods
    
    #Functions that belongs to objects
    #Python objects: variables with its different associated types
    #For each object type, there belongs some functions
    #str -> capitalize(), replace()
    #float -> bit_length(), conjugate()
    #list -> index(), count()
    
        lista.index("risos")
        lista.count("que")
    
        nome = 'viktor'
        nome = nome.capitalize()
        nome = nome.replace('k', 'c')
        nome
        nome.index('c') #index() comum a lists e strings
        nome.upper() #upper() coloca tudo em maiusculo, nao altera o Object
    
    #Alguns Methods alteram o Object
    #Most lists methods will change the list they're called on
    
        lista.append("talquei")
        lista
        lista.remove("talquei")
        lista
        lista.reverse()
        lista

    #Packages
    
    #Directory of Python Scripts
    #Each script = module
    #Specify functions, methods, types
    
    #NumPy -> working with arrays
    #Matplotlib -> data visualization
    #Scikit-learn -> machine learning
    
    #USAR NO TERMINAL: pip install numpy [Numeric Python]
    #USAR NA SHELL: import numpy
    #MUDAR SINTAXE: import numpy as np
    #FUNCAO ESPECIFICA: from numpy import array
    
        import numpy as np
    
        jesus = np.array([1, 2, 3])
     
        jesus
    
        import math    

        x = 3 * math.pi
    
        x
    
#NumPy
    
    #NumPy arrays() contain ONLY ONE TYPE
    #New kind of TYPE
    #Methods proprios, operacoes funcionam de maneira diferente
    #Forces TYPE COERSION
    
        matriz = np.array([11.11, 12.12, 13.13, 14.14, 15.15])
    
        matriz[1]

        matriz > 13 #Cria boolean
    
        matriz[matriz > 13] #Subsetto dada o boolean gerado
    
        maior_13 = matriz > 13
    
        maior_13
    
        matriz[maior_13] #Outra forma
    
    #2D NumPy Arrays
    
        type(matriz) #numpu.ndarray [ndarray = N-dimensional array]
    
        matriz2d = np.array([[11, 12, 13, 14, 15],
                        [21, 22, 23, 24, 25]])
        matriz2d
    
        matriz2d.shape # .shape -> atributo que mostra (rows, columns)
    
        matriz2d[0] #first row
    
        matriz2d[0][0] #a11
        matriz2d[0,0]
    
        matriz2d[:,0] #first column
    
        matriz2d[:,1:4] #submatriz a12:b24
    
        multiplicador = np.array([0.5, 2])
    
        matriz2d * multiplicador #AlgeLin
                            #(2x5) * (2x1) --> nope!
                            
        multiplicador = np.array([[0.5], [2]]) #AlgeLin
                                        #(2x5) * (1x2) --> ok!
    
        matriz2d * multiplicador
    
    #NumPy Basic Statistics
    
        np.mean(x)
    
        np.std(x)
    
        np.median(x)
    
        np.corrcoef(x) #NaN
    
        np.sum(x)
    
    #Sampling
    
        help(np.random.normal)
        #loc = mean
        #scale = std
        #size = shape
        #returns ndarray or scalar
    
        height = np.round(np.random.normal(1.7, 0.25, 5000), 2)
    
        weight = np.round(np.random.normal(70, 15, 5000), 2)
    
        np.mean(height)
        np.mean(weight)
        np.std(height)
        np.std(weight)
        np.corrcoef(height, weight)    
    
        hw = np.column_stack((height, weight))
        np.corrcoef(hw[:,0], hw[:,1])
    
#24.11.18
    
    
    
    
    
    
    
    
