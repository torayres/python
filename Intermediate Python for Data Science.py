# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 23:05:45 2018

@author: Victor
"""

import math
        
import numpy as np
        
import matplotlib.pyplot as plt

#Matplotlib

    #Basic plots with matplotlib
    
        X = [1950, 1970, 1990, 2010]
        
        Y = [2519, 3692, 5263, 6972]
        
        plt.plot(X, Y)
                
        plt.scatter(X, Y)
                
        plt.xscale('log') #muda a escala do eixo x pra log
        
        plt.show() #display graphic (nao ta funfando aqui)
        
     #Histogram
     
     #Explore dataset, get ideia about distribution
     
         help(plt.hist)
     
         #'x' is a list of values you want to build a diagram for
         #'bins' how many bins the data should be divided in
         #Then hist() will find the appropriate boundaries for all bins
         #And calculate how many values are in each one
         #'bins' default is 10
     
         values = [0.1, 0.5, 1.2, 1.5, 1.3, 2.2, 3.2, 2.1, 2.2, 0.8, 2.7, 2.3, 1.8, 3, 3.5, 0.7, 1.6]
         plt.hist(values, bins=3)
         
         plt.clf() #cleans it up so you can start afresh
         
     #Customization
     
         x = [1950, 1970, 1990, 2010]
        
         y = [2.519, 3.692, 5.263, 6.972]
         
         plt.plot(x, y)
         
         plt.xlabel('Year')
         plt.ylabel('Population')
         plt.title('World Population Growth')
         plt.yticks([0, 2, 4, 6, 8], #Customiza eixo Y, qtd/sep dos ticks
                    ['0B', '2B', '4B', '6B', '8B']) #Nomear ticks 
         
     #Add more data
         
         x = [1800, 1850, 1900] + x
         
         y = [1, 1.262, 1.65] + y
         
         plt.plot(x, y)
         
         plt.xlabel('Year')
         plt.ylabel('Population')
         plt.title('World Population Growth')
         plt.yticks([0, 2, 4, 6, 8],
                    ['0B', '2B', '4B', '6B', '8B']) 
                 
         
         help(plt.scatter)
         
         plt.scatter(x, y, s=50, c='red', alpha = 0.3)
         #'s' = size, scalar or array
         #'c' = color: color, sequence (or of color), str/list/2-Darray
         #'alpha' = blending value, 0 (transparent) and 1 (opaque)
         
         plt.xlabel('Year')
         plt.ylabel('Population')
         plt.title('World Population Growth')
         plt.yticks([0, 2, 4, 6, 8],
                    ['0B', '2B', '4B', '6B', '8B']) 
     
         plt.grid(True) #faz grids no grafico
         
         plt.text(1875, 1.8, 'Sus') #adiciona texto ao grafico
         plt.text(1999, 7.5, 'ej')  #coordenadas + texto
         
         
#Dictionaries & pandas       

         pop = [30.55, 2.77, 39.21]
        
         countries = ['afghanistan', 'albania', 'algeria']
        
         countries.index('albania')
        
         ind_alb = countries.index('albania')
        
         pop[ind_alb] #not convenient nor intuitive
        
        #'{ }' geram dicionario
        # '{key1:value1, key2:value2, ...}
        
         world = {'afghanistan':30.55, 'albania':2.77, 'algeria':39.21}
        
        #dict_name[key]
        
         world['albania']
        
         world.keys() #mostra as dict_keys
        
        #Nao pode ter duas keys com nomes iguais
        #So aceita immutable objects (floats, booleans, strings, integers)
        #Lists, por exemplo, nao sao aceitas
        
         list_nope = {'je':'sus', ['ri', 'sos']:10}
        
     #Mexendo
        
         world['sealand'] = 0.000027
        
         'sealand' in world #checa se 'sealand' foi adicionada
        
         world['sealand'] = 0.000028 #cada chave e unica, altera a existente
        
         del(world['sealand']) #deleta
        
         #dicionarios dentro de dicionarios
        
         brasil = {'RJ': {'capital':'rio', 'pop':4},
                    'MG': {'capital':'bh', 'pop':3},
                    'SP': {'capital':'sp', 'pop':5}}
                
         brasil['RJ']['capital']
        
         brasil['SP']['pop']
        
     #Pandas [by Wes McKinney]
        
         import pandas as pd
        
         brasiltoframe = { 
                'estado': ['Espírito Santo','Rio de Janeiro', 'Minas Gerais', 'São Paulo'],
                'capital' : ['Vitória','Rio de Janeiro', 'Belo Horizonte', 'São Paulo'],
                'pop' : [2, 4, 3, 5] }
        
         brasiltoframe
        
         sudeste = pd.DataFrame(brasiltoframe)
        
         sudeste
        
         sudeste.index = ['ES', 'RJ', 'MG', 'SP'] #'.index' method pra settar column label
        
         sudeste
        
     #puxando de csv (comma separated value)
        
         meuframe = pd.read_csv('path/to/meucsv.csv') #vem com column label como variable
        
         meuframe = pd.read_csv('path/to/meucsv.csv', index_col = 0) #resolve
        
     #selecting data
        
         sudeste['capital'] #retorna 'Name: capital, dtype: object'
        
         type(sudeste['capital']) #pandas.core.series.Series
        
         #'Series' sao tipo 1D labelled array
         #Coloque varias Series stackadas e geramos um frame
        
         sudeste[['capital']] #'[[]]' -> sub Data Frame
        
         sudeste[['capital', 'pop']]
        
         sudeste[1:3] #slicing, vem em Frame
        
         #method .loc --> label-based
         #method .iloc --> integer poistion-based
        
         sudeste.loc['RJ'] #tem que settar a label, mas mesmo problema de Series
        
         sudeste.loc[['RJ']] #resolve
        
         sudeste.loc[['ES', 'MG']]
        
         sudeste.loc[['SP', 'RJ'], ['capital', 'pop']] #seleciona columns tambem
        
         sudeste.loc[:, ['estado', 'pop']] #pega todas as rows para determinadas columns
        
         sudeste.iloc[[1]]
        
         sudeste.iloc[[0,2]]
         
         sudeste.iloc[[3,1], [1,2]]
        
         sudeste.iloc[:, [0,2]]        
        
        
#Logic, Control Flow and Filtering        
        
     #Comparison Operators --> how Python values relate
     
         2 < 3 #True
         
         2 == 3 #False
         
         2 != 3 #True
         
         2 > 3 #False
         
         2 <= 3 #True
        
         2 >= 3 #False
         
         'carl' < 'chris' #True --> 'carl' vem antes de 'chris' em termos de alfabeto
         
         'carl' < 3 #Nope
         
      #Boolean Operators

          #'and' 'or' 'not'
          
          True and True #True
          
          True and False #False
          
          False and True #False
          
          False and False #True
          
          x = 12
          
          x > 5 and x < 15 #True
          
          True or True #True
          
          True or False #True
          
          False or True #True
          
          False or False #False
          
          x > 5 or x < 10 #True
          
          not True #False
          
          not False #True
          
          #Numpy
          #np.logical_and()
          #np.logical_or()
          #np.logical_not()
          
      #'if' 'elif' 'else'
          
          x = 438573985439
          
          if x % 2 == 0 : #'if' condition ':'
              print('x is divisible by 2') #expression --> NOTE O INDENT!
              print('bunda')
          elif x % 3 == 0 : #'elif' condition ':'
              print('x is divisible by 3')
              print('jesus')
          else :            #'else' ':' --> nao precisa de condition
              print('x is neither divisible by 2 nor by 3') #expression --> NOTE O INDENT!
              print('risos')
        
      #Filtering pandas DataFrame

           sudeste
           
           sudeste.iloc[:,2]
           sudeste.loc[:,'pop']
           sudeste['pop']
           
           sudeste['pop'] > 3
           
           muitagente = sudeste['pop'] > 3
           
           sudeste[muitagente] #ou direto:
           sudeste[sudeste['pop'] > 3]
           
           #poderia usar um np.logical... dentro dos '[]' tambem
           
#Loops
    
      #'while' loop
      
           #repeats action until condition is met
           
           #'while' condition :
               #'expression'
               
           offset = 50
           
           while offset != 0 :
               if offset > 0 :
                   offset = offset - 1
               else :
                   offset = offset + 1
               print(offset)
    
      #'for' loop    
           
           #for each var in seq, execute expression
           
           #'for' var 'in' seq :
               #'expression'          
                    
           familia = [24, 57, 57, 85]
           
           for idade in familia : #'idade' eh nome ARBITRARIO
               print(idade)
           
           for idade in enumerate(familia) :
               print(idade)
           
           for index, idade in enumerate(familia) : #'index' tambem ARBITRARIO
               print('index ' + str(index) + ': ' + str(idade))
               
           for risos in 'jesus' : #'risos' tambem ARBITRARIO
               print(risos.capitalize())
        
      #Looping Data Structres
      
           #Dictionaries
          
           dicio = { 'wololo':10,
                   'walala':15,
                   'welele':20,
                   'wilili':25,
                   'wululu':30}
          
           for bunda, risos in dicio :
               print(bunda + ': ' +str(risos))
           #ERROR! 'ValueError: too many values to unpack (expected 2)'
          
           for bunda, risos in dicio.items() : #method .items() conserta
               print(bunda + ': ' +str(risos)) #DICIONARIOS SAO UNORDERED!!!
          
           #NumPy Arrays
      
           nparray1 = np.array([1, 2, 3, 4,])
           nparray2 = np.array(['a', 'b', 'c', 'd'])
           
           nparray = np.array([nparray1, nparray2]) 
        
           for bunda in np.nditer(nparray) : #function .nditer(arg) conserta
               print(bunda)
               
           #pandas DataFrame
           
           sudeste
           
           for bunda in sudeste :
               print(bunda)
           #retorna as column labels
           
           for bunda, risos in sudeste.iterrows() : #method iterrows() melhora
               print(bunda) #para cada row label
               print(risos) #gera dataSeries com informacoes da row referente
               
           for bunda, risos in sudeste.iterrows() : #method iterrows() melhora
               print(bunda, risos) #fica meio embolado, melhor jeito acima
               
           for bunda, risos in sudeste.iterrows() :
               print(bunda + ': ' + str(risos['pop'])) #posso subsettar de boa
               
           for bunda, risos in sudeste.iterrows() :
               print(bunda)
               print(risos['pop']) #meio zoado, melhor jeito acima
               
           #Criando nova coluna com 'for'
           
           for bunda, risos in sudeste.iterrows() :
               sudeste.loc[bunda, 'capital length'] = len(risos['capital'])
           
           sudeste
               
           del(sudeste['capital length'])
           
           sudeste
           
           #Melhor usar 'apply'
           
           sudeste['capital length'] = sudeste['capital'].apply(len)
           
           sudeste
           
           #function .apply(arg), tao intuitivo quanto parece
           
#Case Study: Hacker Statistics
           
      #To the game --> estamos no empire states building, ground zero
      #aposta com dado: se der 1 ou 2, desce 1 degrau (limitado a 0)
      #se der 3, 4 ou 5, sobe 1 degrau
      #se der 6, joga o dado de novo, e sobe a quantidade que sair nele
      #quem chegar no degrau 60 primeiro ganha
      #temos 0.1% de chance de cair e voltar pro inicio
      
      #Random Step --> basear proximo movimento em 1 processo estocastico
           
           np.random.rand() #pseudo-random number between 0 and 1
        
           np.random.seed(123) #settar seed
           
           np.random.rand()
           
           coin = np.random.randint(0,2) #random integer between, 0 or 1
           print(coin)
           
           if coin == 0 :
               print('heads')
           else :
               print('tails')
           
           step = 50
           
           dice = np.random.randint(1,7)
           
           if dice <= 2 :
               step = step - 1
           elif dice <= 5 :
               step = step + 1
           else :
               step = step + np.random.randint(1,7)
               
           print(step)
           print(dice)

      #Random Walk --> movimentos baseados numa serie de processos estocasticos
          
          np.random.seed(123)
      
          outcomes = [] #lista vazia
          
          for queijo in range(10) : #function  .range(arg) define numero de iteracoes
              coin = np.random.randint(0,2)
              if coin == 0:
                  outcomes.append('heads') #function .append(arg)
              else :
                  outcomes.append('tails')
          
          print(outcomes) #not a random walk
          #bunch of random steps
          #toss coins doesnt depend on the last one
          
          #transformando em Random Walk
          
          tails = [0] #lista que conta numero de tails
          
          for queijo in range(10) :
              coin = np.random.randint(0,2)
              tails.append(tails[queijo] + coin) #precisa do [queijo]
                                                  #concatenar lista com int
          print(tails)
              
          game_as_rw =[0]
          
          for jesus in range(100) :
              step = game_as_rw[-1] #ultimo elemento da lista game_as_rw
              dice = np.random.randint(1,7)
              if dice <= 2 :
                  step = step - 1
              elif dice <=5 :
                  step = step + 1
              else :
                  step = step + np.random.randint(1,7)
              game_as_rw.append(step)
          
          print(game_as_rw) #ainda ha erro pq tem valores negativos
          
          #function .max(arg) --> retorna maior entre dois argumentos
          #se quero limitar queda de 'x' ate 10 --> max(10, x-1)
          
          game_as_rw =[0]
          
          for jesus in range(100) :
              step = game_as_rw[-1] 
              dice = np.random.randint(1,7)
              if dice <= 2 :
                  step = max(0, step - 1) #maximo entre 0 e step - 1
              elif dice <=5 :
                  step = step + 1
              else :
                  step = step + np.random.randint(1,7)
              game_as_rw.append(step)
          
          print(game_as_rw)
          
          plt.plot(game_as_rw)
           
      #Distribution

          #1.000.000 rounds of tossing coins 10 times
          
          np.random.seed(123)
          
          list100tails = []
          
          for jesus in range(1000000) :
              tails = [0]
              for jesus in range(10) :
                  coin = np.random.randint(0,2)
                  tails.append(tails[jesus] + coin)
              list100tails.append(tails[-1])
                            
          plt.hist(list100tails, bins = 10)
          
          all_walks = []

          for i in range(10) :

              random_walk = [0]
              for x in range(100) :
                  step = random_walk[-1]
                  dice = np.random.randint(1,7)

                  if dice <= 2:
                      step = max(0, step - 1)
                  elif dice <= 5:
                      step = step + 1
                  else:
                      step = step + np.random.randint(1,7)
                  random_walk.append(step)

              all_walks.append(random_walk)

            print(all_walks)
          
            plt.plot(all_walks) #wtf
            
            np_aw = np.array(all_walks) #lista de listas para matriz
            
            plt.plot(np_aw) #wtf2
            
            np_aw
            
            np_aw_t = np.transpose(np_aw) #np.transpose(arg) --> matriz transposta
                        
            np_aw_t #Every row represents the position after 1 throw for the 10 RW
            
            plt.plot(np_aw_t) #agora sim
            
            #incluindo o 0.1% chance de cair
            
            all_walks = []
            for i in range(500) :
                random_walk = [0]
                for x in range(100) :
                    step = random_walk[-1]
                    dice = np.random.randint(1,7)
                    if dice <= 2:
                        step = max(0, step - 1)
                    elif dice <= 5:
                        step = step + 1
                    else:
                        step = step + np.random.randint(1,7)
                    if np.random.rand() <= 0.001 : #alteracao feita aqui
                        step = 0
                    else :
                        step = step
            
                    random_walk.append(step)
                all_walks.append(random_walk)

            np_aw_t = np.transpose(np.array(all_walks))
            plt.plot(np_aw_t)
            
            #qual a chance de chegar no andar 60?
          
            ends = np.array(np_aw_t[-1])
            plt.hist(ends)
            
            np.count_nonzero(ends >= 60) / 500 * 100 #76.6%, pretty good
            
#07.12.2018
          



        