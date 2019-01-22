# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 20:44:37 2018

@author: Victor
"""

import math

import builtins

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from functools import reduce

#Using iterators in PythonLand

    #Iterators vs. Iterables
    
        #Iterables --> an object with an associated .iter() method (lists, dicts, str, files)
        #applying .iter() to an iterable creates a iterator
        #Iterator --> an object that has an associated .next() method that produces the consecutive values
        
        word = 'JeSuS'
        
        it = iter(word) #criei iterable
        
        next(it) #J
        next(it) #e
        next(it) #S
        next(it) #u
        next(it) #S
        next(it) #retorna StopIteration
        
        it2 = iter(word)
        
        print(*it2) #retorna todos resultados de uma vez
        print(*it2) #no more values to go through
        
        dicio = {'victor': 'ayres', 'jesus': 'mamae'}
        
        for key, value in dicio.items() : #unpack key, values com method .items()
            print(key, value)
        
        file = open('file.txt')
        
        it3 = iter(file)
        
        print(next(it3)) #Precisa do print(), se nao fica estranho
        
    #Playing with iterators

        # function enumerate(arg) --> add a counter to any iterable
        # takes any iterable as arg
        # returns a special enumerate object
        # enumerate() returns an enumerate object that produces a sequence
        # of tuples, and each of the tuples is an index-value pair
        
        que = ['jesus', 'bunda', 'risos', 'jherrtrudis']
        
        e = enumerate(que)
        
        e #pairs with the pairs of the original iterable along with their index within the iterable
        
        e_list = list(e)
        
        e_list #gera list of tuples 
        
        #object enumerate is iterable itself 
        
        for index, value in enumerate(que) :
            print(index, value) #default começa no 0
        
        for index, value in enumerate(que, start = 7) : #start muda default
            print(index, value) 
        
        # function zip(arg) --> stitch together an arbitrary number of iterables        
        # returns an iterator of tuples
        
        quei = ['qua', 'quo', 'que']
        jo = ['dro', 'vadis','fazes']
        
        z = zip(quei, jo)
        
        type(z) #object 'zip' --> an iterator of tuples
        
        z_list = list(z)
        
        z_list #results in a list of tuples combining each element from each root list
        
        for quei, jo in zip(quei, jo) : #outra maneira
            print(quei, jo)

        print(*z) #outra maneira
        
        #'*' unpacks an iterable like list/tuple into positional arguments in a function call
        
        quei = ['qua', 'quo', 'que']
        jo = ['dro', 'vadis','fazes']
        
        z1 = zip(quei, jo)
        
        vamos, ver = zip(*z1)
        
        print(vamos)
        print(ver)
        
    #Using iterators to load large files into memory

        #There can be too much data to hold in memory
        #solution --> load data in chunks
        #--> perform the desired operation on each chunk
        #--> store the result
        #--> discard the chunk
        #--> load the next chunk
        
        #with pandas .read_csv(), specify with the argument chunksize = num
            
        #

        
    
#List comprehension and generators
        
    #List Comprehension
    
        #More efficient than for loops
        
        nums = [12, 8, 21, 3, 16]
        
        new_nums = []
        
        for num in nums :
            new_nums.append(num + 1)
        print(new_nums)
            
        nums = [12, 8, 21, 3, 16]
        
        new_nums = [num + 1 for num in nums] #list comprehension!
        
        new_nums
        
        #outro exemplo
        
        result = [num for num in range(11)]
        
        result
        
        #List comprehension --> Collapses 'for' loops for building lists into a single line
        #Components -->
        #(1) An iterable
        #(2) An iterator variable that represents the members of the iterable
        #(3) An output expression
        
        #Reads
        # [ 'output expression' for 'iterator variable' in 'iterable']
        
        #Nested loops
        
        pairs_1 = []
        
        for num1 in range(0,2):
            for num2 in range (6,8):
                pairs_1.append(num1, num2)
        pairs_1
        
        #Usando list comprehension
        
        pairs_2 = [(num1, num2) for num1 in range(0,2) for num2 in range (6,8)]
        
        pairs_2 #same thing
        
        #Reads
        # [ [output expression] for 'iterator variable' in 'iterable']
        
    #Advanced comprehensions
        
        #Conditional on the iterable
        
        [ (num ** 2) for num in range(10) if num % 2 == 0 ]
        
        #Reads
        # [ 'output expression' for 'iterator variable' in 'iterable' if 'predicate expression' ]
        
        #Conditional on the output expression
        
        [ (num ** 2 if num % 2 == 0 else 0) for num in range(10) ]
        
        #Dictionary comprehension --> to create dictionaries
        #ATENCAO AS DIFERENCAS
        #{} e nao []
        #separa key, value com ':'        
        
        pos_neg = {num: -num for num in range(9)}
        
        pos_neg
        
    #Introduction to generators expressions

        #Generators --> like a Comprehension, but DOESNT STORE THE RESULT IN MEMORY
        #Uses () instead of []
        #'lazy evaluation' --> the evaluation of the expression is delayed until its value is needed
        #Faz tudo que um comprehension faz
        #Gera object <generator>
        
        (num for num in range(10*100000000)) #se faco com list, pc explode risos
        
        #Generator functions --> when called, produces generator objects
        #instead of using 'return', we need to use 'yield'
        
        def num_seq(n) :
            """Generate values from 0 to n."""
            i = 0
            while i < n :
                yield i
                i += 1
        num_seq(20) #gerou generator object
        print(num_seq(20)) #idem
        
        for item in num_seq(20) : #calling the generator function
            print(item)
        
    #Wrapping up comprehensions and generators

        #Basic
        # [ <output expression> for <iterator variable> in <iterable>]
        
        #Advanced
        # [ <output expression + conditional on output> for <iterator variable>
        # in <iterable + conditional on iterable> ]
    
#Bring it all together!
        
    #Welcome to the case study
        
        #Tentando reproduzir a previa do exercicio marromenos
        dados = pd.read_csv('worldbank.csv')

        dados
        
        feature_names = list(dados) #lista com column headers
        feature_names = list(dados.columns.values) #outra maneira
        feature_names
        
        row_vals = list(dados.iloc[0, :]) #valores da primeira linha de dados
        row_vals
        
        zipped_list = zip(feature_names, row_vals) #zippamos listas
        
        rs_dict = dict(zipped_list) #transformamos listas em dicionarios
        
        rs_dict 
        
        #acho que deu
        
        %reset -f #reseta variables, o '-f' faz proceder sem perguntar se quer
        
        #Vamos automatizar esse processo de extracao
        
        import math
        import builtins
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        from functools import reduce
        
        dados = pd.read_csv('worldbank.csv')
        feature_names = list(dados)
        row_vals = list(dados.iloc[0, :])
        
        def lists2dict(list1, list2) :
            """Return a dictionary where list1 provides the keys
            and list2 provides the values"""
            zipped_lists = zip(list1, list2)
            rs_dict = dict(zipped_lists)
            return rs_dict
        
        rs_fxn = lists2dict(feature_names, row_vals)
        
        rs_fxn
        
        row_lists # um dia sai... rip reproducao
        
        dados.head()
          
    #Using python generators for streaming data
    
        #Using a generator to load a file line by line
        #Works on STREAMING DATA -->
        #if new lines are being written to the file you're reading
        #it will keep on reading and processing until there are no lines left for it read
        
        #<with open('datacamp.csv') as datacamp>
        #binds the csv file 'datacamp.csv' as <datacamp> in the context manager.
        #Here, the <with> statement is the context manager, and its purpose is to
        #ensure that resources are efficiently allocated when opening a connection to a file.
        
    #Using pandas' read_csv iterator for streaming data
    
#09.12.2018        