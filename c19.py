# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:16:01 2020

@author: praneeth
"""
from covid import Covid
import matplotlib.image as mpimg 
import streamlit as sl
import pandas as pd
c19=Covid(source="worldometers")
sl.write("""
# COVID-19 CORONAVIRUS PANDEMIC
""")
img = mpimg.imread('vir.jpg')
sl.image(img,use_column_width=True,caption='CORONA VIRUS')
sym = mpimg.imread('advice.jpg')
sl.sidebar.image(sym,use_column_width=True)
def user_input_features():
    sl.sidebar.subheader('**REGION:**')
    region=sl.sidebar.selectbox('select the country',('world','usa','brazil','india','russia','south africa','mexico','peru','chile','spain','uk','iran','pakistan','saudi arabia','colombia','italy','bangladesh','turkey','germany','france','argentina','iraq','canada','qatar','indonesia','egypt','kazakhstan','philippines','ecuador','sweden','oman','bolivia','belarus','ukraine','belgium','israel','kuwait','dominican republic','panama','uae','netherlands','singapore','portugal','romania','guatemala','poland','nigeria','honduras','bahrain','armenia','afghanistan','switzerland','kyrgyzstan','ghana','azerbaijan','japan','algeria','ireland','serbia','moldova','uzbekistan','morocco',
'austria',
'nepal',
'kenya',
 'cameroon',
 'venezuela',
 'costa rica',
 'czechia',
 'ivory coast',
 'el salvador',
 'australia',
 'ethiopia',
 's. korea',
 'denmark',
 'sudan',
 'palestine',
 'bosnia and herzegovina',
 'bulgaria',
 'north macedonia',
 'madagascar',
 'senegal',
 'norway',
 'malaysia',
 'drc',
 'french guiana',
 'finland',
 'haiti',
 'tajikistan',
 'gabon',
 'guinea',
 'luxembourg',
 'mauritania',
 'djibouti',
 'zambia',
 'albania',
 'croatia',
 'car',
 'paraguay',
 'hungary',
 'greece',
 'lebanon',
 'malawi',
 'nicaragua',
 'maldives',
 'thailand',
 'congo',
 'somalia',
 'equatorial guinea',
 'mayotte',
 'montenegro',
 'hong kong',
 'libya',
 'sri lanka',
 'zimbabwe',
 'cuba',
 'mali',
 'cabo verde',
 'eswatini',
 'south sudan',
 'slovakia',
 'slovenia',
 'estonia',
 'lithuania',
 'guinea-bissau',
 'namibia',
 'rwanda',
 'iceland',
 'sierra leone',
 'benin',
 'mozambique',
 'yemen',
 'new zealand',
 'suriname',
 'tunisia',
 'latvia',
 'uruguay',
 'jordan',
 'liberia',
 'georgia',
 'uganda',
 'niger',
 'burkina faso',
 'cyprus',
 'angola',
 'chad',
 'andorra',
 'togo',
 'sao tome and principe',
 'jamaica',
 'botswana',
 'diamond princess',
 'malta',
 'san marino',
 'syria',
 'réunion',
 'channel islands',
 'tanzania',
 'lesotho',
 'taiwan',
 'vietnam',
 'guyana',
 'bahamas',
 'burundi',
 'comoros',
 'myanmar',
 'mauritius',
 'isle of man',
 'gambia',
 'mongolia',
 'martinique',
 'eritrea',
 'cambodia',
 'faeroe islands',
 'guadeloupe',
 'cayman islands',
 'gibraltar',
 'bermuda',
 'trinidad and tobago',
 'brunei',
 'aruba',
 'monaco',
 'sint maarten',
 'seychelles',
 'barbados',
 'turks and caicos',
 'bhutan',
 'antigua and barbuda',
 'liechtenstein',
 'papua new guinea',
 'french polynesia',
 'st. vincent grenadines',
 'saint martin',
 'belize',
 'macao',
 'curaçao',
 'fiji',
 'saint lucia',
 'timor-leste',
 'grenada',
 'new caledonia',
 'laos',
 'dominica',
 'saint kitts and nevis',
 'greenland',
 'falkland islands',
 'montserrat',
 'vatican city',
 'caribbean netherlands',
 'western sahara',
 'ms zaandam',
 'british virgin islands',
 'st. barth',
 'saint pierre miquelon',
 'anguilla',
 'china'))
    return region 
reg=user_input_features()
sl.write("#Coronaviurs **Cases** Tracker")
sl.title("Live Updates")         
sl.subheader("Total **Conformed** Cases: "+str(c19.get_total_confirmed_cases()))
sl.subheader("Total **Active** Cases: "+str(c19.get_total_active_cases()))
sl.subheader("Total **Recovered** Cases: "+str(c19.get_total_recovered()))
sl.subheader("Total **Deaths** : "+str(c19.get_total_deaths()))
ad = mpimg.imread('flat.jpg')
sl.image(ad,use_column_width=True,caption='To stay safe is to save lives!')
def results(reg):
    p=c19.get_status_by_country_name(reg)
    df=pd.DataFrame(p,index=['count'])
    df1=df.T
    return df1
df=results(reg)
sl.header("COVID 19-"+reg+":")
sl.table(df)
sl.title("Know The Symptoms")
ad1 = mpimg.imread('sym.jpg')
sl.image(ad1,use_column_width=True,caption='Know The Symptoms')
sl.write(""" **Most common symptoms**:
-fever
-dry cough
-tiredness""")
sl.write("""**Less common symptoms**:
-aches and pains
-sore throat
-diarrhoea
-conjunctivitis
-headache
-loss of taste or smell
-a rash on skin,or discolouration of fingers or toes""")
sl.write("""**Serious symptoms**:
-difficulty breathing or shortness of breath
-chest pain or pressure
-loss of speech or movement""") 
sl.write("Seek **immediate** medical attention if you have **serious symptoms**. Always call before visiting your doctor or health facility.People with mild symptoms who are otherwise healthy should manage their symptoms at home.On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to **14 days**.")
sl.title("Precautions To Take:")
sl.header("Protect yourself and others from the spread COVID-19") 
sl.write("While stepping out, make sure to cover your nose and mouth with a **mask**. Here take a look at how you should wear a **mask** and the right way to dispose of it. ")
face = mpimg.imread('face1.jpg')
sl.image(face,use_column_width=True,caption="Keep your mouth tight and masked, just kill the demon to heal the earth, the Coronavirus")
sl.write("**Avoid** outside exposure to suspected areas and infected people")
home = mpimg.imread('home.jpg')
sl.image(home,use_column_width=True,caption='**To stay safe is to save lives!**')
sl.write("**Wash hands** with soap and water. Also, it is advisable to use an alcohol-based sanitizer (Recommended brands include- Lifebuoy: Immunity Boosting hand Sanitizer/Dettol: Original Instant Hand Sanitizer)")
hand = mpimg.imread('hands.jpg')
sl.image(hand,use_column_width=True,caption='**Don’t be a bum, wash off the scum**')
sl.write("Keep your hands and fingers away from nose, eyes, and mouth. By doing so, you will eliminate the chances of the **virus spreading** if it is on your hands.")
sl.write("Thorough washing and cooking of meat **before** consuming is advised")
sl.title("Salute the courage and energy of corona warriors. Feels like God has taken avatar in form of corona warriors. Thanks!")  
