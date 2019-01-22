# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:27:25 2018

@author: Victor
"""

import math

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

from functools import reduce

import builtins

#Welcome to the course

    #Text file
    
        filename = 'file.txt'
        
        file = open(filename, mode = 'r') # 'r' is to read, 'w' seria pra escrever nele
        
        text = file.read() #.read() method
        
        file.close() #.close() method --> closes the connection to the file
        
        print(text)
        
        #Alternative
        
        with open('file.txt', 'r') as file : # 'with' is a context manager
            print(file.read()) # nao precisa se preocupar em fechar a conexao
        
        !ls # display contentes of your current directory
        
        print(file.closed) #checa se 'file' esta fechado
        
        #Puxar linha por linha
        
        with open('file.txt', 'r') as file : # 'with' is a context manager
            print(file.readline()) #puxa apenas primeira linha
            print(file.readline()) #agora primeira e segunda, etc
                        
    #The importance of flat files in data science
    
        #FLAT FILES --> basic text files containing records
        #--> table data without structered relationships
        #--> consists of records: row of fields or attributes
        #--> each of which contains at most one item of info
        #--> .txt, .csv, characters separators, called delimiter
        #may have a header, impacts in the importing
        #in contrast of 'relational database', where columns of distinct tables can be related
        
        import this #imports the Zen of Python
        
    #Importing flat files using NumPy
    
        #Import as nparray if all the data is numerical
        
        #function --> .loadtxt(), nao e muito bom pra mixed date types
        #function --> .genfromtxt(), melhora problema acima
        
        filename =  'nums.txt'
        
        data = np.loadtxt(filename, delimiter = ',', dtype = str)
        #precisa settar o delimiter, default é " "; '\t' seria para 'tab delimiter'
        #dtype para puxar tudo como string
        
        data
        
        data = np.loadtxt(filename, delimiter = ',', skiprows = 1)
        #caso tenha header, pula linha
        
        data = np.loadtxt(filename, delimiter = ',', usecols=[0,1])
        #escolher quais colunas quero dos meus dados
        
        data = np.genfromtxt(filename, delimiter = ',', dtype = None)
        #'names = TRUE' se tivesse header
        #'dtype = None' a funcao tenta descobrir qual o tipo sozinha
        
        data
        
        #function --> .recfromcsv()
        #funciona como a gen, mas default dtype = None, names = TRUE, delimiter = ','
        #para .csv, obviamente
        
    #Importing flat files using pandas
    
        #Outras funcoes nao resolvem este problema de data scientists -->
        #--> to have two-dimensional labeled data structures with columns of potentially different types
        #onde role fazer a porra toda
        
        filename = 'exemplo.csv'
        
        data = pd.read_csv(filename) #como ja fizemos muitas vezes
        
        data.head() #mostra primeiros 5 linhas, incluindo header
        
        data_array = data.values #attribute to convert from df to nparray
               
        #'sep = ' --> equivalente de 'delimiter = '
        #'comment = ' takes characters that comments occur after in the file
        #'na_values = ' takes a list of strings to recognize as NA/NaN

#Importing data from other files

    #Introduction to other file types
    
        #Pickled file --> native to python
        #why --> many datatypes for which it isnt obvious where to store them (dicts, lists)
        #Pickled files are serialized
        #Serialized --> convert object to a sequence of bytes or bytestream
        
        #Excel spreadsheets, MATLAB, SAS, Stata, HDF5
        
        #Pickled file
        
        import pickle
        
        with open('exemplo.pkl', 'rb') as file :
            #'rb' --> read only AND binary file (PC-based readable, not human readable)
            data = pickle.load(file)
            
        #Excel spreadsheets
        
        file = 'file.xlsx'
        
        data = pd.ExcelFile(file) #pandas function .ExcelFile
        
        print(data.sheet_names) #attribute .sheet_names retorna nome das pastas
        
        df1 = data.parse('Plan1') #method .parse(arg) retorna sheet especificado
        
        df2 = data.parse(0) #tambem aceita index
        
        df1.head() #method .head() mostra 5 primeiros dados (sem conta label)
        
        semvictor = data.parse(0, skiprows=[0], names=['que','q','q','q','q'])
        #<skiprows = > precisa ser lista
        #<names = > esta mudando o nome de cada coluna, precisa ser lista
        
        justmonth = data.parse(0, parse_cols=[0])
        #<parse_cols = > precisa ser lista, pega so a determinada coluna
        #nao ta funcionando por algum motivo
        
        #Directory
        
        import os
        
        wd = os.getcwd() #busca diretorio atual
        
        os.listdir(wd) #lista tudo o que tem
        
    #Importing SAS/Stata files using pandas

        #SAS: "Statistical Analysis System"
        #.sas7bdat --> dataset files
        #.sas7bcat --> catalog files
        
        from sas7bdat import SAS7BDAT
        
        with SAS7BDAT('example.sas7bdat') as file :
            df_sas = file.to_data_frame()
        
        #Stata: "Statistics" + "data"
        #.dta
        
        data = pd.read_stata('example.dta')
    
    #Importing HDF5 files
    
        #HDF5: "Hierarchical Data Format version 5"
        #Standard for huge amounts of numerical data, hundreds of gb or tb
        #Can scale up to exabytes
        
        import h5py
        
        filename = 'example.hdf5'
        
        data = h5py.File(filename, 'r') # 'r' is to read
        
        #hdf5 type file
        #for key in data.keys():
                #print(key)
        
        #meta: meta data for the file
        #quality: refers to data quality
        #strain: strain data from the interferometer
         
    #Importing MATLAB files
    
        #MATLAB: "Matrix Laboratory"
        #.mat
        #scipy.io.loadmat() --> read .mat files
        #scipy.io.savemat() --> write .mat files
        
        import scipy.io
        
        filename = 'example.mat'
        
        mat = scipy.io.loadmat(filename)
        
        #dictionary type!
        
#Working with relational databases in Python

    #Introduction to relational databases
    
        #Based on relational model of data by Edgar 'Ted' Codd in the 1960s
        #Consists of tables
        #Tables --> represent one entity type
        #Each row (or record) represents an instance of the entity type
        #Each column represnts an attribute of each instance of the entity type
        #In this case, analogous to a DataFrame
        #ESSENCIAL: each row contains one unique identifier, 'primary key'
        #'prymary key': explicitly access the row (record) in question
        #In the video example, the key is the first column, ID
        #The tables are linked!
        #By navigating through primary keys of each table present in other tables
        #Saves a bunch of space
        
        #Todd's 12 Rules/Commandments (13 rules, because it is 0 indexed)
        #The first rule is label 0
        
        #Most popular today: PostgreSQL, MySQL, SQLite --> SQL query language
        #SQL --> "Structured Query Language"
        #SQL --> describes how you communicate with a database in order to both
        #access and update the information it contains
        #'Querying' --> getting data out from the database
        
    #Creating a database engine in Pyhon
    
        #How to connect to a database
        
        from sqlalchemy import create_engine
        
        engine = create_engine('sqlite:///example.sqlite') #which database + name
        #poderia ser PostgreSQL ou MySQL, por exemplo
        #called 'connection string'
        
        table_names = engine.table_names() #method .table_names para ver o nome das tables
        
        table_names
        
        #Your first SQL query
        
        from sqlalchemy import create_engine
        
        import pandas as pd
        
        engine = create_engine('sqlite:///example.sqlite')
        
        con = engine.connect() #opens the connection
        
        rs = con.execute("SELECT * FROM x") #(arg) é comando do SQL que puxa so o q vc quer
        #the relevant SQL query
        
        df = pd.DataFrames(rs.fetchall()) #method .fetchall() to turn into dataframe
        #fetchall --> fetches all rows
        #could use --> .fetchmany(size=x), pra escolher tamanho do que e puxado
        
        df.columns = rs.keys() #ajeita os nomes das colunas
        
        con.close() #closes the connection
        
        #Alternativa:
        
        with engine.connect() as con :
            rs = con.execute("SELECT * FROM x")
            df = pd.DataFrame(rs.fetchall())
            df.columns = rs.keys()
            
        #Let's say, for example that you wanted to get all records from the
        #Customer table of the Chinook database for which the Country is 'Canada'.
        #You can do this very easily in SQL using a SELECT statement followed by a
        #WHERE clause as follows:

        SELECT * FROM Customer WHERE Country = 'Canada'
        
        #You can also order your SQL query results.
        #For example, if you wanted to get all records from the Customer table
        #of the Chinook database and order them in increasing order by
        #the column SupportRepId, you could do so with the following query:

        SELECT * FROM Customer ORDER BY SupportRepId
        
    #Querying relational databases directly with pandas

        #Alternatia mais eficiente

        from sqlalchemy import create_engine
        
        import pandas as pd
        
        engine = create_engine('sqlite:///example.sqlite')
        
        df = pd.read_sql_query("SELECT * FROM x", engine) #tcharan
        
    #Advanced Querying: exploiting table relationships
   
        #Tables are linked, use it
        
        #JOIN tables together by their id (especificamente, INNER JOIN)
        
        #Recall that to INNER JOIN the Orders and Customers tables from the Northwind database,
        #Hugo executed the following SQL query:

        SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID
        #para e pensa no codigo que vc vai lembrar que e intuitivo
        
#13.12.2018        
        
                
                
            
        