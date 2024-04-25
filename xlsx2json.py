# import pandas lib as pd
import pandas as pd
import sys
import os.path
from  json import loads, dump

# total arguments
while(len(sys.argv) != 3):
    print("Usage: python xlsx2json.py <xlsx filename> <json output filename>\n")

if (not os.path.isfile(sys.argv[1])):
    print("Invalid file!")

banks = pd.read_excel('tmpl.xlsx')

# read by default 1st sheet of an excel file
 
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    banks.to_json(f, orient="records", force_ascii=False)
