import pandas as pd
import io
import re

def quant_retrieve():
    fileNames = input('Enter relative paths for quant files to be used, seperated by commas (include .sf): ')
    fileList = fileNames.split(',')

    tpmdf = pd.DataFrame()

    #FIXME 2/7 This block is some shit ass code but its working, fix in future release
    quants_file = open('C:/Users/mghol/Documents/Projects/GenDB/' + fileList[0])
    quants_string = quants_file.read()

    quants_string = quants_string.replace('\\',',')
    quants_string = quants_string.replace('\t',',')
    quants_string = re.sub(r'(MTE_[0-9]*)([\w\-\.]*),',r'\1,',quants_string)

    quants = pd.read_csv(io.StringIO(quants_string))
    Name = pd.DataFrame({'Name':quants['Name']})#,columns=['TPM_'+file]) #FIXME 2/6 Adding column names is resulting in empty df

    tpmdf = pd.concat([tpmdf,Name],axis=1)



    for file in fileList:
        quants_file = open('C:/Users/mghol/Documents/Projects/GenDB/' + file)
        quants_string = quants_file.read()

        quants_string = quants_string.replace('\\',',')
        quants_string = quants_string.replace('\t',',')
        # 2/28 Commented out to try to fix final join
        quants_string = re.sub(r'(FUN_[0-9]*)([\w\-\.]*),',r'\1,',quants_string)

        quants = pd.read_csv(io.StringIO(quants_string))
        
        TPM = pd.DataFrame({file:quants['TPM']})#,columns=['TPM_'+file]) #FIXME 2/6 Adding column names is resulting in empty df
        
        tpmdf = pd.concat([tpmdf,TPM],axis=1)

    return 0
