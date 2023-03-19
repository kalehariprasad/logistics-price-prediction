# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:18:10 2023

@author: User
"""

import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np
model=pickle.load(open('model','rb' ))

st.title('Consignment Price Prediction')



country=st.selectbox('country', sorted(('Vietnam', 'Congo, DRC', 'South Sudan', 'South Africa', 'Rwanda',
           'Nigeria', 'Mozambique', 'Guyana', 'Burundi', 'Zambia', 'Uganda',
           "Côte d'Ivoire", 'Zimbabwe', 'Tanzania', 'Haiti', 'Benin',
           'Dominican Republic', 'Kenya', 'Swaziland', 'Ethiopia', 'Cameroon',
           'Namibia', 'Afghanistan', 'Mali', 'Sudan', 'Botswana', 'Togo',
           'Pakistan', 'Lesotho', 'Malawi', 'Guatemala', 'Liberia', 'Ghana',
           'Lebanon', 'Sierra Leone', 'Belize', 'Angola', 'Libya', 'Senegal',
           'Burkina Faso', 'Kyrgyzstan', 'Kazakhstan', 'Guinea')))
managedby=st.selectbox('management', sorted(('PMO - US', 'South Africa Field Office', 'Haiti Field Office',
           'Ethiopia Field Office')))

full_fill_via=st.selectbox('fullfii via',sorted (('Direct Drop', 'From RDC')))

vendor_inco= st.selectbox('vendor inco TERM', sorted(('EXW', 'FCA', 'DDU', 'CIP', 'DDP', 'CIF', 'N/A - From RDC', 'DAP')))

shipment_mode= st.selectbox('shipment mode', sorted(('Air', 'Truck', 'Air Charter', 'Ocean')))
        
product_group= st.selectbox("product group", sorted(('HRDT', 'ARV', 'ACT', 'MRDT', 'ANTM')))


sub_classification = st.selectbox('Sub Classification', sorted(('HIV test', 'Pediatric', 'Adult', 'HIV test - Ancillary', 'ACT',
           'Malaria')))

Brand = st.selectbox('Brand',sorted(('Reveal', 'Generic', 'Determine', 'Stocrin/Sustiva', 'Aluvia',
           'Uni-Gold', 'InstantCHEK', 'Videx', 'First Response', 'Stat-Pak',
           'OraQuick', 'Bioline', 'Retrovir', 'Viread', 'Zerit', 'Capillus',
           'Genie', 'Invirase', 'Videx EC', 'Ziagen', 'Coartem', 'Viramune',
           'Paramax', 'Atripla', 'Kaletra', 'Epivir', 'Norvir', 'Truvada',
           'Clearview', 'Colloidal Gold', 'INSTi', 'Trizivir', 'Visitect',
           'Viracept', 'DoubleCheck', 'Bundi', 'ImmunoComb', 'Crixivan',
           'LAV', 'Pepti-LAV', 'Intelence', 'Prezista', 'Isentress',
           'Reyataz', 'Combivir', 'Multispot', 'CareStart', 'Hexagon')) )


dosage_form = st.selectbox('Dosage form', sorted(('Test kit', 'Oral suspension', 'Tablet', 'Capsule',
           'Oral solution', 'Tablet - FDC', 'Powder for oral solution',
           'Test kit - Ancillary', 'Chewable/dispersible tablet',
           'Delayed-release capsules - blister', 'Tablet - blister',
           'Tablet - FDC + blister', 'Tablet - FDC + co-blister', 'Injection',
           'Delayed-release capsules', 'Chewable/dispersible tablet - FDC',
           'Oral powder')))

line_item_quantity = st.number_input('item quantity')

First_Line_Designation = st.selectbox('item is in First Line Designation', sorted(('yes','No')))

weight =st.number_input('weight in kilo grams')
    

if st.button('Predict Price'):
    user_input= np.array([country,managedby,full_fill_via,vendor_inco,shipment_mode,product_group,sub_classification,Brand,dosage_form,line_item_quantity,First_Line_Designation,weight])

   

    user_input=user_input.reshape(1,12)
    
    st.title('price will be   $'+  str(float(model.predict(user_input)[0])))
   
    
   