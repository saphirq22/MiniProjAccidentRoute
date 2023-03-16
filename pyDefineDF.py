import pandas as pd

# pip install -r requirements.txt

pathCa = "C:/Users/saphi/OneDrive/Documents/miniProjPy/carcteristiques-2021-1.csv"
pathLi = "C:/Users/saphi/OneDrive/Documents/miniProjPy/lieux-2021.csv"
pathUs = "C:/Users/saphi/OneDrive/Documents/miniProjPy/usagers-2021.csv"
pathVh = "C:/Users/saphi/OneDrive/Documents/miniProjPy/vehicules-2021.csv"
pathPo = "C:/Users/saphi/OneDrive/Documents/miniProjPy/Departements.csv"

laFranceEntiere = ['1','2','3','4','5','6','7','8','9',
                   '10','11','12','13','14','15','16','17','18','19',
                   '21','22','23','24','25','26','27','28','29',
                   '30','31','32','33','34','35','36','37','38','39',
                   '40','41','42','43','44','45','46','47','48','49',
                   '50','51','52','53','54','55','56','57','58','59',
                   '60','61','62','63','64','65','66','67','68','69',
                   '70','71','72','73','74','75','76','77','78','79',
                   '80','81','82','83','84','85','86','87','88','89',
                   '90','91','92','93','94','95',
                   '971','972','973','974','975','976','977','978',
                   '986','987','988', '2A', '2B']

AuvRhoAlpes =	['1', '3', '7', '15', '26', '38', '42', '43', '63', '69', '73', '74']	
BourFraCom = ['21', '25', '39', '58', '70',	'71', '89', '90']					
Bretagne = 	['22', '29', '35', '56']									
CenVaLoi=	['18', '28', '36', '37', '41', '45']							
Corse =	['2A', '2B']												
GraEst =	['8', '10',	'51', '52',	'54', '55', '57', '67',	'68', '88']			
HaudeFra =	['2', '59', '60', '62', '80']								
Idf =	['75', '77', '78', '91', '92', '93', '94', '95']					
Norman =	['14', '27', '50', '61', '76']								
NouvAqui =	['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87']	
Occitanie = ['9', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82']
PaysLoire =	['44', '49', '53', '72', '85']								
Paca= ['4', '5', '6', '13', '83', '84']							
Drom= ['971','972','973','974','975','976','977','978','986','987','988']

def DefineDF(maRegion):
    #def des data frame
    dfCa=pd.read_csv(pathCa, sep=";") #, on_bad_lines='skip')
    dfLi=pd.read_csv(pathLi, sep=";") #, on_bad_lines='skip')
    dfUs=pd.read_csv(pathUs, sep=";") #, on_bad_lines='skip')
    dfVh=pd.read_csv(pathVh, sep=";") #, on_bad_lines='skip')

    dfVhUs = dfVh.merge(dfUs,on=['Num_Acc','num_veh'])
    dfCaLi = dfCa.merge(dfLi,on = 'Num_Acc')
    df = dfVhUs.merge(dfCaLi,on='Num_Acc')
    df = df.sort_values(by=['Num_Acc', 'grav', 'catv'], ascending=False)

    df = df[df.dep.isin(maRegion)]

    return df

"""     del dfCa
    del dfLi
    del dfUs
    del dfVh
    del dfVhUs
    del dfCaLi
    gc.collect() """


def DefineDFca(maRegion):
    df = pd.read_csv(pathCa, sep=";")
    df = df[df.dep.isin(maRegion)]
    return df

def DefineDFus(maRegion):
    df = pd.read_csv(pathUs, sep=";")
    dfCa = pd.read_csv(pathCa, sep=";")

    df = df.merge(dfCa, on =['Num_Acc'] )
    df = df[df.dep.isin(maRegion)]
    df = df.drop(columns=["jour","mois","an","hrmn","lum","dep","com","agg","int","atm","col","adr","lat","long"])
    return df

def DefineDFvh(maRegion):
    df = pd.read_csv(pathVh, sep=";")
    dfCa = pd.read_csv(pathCa, sep=";")
    df = df.merge(dfCa, on ='Num_Acc' )
    df = df[df.dep.isin(maRegion)]
    df = df.drop(columns=["jour","mois","an","hrmn","lum","dep","com","agg","int","atm","col","adr","lat","long"])
    return df

def DefineDFli(maRegion):
    df = pd.read_csv(pathLi, sep=";")
    dfCa = pd.read_csv(pathCa, sep=";")
    df = df.merge(dfCa, on ='Num_Acc' )
    df = df[df.dep.isin(maRegion)]
    df = df.drop(columns=["jour","mois","an","hrmn","lum","dep","com","agg","int","atm","col","adr","lat","long"])
    return df

def DefineDFpo(maRegion):
    df = pd.read_csv(pathPo, sep=";")
    df = df.astype({"CODDEP": "str"})
    df = df[df.CODDEP.isin(maRegion)]
    return df

def DefineDFVhUs(maRegion):
    dfUs=pd.read_csv(pathUs, sep=";") #, on_bad_lines='skip')
    dfVh=pd.read_csv(pathVh, sep=";")
    dfVhUs = dfVh.merge(dfUs,on=['Num_Acc', 'num_veh'])

    dfCa = pd.read_csv(pathCa, sep=";")
    df = dfVhUs.merge(dfCa, on ='Num_Acc' )
    df = df[df.dep.isin(maRegion)]
    df = df.drop(columns=["jour","mois","an","hrmn","lum","dep","com","agg","int","atm","col","adr","lat","long"])
    return df