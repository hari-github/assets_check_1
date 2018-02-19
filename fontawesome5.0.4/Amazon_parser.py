import csv
from bs4 import BeautifulSoup
import pandas as pd
dat = pd.read_csv("C:\Users\hari.prakash\Downloads//amazon_cooktops.csv")
print len(dat['Field2'])
sku=[]
prd=[]
sku.append(dat['Field1'][0])
print len(dat['Field2'])
sku=[]
prd=[]
i = 0
Spec = pd.DataFrame()
for j in range(len(dat)):
    v = dat['Field5'][j]
    id_2 = dat['Field1'][j]
    id_1 = dat['Field4'][j]
    sku=[]
    prd=[]
    prd.append(dat['Field1'][j])
    sku.append(dat['Field4'][j])
    #Spec1 = pd.DataFrame(data = {'prd_id' : id_2 , 'sku_id' : id_1})
    
    if (v==1):
        print j
        sku=[]
        prd=[]
        prd.append(dat['Field1'][j])
        
        
        id_2 = dat['Field1'][j]
        id_1 = dat['Field4'][j]
        Spec1 = pd.DataFrame(data = {'prd_id' : prd , 'sku_id' : id_1})
        par = dat['Field2'][j]
        #print dat['Field1'][j]
        soup = BeautifulSoup(par, 'html.parser')

        #print len(data2)
        #label=data2.findAll('div',{'class':''})
        tbl=soup.find('table',{'id':'productDetails_techSpec_section_1'})
        rows = tbl.findAll('tr')
        var_sku = 'prd_id'
        Spec1[var_sku] = id_2
        Spec1['sku_id'] = id_1


        for tr in rows:
            cols = tr.findAll('th')
            #print cols.text
            for td in cols:
                tit = td.text
                #print tit
                #print td.find(text=True)
            cols = tr.findAll('td')
            #print cols.text
            for td in cols:
                val = td.text
                #print val
            Spec1[tit] = val
            i = i + 1
        
            
            

        #print Spec1
        
    Spec = Spec.append(Spec1)
    #print Spec
        
    #print "-------------------------------------------------------------------"
    Spec.to_csv( "C:\Users\hari.prakash\Documents//parsed_data_amazon_n.csv", index=False,quoting=csv.QUOTE_ALL)