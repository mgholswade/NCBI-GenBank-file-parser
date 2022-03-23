import pandas as pd
import io
import re
import NCBI_genebank_file_parser as gfp

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

    return tpmdf

def gff3_retrieve():
    #NEW CODE
    gff3_file = open('C:/Users/mghol/Documents/Projects/GenDB/Mattirolomyces_terfezioides.gff3')
    gff3_string = gff3_file.read()

    gff3_string = gff3_string.replace('\\',' ')
    gff3_string = gff3_string.replace('\t',' ')
    gff3_stsring = gff3_string.replace(';',' ')
    gff3_string = re.sub('ID=[\w\-\.]*;','',gff3_string)
    # 2/28 Commented out to try to fix final join
    gff3_string = re.sub(r'Parent=(MTE_[0-9]*)([\w\-\.]*);',r'\1 ',gff3_string)


    #This is super fucked up but I havent figured out how to loop this until there are no more spaces in product tags, this will work as long as names
    #arent longer than 7 words.
    gff3_string = re.sub(r'product=([\S_]*) ',r'product=\1_',gff3_string)
    gff3_string = re.sub(r'product=([\S_]*) ',r'product=\1_',gff3_string)
    gff3_string = re.sub(r'product=([\S_]*) ',r'product=\1_',gff3_string)
    gff3_string = re.sub(r'product=([\S_]*) ',r'product=\1_',gff3_string)
    gff3_string = re.sub(r'product=([\S_]*) ',r'product=\1_',gff3_string)
    gff3_string = re.sub(r'product=([\S_]*) ',r'product=\1_',gff3_string)


    newfile = open('test.txt','w')
    newfile.write(gff3_string)

    f = open("test.txt", "r")
    data = [line.split() for line in f]

    data = data[1:]
    masterList = []
    for line in data:
        newlist = []
        for item in line:
            newlist.append(item)
        masterList.append(newlist)

    df = pd.DataFrame.from_dict(masterList)
    df.columns = ['Scaffold','Source','Type','Start','End','A','B','C','Name','Details']

    return df

def main():
    quantdf = quant_retrieve()
    gff3df = gff3_retrieve()
    gbkdf = gfp.ntgenbank()

    return 0

main()