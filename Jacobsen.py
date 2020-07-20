import tabula
import time
import pandas as pd
import csv



df = pd.concat(tabula.read_pdf("Corn-Comp-Chart.pdf", area = (120, 65, 1010, 920), guess=False, pandas_options={'header': None}))

df.to_csv(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Jacobsen.csv", sep='\t', index=False, header=False, mode='a', columns=[0,1])

df2 = pd.concat(tabula.read_pdf("Soybeans-Comp-Chart-1.pdf", area = (120, 65, 642, 920), guess=False, pandas_options={'header': None}))

df2.to_csv(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Jacobsen.csv", sep='\t', index=False, header=False, mode='a', columns=[0,1])
Brand="Jacobsen"

with open(r"C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Jacobsen.csv") as f1:
    for line in f1:
        entry = line.split('\t')
        product = entry[0]
        if "SS RIB" in entry[0]:
            trait = "SS RIB"
        elif "3111" in entry[0]:
            trait = "3111"
        elif "3000GT" in entry[0]:
            trait = '3000GT'
        elif "VT2 PRO RIB" in entry[0]:
            trait = 'VT2 PRO RIB'
        elif "GTCBLL" in entry[0]:
            trait = 'GTCBLL'
        elif "RR" in entry[0]:
            trait = 'RR'
        elif "NR2X" in entry[0]:
            trait = "NR2X"
        elif "R2X" in entry[0]:
            trait = "R2X"
        elif "NR2" in entry[0]:
            trait = "NR2"
        elif "GTLL" in entry[0]:
            trait = "GTLL"
        elif "GT" in entry[0]:
            trait = "GT"
        elif "E3" in entry[0]:
            trait = "E3"
        elif "LL" in entry[0]:
            trait = "LL"
        else: 
            trait = "None"
        relativeMaturity = entry[1].replace("\n", "")
        if "." in relativeMaturity:
            cropType="Soybeans"
        else:
            cropType="Corn"
        with open(r'C:\Users\rkeenan\OneDrive - Aurora Cooperative\Documents\Development\Seed Website Scrapers\Products.csv', 'a') as f1:
            f1.write(Brand + "\t" + product + "\t" + trait  + "\t" + "None" + "\t" + relativeMaturity + "\t" + cropType + "\n")