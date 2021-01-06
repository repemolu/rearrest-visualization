#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:26:37 2020

@author: rebecca
"""
"""
sources
https://data.cityofnewyork.us/Public-Safety/DOP-Juvenile-Rearrest-Rate-Monthly-Average-/c87b-2j3i
https://data.cityofnewyork.us/Public-Safety/DOP-Adult-Rearrest-Rate-Monthly-Average-/gk9u-c3tv
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graph1(y,r,y2,r2):
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
    plt.clf()
    plt. title("Citywide Juvenile Probationers Rearrest Rates")
    n = list(range(1,13))
    m = months.split()
    plt.xticks(n,m)
    plt.xlabel("Months")
    plt.ylabel("Rearrest Rates (%)")
    plt.plot(n,r,color="black",marker='o',label = y)
    plt.plot(n,r2,color="red",marker='o',label=y2)
    plt.legend(loc="upper right")
    plt.show()

def adults_rearrests():
    adult_rates = pd.read_csv('DOP_Adult_Rearrest_Rate__Monthly_Average_.csv')
    

    
    

    a_new = adult_rates.drop([0,1,2,3,4,5,6,7,8,9,46,47,48,49])

    a_rates_list = a_new['Rate'].tolist()


   

    a_rates_2017 = a_rates_list[0:12]
    a_rates_2018 = a_rates_list[12:24]
    a_rates_2019 = a_rates_list[24:36]

    a_rates_dict = {}

#    years = ('2017','2018','2019')

#    rate_year = (rates_2017, rates_2018, rates_2019)

    a_rates_dict['2017'] = a_rates_2017
    a_rates_dict['2018'] = a_rates_2018 
    a_rates_dict['2019'] = a_rates_2019 
    

    
    r= a_rates_dict['2017']
    r2= a_rates_dict['2018']
    r3= a_rates_dict['2019']
    bars = np.add(r, r2).tolist()

   
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
    plt.clf()
    plt. title("Citywide Adult Probationer Rearrest Rates")
    n = list(range(1,13))
    m = months.split()
    plt.xticks(n,m)
    plt.xlabel("Months")
    plt.ylabel("Rearrest Rates (%)")
    plt.bar(n,r,color="steelblue",edgecolor='white',label= '2017')
    plt.bar(n,r2,color="dimgray",edgecolor='white', bottom=r, label= '2018')
    plt.bar(n,r3,color="cornflowerblue",edgecolor='white',bottom=bars,label= '2019')
    plt.legend(loc='lower right' )
    plt.show()

def juvenile_rearrests():
    
    rates = pd.read_csv('DOP_Juvenile_Rearrest_Rate__Monthly_Average.csv')

    new = rates.drop([0,1,2,3,4,5,6,7,8,9,46,47,48,49])

    rates_list = new['Rate'].tolist()



    rates_2017 = rates_list[0:12]
    rates_2018 = rates_list[12:24]
    rates_2019 = rates_list[24:36]

    rates_dict = {}

#    years = ('2017','2018','2019')

#    rate_year = (rates_2017, rates_2018, rates_2019)


    rates_dict['2017'] = rates_2017
    rates_dict['2018'] = rates_2018 
    rates_dict['2019'] = rates_2019 
    
    

    
    year_requested = input('Which year do you want to see? (choose from 2017-2019)   ')
    year_requested2 = input("Insert a second year (from 2017-2019).   ")
    if year_requested in rates_dict and year_requested2 in rates_dict:
          
          graph1(year_requested,rates_dict[year_requested],year_requested2,rates_dict[year_requested2])
    
    else:
            print ("We do not have data for either or both of those years.")
    

    


