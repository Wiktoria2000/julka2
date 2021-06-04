# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:13:17 2021

@author: Wiktoria
"""
from math import atan, tan, cos, sin, sqrt, pi
import pandas as pd
import numpy as np 

import streamlit as st 
import streamlit

dane = pd.read_excel('DANE.xlsx')
#dane = pd.read_excel('C:/Users/Wiktoria/Desktop/SEMESTR 4/INFOMATYKA 2/ĆWICZENIA/PROJEKT/DANE.xlsx')


dane.index = dane['MIASTO'] #zamiana ineskow 1,2,3 na nazwy miast 
a = input('Miejsce wylotu ')
b = input('Miejsce lądowania  ')

#przyporządkowanie do konkretnej komórki 
h_fi = dane.loc[a,'H_(FI)']
m_fi = dane.loc[a,'M_(FI)']
s_fi = dane.loc[a,'S_(FI)']
h_l = dane.loc[a,'H_(L)']
m_l = dane.loc[a,'M_(L)']
s_l = dane.loc[a,'S_(L)']

h_fi2 = dane.loc[b,'H_(FI)']
m_fi2 = dane.loc[b,'M_(FI)']
s_fi2 = dane.loc[b,'S_(FI)']
h_l2 = dane.loc[b,'H_(L)']
m_l2 = dane.loc[b,'M_(L)']
s_l2 = dane.loc[b,'S_(L)']

lB = np.deg2rad(h_l2 + m_l2/60 + s_l2/3600)
lA = np.deg2rad(h_l + m_l/60 + s_l/3600)
fA = np.deg2rad(h_fi + m_fi/60 + s_fi/3600)
fB = np.deg2rad(h_fi2 + m_fi2/60 + s_fi2/3600)

#VINCENT (ODLEGLOSC MIEDZY LOTNISKAMI)
a = 6378137
e2 = 0.0066943800

b=a*(1-e2)**0.5;
f=1-(b/a);
L=lB-lA;
U1 = atan((1-f)*tan(fA));
U2 = atan((1-f)*tan(fB));
# trzeba dopisac poczatek czyli przeniesienie na sfere do szerokosci zredukowanych
i=0;
La=L;
while 1:
    i=i+1;
    sd=sqrt(((cos(U2))*(sin(La)))**2+((cos(U1))*(sin(U2))-(sin(U1))*(cos(U2))*(cos(La)))**2);
    cd=(sin(U1))*(sin(U2))+(cos(U1))*(cos(U2))*(cos(La));
    d=atan(sd/cd);
    sa=(cos(U1))*(cos(U2))*(sin(La))/sd;
    c2dm=cd-2*(sin(U1))*(sin(U2))/(1-sa**2);
    
    C=(f/16)*(1-sa**2)*(4+f*(4-3*(1-sa**2)));
    Ls=La;
    La=L+(1-C)*f*sa*(d+C*sd*(c2dm+C*cd*(-1+2*c2dm**2)));
    
    if abs(La-Ls)<(0.000001/206265):
        break
    


u2=(((a**2)-(b**2))/(b**2))*(1-(sa)**2);
A=1+((u2)/16384)*(4096+(u2)*(-768+(u2)*(320-175*(u2))));
B=((u2)/1024)*(256+(u2)*(-128+(u2)*(74-47*(u2))));
dd=B*(sd)*((c2dm)+(0.25)*B*((cd)*(-1+2*(c2dm)**2)-(1/6)*B*(c2dm)*(-3+4*(sd)**2)*(-3+4*(c2dm)**2)));

s=b*A*(d-dd);
AAB=atan(((cos(U2))*(sin(Ls)))/((cos(U1))*(sin(U2))-(sin(U1))*(cos(U2))*(cos(Ls))));
ABA=atan(((cos(U1))*(sin(Ls)))/(((-sin(U1)))*(cos(U2))+(cos(U1))*(sin(U2))*(cos(Ls))))+pi;

#spalanie



if AAB<0:
    AAB=AAB+pi;
    ABA=ABA+pi;
    
print('DLUGOSC LOTU MIĘDZY LOTNISKAMI:',round(s,3),'m')
s = round(s,3)/1000
c = 4.52
p = 320000
spalanie = (1800*s)/100
cena = c*spalanie
print(round(cena,2),'zł')
cena_na_osobe = cena/544
print(round(cena_na_osobe,2),'zł')

#waga bagazu

k = input('Podaj klasę lotu:\n -klasa ekonomiczna\n -pierwsza klasa\n -biznes klasa\n  ')

w_podreczna = int(input('Podaj wagę twojego bagażu podręcznego: '))
w_dodatkowa = int(input('Podaj wagę twojego bagażu dodatkowego: '))

if k == 'biznes klasa':
    podstawa = 300
    if w_dodatkowa > 32:
        print('Twój bagaż dodatkowy przekracza dopuszcalną wagę (max 32kg)! Zmniejsz wagę bagażu. ')
    if w_dodatkowa <= 32:
        print('Waga bagażu dodatkowego dopuszczalna!')
    if w_podreczna < 8:
        cena_biletu = cena_na_osobe + podstawa
    if w_podreczna >= 8:
        cena_biletu = cena_na_osobe + 360 + podstawa
        print('Twój bagaż podręczny przekracza 8kg! Cena biletu wzrosła do',round(cena_biletu,2),'zł')
        

if k == 'klasa ekonomiczna':
    podstawa = 100
    if w_dodatkowa > 23:
        print('Twój bagaż dodatkowy przekracza dopuszcalną wagę (max 23kg)! Zmniejsz wagę bagażu. ')
    if w_dodatkowa <= 23:
        print('Waga bagażu dodatkowego dopuszczalna!')
    if w_podreczna < 8:
        cena_biletu = cena_na_osobe + podstawa
    if w_podreczna >= 8:
        cena_biletu = cena_na_osobe + 360 + podstawa
        print('Twój bagaż podręczny przekracza 8kg! Cena biletu wzrosła do',round(cena_biletu,2),'zł')
        
if k == 'pierwsza klasa':
    podstawa = 200
    if w_dodatkowa > 32:
        print('Twój bagaż dodatkowy przekracza dopuszcalną wagę (max 32kg)! Zmniejsz wagę bagażu. ')
    if w_dodatkowa <= 32:
        print('Waga bagażu dodatkowego dopuszczalna!')
    if w_podreczna < 8:
        cena_biletu = cena_na_osobe + podstawa
    if w_podreczna >= 8:
        cena_biletu = cena_na_osobe + 360 + podstawa
        print('Twój bagaż podręczny przekracza 8kg! Cena biletu wzrosła do',round(cena_biletu,2),'zł')

import datetime
    
t = (s/800 + 0.3)*3600

time = str(datetime.timedelta(seconds=t))
print("Przewdywany czas lotu",time,'h' )


        #julka jest fajna
        
        
        ############
    import requests, json
  
# Enter your API key here
api_key = "f9f59afb6ef10c4cc9553041ea8d9882"
  
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name
city_name = input("Enter city name : ")
  
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
# get method of requests module
# return response object
response = requests.get(complete_url)
  
# json method of response object 
# convert json format data into
# python format data
x = response.json()
  
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
  
    # store the value of "main"
    # key in variable y
    y = x["main"]
  
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
  
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
  
    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]
  
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
  
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z
    weather_description = z[0]["description"]
  
    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))
  
else:
    print(" City Not Found ")





