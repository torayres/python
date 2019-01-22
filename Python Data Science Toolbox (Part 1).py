# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 00:02:59 2018

@author: Victor
"""

import math
        
import numpy as np
        
import matplotlib.pyplot as plt


#Writing your own functions

    #User-defined functions
    
        #Built-in functions
        
        bunda = str(5)
        
        bunda
        
        #Defining a function with or without parameters
        
        def squarecoco() :
            valuecoco = 4**2
            print(valuecoco)
        
        squarecoco()
        
        def sqrprint(value):
            sqrprint = value**2
            print(sqrprint)
            
        sqrprint(4) #noice, smort
        
        def sqr(value): 
            new_value = value**2
            return new_value
        
        sqr(4)
        
        #Docstrings --> describes what your function does
            #documents the function
            #placed in the immediate line after the header
            #in between triple " " "
            
        def square(value) :
            """Returns the square of a value."""
            new_value = value ** 2
            return new_value
        
        square(4)
        
        #VARIAVEIS X = PRINT(ARG) --> TYPE = 'NONETYPE' --> NAO RETORNA VALOR
        
    #Multiple Parameters and Return Values        
        
        #Multiple function parameters
        
        def power(value1, value2) :
            """Raise value1 to the power of value2."""
            new_value = value1 ** value2
            return new_value
        
        power(2, 3)
        
        #Tuples
            #Like a list - can contain multiple values
            #Immutable after defined
            #CONSTRUCTED USING PARENTHESIS '()'
            
        tuplerisos = (2, 4, 6)
        
        type(tuplerisos)
        
        a, b, c = tuplerisos #Unpack tuble in several values
        
        a
        b
        c
        
        tuplerisos[1] #allows subsetting
        
        #Returning multiple values with Tuples
        
        def raise_both(value1, value2) :
            """Raises value1 to the power of value2 and vice-versa."""
            new_value1 = value1 ** value2
            new_value2 = value2 ** value1
            tuple = (new_value1, new_value2)
            return tuple
        
        raise_both(2,3)
        
    #Bringing it all together        
        
        #To add 1 the value of a key entry in a dictionary d, use d[entry] += 1.
        #To add a new key to d and set its value to 1, use d[entry] = 1.    
             
#Scope and user-defined functions
        
    #Scopes
            
        #Not all objects are accessible everywhere in a script    
        #Scope --> part of the program where an object or name may be accessible
        
        #Global Scope --> defined in main body of a script or python program
        
        #Local Scope --> define within a function, after the execution, any
        #object or name ceases to be accessible
        
        #Built-in Scope --> names in the pre-defined built-ins modules (print, sum, etc)
        
                    
        #Global vs Local
        
        def square(value) :
            """Returns the square of a value."""
            new_value = value ** 2
            return new_value
        
        square(4)
        
        new_value #NOT DEFINED --> definido apenas dentro da funcao square
        
        #First it searches in the LOCAL SCOPE and ONLY THEM in the GLOBAL
        #If neither of them is returned searches in the BUILT-IN SCOPE
        
        new_value = 10
        
        def square(value) :
            """Returns the square of a value."""
            new_value = value ** 2
            return new_value
        
        square(4) #called in the local scope, returned the argument

        new_value #called in the global scope, returned its value
        
        def square(value) :
            """Returns the square of a value."""
            new_value2 = new_value ** 2 #new_value utilizado dentro da funcao
            return new_value2
        
        square(4) #called in local scope, returns function defined globally

        new_value = 20
        
        square(3274278423)
        
        #Altering the value of a global name within a function call
        
        new_value = 10
        
        def square(value) :
            """Returns the square of a value."""
            global new_value #keyword GLOBAL accesses the global nome
            new_value = new_value ** 2 #square of global 'new_value'
            return new_value
        
        square(2141423) #retorna new_value**2
        
        new_value #faz update de new_value, agora ao quadrado!
        
        #Here you're going to check out Python's built-in scope,
        #which is really just a built-in module called builtins. 
        #However, to query builtins, you'll need to import builtins
        #'because the name builtins is not itself built in...No, I’m serious!'
        
        import builtins
        
    #Nested Functions
        
    #Functions within functions
    #First searches in the inner function
    #Then the outter, ENCLOSING, function
    #Then the global scope
    #Then the built-in scope
       
        #Why nest functions?

        def mod2plus5(x1, x2, x3) :
            """Returns the remainder plus 5 of three values."""
            new_x1 = x1 % 2 + 5
            new_x2 = x2 % 2 + 5
            new_x3 = x3 % 2 + 5
            
            return(new_x1, new_x2, new_x3)
            
        mod2plus5(5, 7, 9) #NOT SCALABLE!
        
        def mod2plus5(x1, x2, x3) :
            """Returns the remainder plus 5 of three values."""
            def inner(x) :
                """Returns the remainder plus 5 of a value."""
                return x % 2 + 5 #'x' arg de inner()
            
            return(inner(x1), inner(x2), inner(x3)) #args de mod2plus5 as inner args!
            
        mod2plus5(5, 7, 9) #Better!
        
        def raise_val(n) :
            """Return the inner function."""
            
            def inner(x) :
                raised = x ** n
                return raised
            
            return inner
        
        raise_val(2)        
        # RETORNA: <function __main__.raise_val.<locals>.inner(x)>
        
        square = raise_val(2) #CRIA FUNCAO QUE ME DA QUADRADO DE SEU ARG
        
        square(15) #RETORNA 15 ** 2
        
        cube = raise_val(3) #IDEM, SO QUE CUBO
        
        cube(15) #RETORNA 15 ** 3
        
        #When we call function SQUARE, it remembers the value n=2
        #although the enclosing scope define by RAISE_VAL and to which n=2
        #is LOCAL and has finished execution
        #Sutileza chamada 'CLOSURE' in Comput Sci Circles
        
        #keyword 'nonlocal' --> create/chagne names in an enclosing scope
        
        def outer() :
            """Prints the value of n."""
            n = 1
            def inner() :
                nonlocal n #faz referencia a 'n', definido na ENCLOSING function
                n = 2 #muda valor de 'n'
                print(n)
                
            inner()
            print(n)
        
        outer() #valor de 'n' foi mudado tanto em outer() quanto em inner()!
        
        #Scopes searched
        
        #Local
        #Enclosing
        #Global
        #Built-in
        
        #The LEGB rule
        
        #Assigning names will only create or change LOCAL NAMES
        #Unless we use keyword global or nonlocal
        
    #Default and flexible arguments

        #Default
        
        def power(value, your_choice = 1) : #settei default = 1
            """Raise value to the power of your_coice."""
            new_value = value ** your_choice
            return new_value
        
        power(4)
        power(4, 2)
    
        #Flexible
        
        #Arbitrary number of arguments
        def add_all(*args) :
            #'*args': turns all args passed into a tuple in the function body
            """Sum all values in *args together."""
            sum_all = 0
            for num in args :
                sum_all += num #atencao a notacao!!!
                
            return sum_all
        
        add_all(4,5,7,4,2,23,2,3,4,3)
        
        #Arbitrary number of key-words arguments
        def print_all(**kwargs) :
            #'**kwargs': turns the identifier-kw pairs into a dictionary within the function body
            """Print-out key-value pairs in **kwargs."""
            
            for key, value in kwargs.items() :
                print(key + ": " + value)
                
        print_all(cu='bunda',je='sus')
        
    #Bringing it all together!


#Lambda functions and error-handling

    #Lambda Functions

        #Quicker way of writing functions
        
        raise_to_power = lambda x, y : x ** y
        
        raise_to_power(2, 3)
        
        #Anonymous functions --> creating functions without a name
        #simple functionalities to be anonymously embedded within larger expressions
        
        #map(function, sequence) -->
        #applies the function to all elements in the sequence (such as a list)
        
        nums = [48, 6, 9, 21, 1]
        
        square_all = map(lambda num : num ** 2, nums) #squares all numbers of the seq
        
        print(square_all)
        # RETORNA: <map object at 0x0000023055163518>
        
        print(list(square_all)) #printa a lista
        
        #filter() --> filter out elements from a list that don't satisfy certain criteria
        
        #reduce() --> performs computations on a list; returns a single value as a result
        
        from functools import reduce
        
    #Introduction to Error Handling
    
        #float()
        
        float(2) #ok
        
        float('2.3') #ok
        
        float('hello') #VALUE ERROR --> um dos muitos tipos de erros
        #ValueError: could not convert string to float: 'hello'
        
        def sqrt(x) :
            """Returns the square-root of x."""
            sqrt = x ** 0.5
            return sqrt
            
        sqrt(4) #ok
        
        sqrt('hello') #TYPE ERROR, e talvez nao tao claro em relacao ao problema
        #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
        
        #Error caught during execution --> EXCEPTIONS
        
        #To catch them: TRY-EXCEPT CLAUSE
        #runs code following 'try', and if it can, all is well
        #if it can't, due to and exception, run the code following 'except'
        
        def sqrt(x) :
            """Returns the square-root of x."""
            try :
                return x ** 0.5
            except :
                print('x must be an int or float')
        
        sqrt(3) #ok, retorna try
        
        sqrt('hello') #retorna exception
        
        #Posso especificar que erros pegar na exception
        
        def sqrt(x) :
            """Returns the square root of x."""
            try :
                return x ** 0.5
            except TypeError : #so quero pegar TypeErrors
                print('x must be an int or float')
                
        sqrt(384)

        sqrt('hello')                
        
        #Raise an error instead of printing
        
        sqrt(-1) #retorna complex number
        
        def sqrt(x) :
            """Returns the square root of x."""
            if x < 0 :
                raise ValueError('x must be non-negative')
            else :
                try :
                    return x ** 0.5
                except TypeError : #so quero pegar TypeErrors
                    print('x must be an int or float')
        
        sqrt(-2) #retorna ValueError definido
                
    #Bringing it all together!
        
#08.12.2018





















