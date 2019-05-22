import pandas as pd,glob,xlrd,os
import numpy as np
from operator import is_not
from functools import partial
from pathlib import Path
import tkinter as tk
from tkinter import Frame
import datetime
import csv,re
r = tk.Tk()         
r.title('Ericsson_CQ_Generator')
from tkinter import filedialog
#file_Path=(r'C:\Ericsson\CQ\CIQ_to_CQ\Complete AT03EN001 ERC 2.5 TDD 2018_06_27_13_47_11.xlsx.xlsx')
#fun(file_Path)

list_=[]

def fun3(frame):
    list_.append(frame)


def fun(file_Path,con,band):
    file1 = pd.read_excel(file_Path, 'eUtran Parameters')
    #print(file1['Band'],file1['Band'][:1].__contains__('1900'))
    #if file1['Band'].__contains__('1900'):
    file_eNB_info = pd.read_excel(file_Path, 'eNB Info')
    sector_length= file_eNB_info['numberOfSectors_per_DUL']
    sector_length=sector_length[:1]
    l=int(sector_length)
    print('length=',l)

    #print("sat")
    #print("Converting '{}'")
    list1=['Ericsson','Ericsson','Ericsson']
    list1=list1[:l]
    #Beamwidth=[None]*3
    Beamwidth=['65','65','65']
    Beamwidth=Beamwidth[:l]
    config=[con,con,con]
    config=config[:l]
    channel_type=['1','1','1']
    channel_type=channel_type[:l]
    list5=pd.datetime.today().strftime("%m/%d/%Y");
    list6=[list5,list5,list5]
    list6=list6[:l]
    Sector_id= [None]*3
    Switch_Name=[None]*3
    Market_Name=[None]*3
    #Cascade=[None]*3
    Cluster_Name=[None]*3
    lst=list
    n=l
    j=0;
    for i in range(n):
       j=j+1
       #list7.append(j)
       Sector_id.insert(i,j)
    Sector_id=Sector_id[:l]
    print(Sector_id)

    #print(final_list,list6)
    list_fixeValues=pd.DataFrame({})
    try:
        #file1= pd.read_excel(file_Path,'eUtran Parameters')
        Market_Name.insert(0,file1.loc[0,'Market'])
        Cascade =file1.loc[0,'Cascade_ID']
        #band = file1.loc[0, 'Band']
        Market_Name=Market_Name[:l]
        print(Market_Name)
        Switch_Name.insert(0,'LTE_'+file1.loc[0,'Market']+'_SWITCH')
        Switch_Name=Switch_Name[:l]
        print(Switch_Name)
        sector_id_file=pd.DataFrame(np.column_stack([Sector_id]), columns=['SECTORID'])
        Beamwidth_file =pd.DataFrame(np.column_stack([Beamwidth]), columns=['BEAMWIDTH'])

        #sector_id_file = pd.DataFrame(np.column_stack([sector_id]), columns=['SECTORID'])
        final_list6 = pd.DataFrame(np.column_stack([config, channel_type]),
                                   columns=['CONFIG', 'CHANNEL_TYPE'])
        final_list1 = pd.DataFrame(np.column_stack([list6, list1,Market_Name, Switch_Name]),
                                  columns=['DATE', 'VENDORNAME','MARKET_NAME','Switch_Name'])

        final_list1=final_list1.fillna(method='ffill').head()
        print('Final_List1=',final_list1)
        #print(final_list1[['Switch_Name','MARKET_NAME']])

        file2= pd.read_excel(file_Path,'PCI')
        #print(file1[['Market','Cascade_ID','eNBId','latitude','longitude','beamDirection','earfcn']])
        final_list2=file1[['Cascade_ID','eNBId']]
        #final_list2 = pd.DataFrame(np.column_stack([Cascade_ID,eNBId]),
                                 #  columns=['CASCADE', 'ENODEBID'])
        final_list2= final_list2[0:l]
        print('Final_List2=',final_list2)
        final_list3 = file1[['latitude','longitude','beamDirection']]
        #final_list3 = pd.DataFrame(np.column_stack([latitude,longitude,beamDirection]),
                            #       columns=['LATITUDE', 'LONGITUDE','AZIMUTH'])
        final_list3 = final_list3[0:l]
        print('Final_List3=', final_list3)
        if con.__eq__('20'):
           final_list5 = file1[['earfcn', 'Band']]
           #final_list3 = pd.DataFrame(np.column_stack([earfcn, Band]),
                                   #columns=['CHANNEL_NUMBER', 'BAND_CLASS'])
           final_list5 = final_list5[0:l]
           print('Final_List5=', final_list5)
        else:
            final_list5 = file1[['earfcnDl', 'Band']]
            # final_list3 = pd.DataFrame(np.column_stack([earfcn, Band]),
            # columns=['CHANNEL_NUMBER', 'BAND_CLASS'])
            final_list5 = final_list5[0:l]
            print('Final_List5=', final_list5)

        #print(file1_new)
        pci= file2['PCI']
        pci=pci[0:l]
        pci_file = pd.DataFrame(np.column_stack([pci]), columns=['SECTOR_IDENTIFIER'])
        cluster_file = pd.DataFrame(np.column_stack([Cluster_Name]), columns=['CLUSTER_NAME'])
        final_file= pd.concat([final_list1,final_list2,sector_id_file,final_list3,Beamwidth_file,pci_file,cluster_file,final_list5,final_list6], axis=1)
        final_file.columns=['DATE','VENDORNAME','MARKET_NAME','SWITCH_NAME','CASCADE','ENODEBID','SECTORID','LATITUDE','LONGITUDE','AZIMUTH','BEAMWIDTH','SECTOR_IDENTIFIER','CLUSTER_NAME','CHANNEL_NUMBER','BAND_CLASS','CONFIG','CHANNEL_TYPE']
        abcd1=Cascade+"_"+band
        #abcd1= 'CQ'
        #print(type(Cascade),type(band),abcd1)
        p = Path('C:/Ericsson/CQ/')
        final_file.columns = final_file.columns.str.replace(' ', '')
        fun3(final_file)
#        final_file.to_csv(Path(p,abcd1+'.csv'), index = False)

        #final_file.to_csv(r'C:\Ericsson\CQ\'+abcd+'.csv',index=False)


    except KeyError:
        print("Failed to Print")

# 800 FDD ............................................................>

def fun1(file_Path,con,band):
    print('inside of 800')
    file1_new = pd.read_excel(file_Path, 'eUtran Parameters')
    #print(file1['Band'],file1['Band'][:1].__contains__('1900'))
    #if file1['Band'].__contains__('1900'):
    file_eNB_info = pd.read_excel(file_Path, 'eNB Info')
    #sector_length= file_eNB_info['numberOfSectors_per_DUL']
    #print(file_eNB_info['numberOfSectors_per_DUL'])
    sector_length800=file_eNB_info.loc[1,'numberOfSectors_per_DUL']
    carrier_length800 = file_eNB_info.loc[1, 'No_of_Carriers']
    sector_length1900 = file_eNB_info.loc[0, 'numberOfSectors_per_DUL']
    carrier_length1900 = file_eNB_info.loc[0, 'No_of_Carriers']
    print(sector_length1900,carrier_length1900)
    l1=int(carrier_length800)
    l=int(sector_length800)

    lc1900 = int(carrier_length1900)
    ls1900 = int(sector_length1900)
    lsc= lc1900*ls1900
    print('length800=',l,'carrier_length800=',l1,lsc)
    file1= file1_new.tail(l*l1)
    print(file1)
    #print("sat")
    #print("Converting '{}'")
    list1=['Ericsson','Ericsson','Ericsson']
    list1=list1[:l]
    #Beamwidth=[None]*3
    Beamwidth=['65','65','65']
    Beamwidth=Beamwidth[:l]
    config=[con,con,con]
    config=config[:l]
    channel_type=['1','1','1']
    channel_type=channel_type[:l]
    list5=pd.datetime.today().strftime("%m/%d/%Y");
    list6=[list5,list5,list5]
    list6=list6[:l]
    Sector_id= [None]*3
    Switch_Name=[None]*3
    Market_Name=[None]*3
    #Cascade=[None]*3
    Cluster_Name=[None]*3
    lst=list
    n=l
    j=0;
    for i in range(n):
       j=j+1
       #list7.append(j)
       Sector_id.insert(i,j)
    Sector_id=Sector_id[:l]
    print(Sector_id)

    #print(final_list,list6)
    #list_fixeValues=pd.DataFrame({})
    try:
        #file1= pd.read_excel(file_Path,'eUtran Parameters')
        print('hi')
        Market_Name.insert(0,file1_new.loc[0,'Market'])
        Cascade =file1_new.loc[0,'Cascade_ID']
        Market_Name=Market_Name[:l]
        print(Market_Name)
        Switch_Name.insert(0,'LTE_'+file1_new.loc[0,'Market']+'_SWITCH')
        Switch_Name=Switch_Name[:l]
        print(Switch_Name)
        sector_id_file=pd.DataFrame(np.column_stack([Sector_id]), columns=['SECTORID'])
        Beamwidth_file =pd.DataFrame(np.column_stack([Beamwidth]), columns=['BEAMWIDTH'])

        #sector_id_file = pd.DataFrame(np.column_stack([sector_id]), columns=['SECTORID'])
        final_list6 = pd.DataFrame(np.column_stack([config, channel_type]),
                                   columns=['CONFIG', 'CHANNEL_TYPE'])
        final_list1 = pd.DataFrame(np.column_stack([list6, list1,Market_Name, Switch_Name]),
                                  columns=['DATE', 'VENDORNAME','MARKET_NAME','Switch_Name'])

        final_list1=final_list1.fillna(method='ffill').head()
        print('Final_List1=',final_list1)
        #print(final_list1[['Switch_Name','MARKET_NAME']])

        file2= pd.read_excel(file_Path,'PCI')
        #print(file1[['Market','Cascade_ID','eNBId','latitude','longitude','beamDirection','earfcn']])
        #final_list2 = [None] * 3
        final_list2=file1_new[['Cascade_ID','eNBId']]
        #final_list2 = pd.DataFrame(np.column_stack([Cascade_ID,eNBId]),
                                 #  columns=['CASCADE', 'ENODEBID'])
        #final_list21 = [None]* 3
        final_list2= final_list2[l:lsc+l]

        #final_list21=final_list21.fillna(method='bfill').head()
        #final_list2= final_list2[0:l]
        #final_list21.fillna(method='ffill').head()
        #extra=final_list2.loc[3,'Cascade_ID']
        #final_list2.reset_index()
        final_list2.index = [0,1, 2]
        print('Final_List2=',final_list2)
        #print('Final_List2=',final_list2,final_list2.loc[0,'Cascade_ID'],final_list2.loc[0,'eNBId']])
        final_list3 = file1_new[['latitude','longitude','beamDirection']]
        #final_list3 = pd.DataFrame(np.column_stack([latitude,longitude,beamDirection]),
                            #       columns=['LATITUDE', 'LONGITUDE','AZIMUTH'])
        final_list3 = final_list3[0:l]
        print('Final_List3=', final_list3)
        if con.__eq__('20'):
           final_list5 = file1_new[['earfcn', 'Band']]
           #final_list3 = pd.DataFrame(np.column_stack([earfcn, Band]),
                                   #columns=['CHANNEL_NUMBER', 'BAND_CLASS'])
           final_list5 = final_list5[lsc:lsc+l]
           final_list5.index = [0, 1, 2]
           print('Final_List5=', final_list5)
        else:
            final_list5 = file1_new[['earfcnDl', 'Band']]
            # final_list3 = pd.DataFrame(np.column_stack([earfcn, Band]),
            # columns=['CHANNEL_NUMBER', 'BAND_CLASS'])
            final_list5 = final_list5[lsc:l+lsc]
            final_list5.index = [0, 1, 2]
            print('Final_List5=', final_list5)

        #print(file1_new)
        pci= file2['PCI']
        pci=pci[0:l]
        pci_file = pd.DataFrame(np.column_stack([pci]), columns=['SECTOR_IDENTIFIER'])
        cluster_file = pd.DataFrame(np.column_stack([Cluster_Name]), columns=['CLUSTER_NAME'])
        final_file= pd.concat([final_list1,final_list2,sector_id_file,final_list3,Beamwidth_file,pci_file,cluster_file,final_list5,final_list6], axis=1)
        final_file.columns=['DATE','VENDORNAME','MARKET_NAME','SWITCH_NAME','CASCADE','ENODEBID','SECTORID','LATITUDE','LONGITUDE','AZIMUTH','BEAMWIDTH','SECTOR_IDENTIFIER','CLUSTER_NAME','CHANNEL_NUMBER','BAND_CLASS','CONFIG','CHANNEL_TYPE']
        abcd1 = Cascade + "_" + band
        #abcd1 = 'CQ'
        p = Path('C:/Ericsson/CQ/')
#        final_file.to_csv(Path(p,abcd1+'.csv'), index = False)
        fun3(final_file)
        #final_file.columns = final_file.columns.str.replace(' ', '')
        #final_file.dropna()
        #final_file.dropna(subset=['CASCADE','ENODEBID','CHANNEL_NUMBER','BAND_CLASS'], inplace=True)
        #final_file.to_csv(r'C:\Ericsson\CQ\'+abcd+'.csv',index=False)


    except KeyError:
        print("Failed to Print")



def fun4():

    time = str(datetime.datetime.now())
    time = re.sub('\W+', '-', time)
    print(time, list_)
    abcd1 = 'CQ' + ' ' + time
    frame = pd.concat(list_, axis=0, ignore_index=True)
    frame.columns = frame.columns.str.replace(' ', '')
    p = Path('C:/Ericsson/CQ/')
    frame2 = frame.apply(lambda x: pd.Series(x.dropna().values))
    frame2.to_csv(Path(p, abcd1 + '.csv'), index=False)


def fun2():
    print("i am in fun2")
    #path = r'C:\Ericsson\CQ\CIQ_to_CQ' # use your path
    #allFiles = glob.glob(path + "/*.csv")
#    INPATH = filedialog.askdirectory()
#    allFiles = glob.glob(INPATH + "/*", recursive=True)
    allFiles = glob.glob('C:\Ericsson\CQ\*.csv')
    list_ = []

    for file_ in allFiles:
        #print(file_)
        df = pd.read_csv(file_, index_col=None, header=0)
        list_.append(df)


    time= str(datetime.datetime.now())
    time = re.sub('\W+', '-', time)
    print(time,list_)
    abcd1='CQ'+' '+time
    frame = pd.concat(list_, axis=0, ignore_index=True)
    frame.columns = frame.columns.str.replace(' ', '')
    #frame = frame[np.isfinite(frame['EPS'])]
    p = Path('C:/Ericsson/CQ/')
    frame2 = frame.apply(lambda x: pd.Series(x.dropna().values))
    frame2.to_csv(Path(p, abcd1 + '.csv'), index=False)
    #file1 = frame.apply(lambda x: pd.Series(x.dropna().values))
    #file1

def Gui():
    results=[None]*1

    INPATH = filedialog.askdirectory()
    excel_files = glob.glob(INPATH + "/*", recursive=True)
#    excel_files=glob.glob('C:\Ericsson\CQ\CIQ_to_CQ\*.xlsx')
    #file_Path=(r'C:\Ericsson\CQ\CIQ_to_CQ\Complete AT03EN001 ERC 2.5 TDD 2018_06_27_13_47_11.xlsx.xlsx')
    for file1 in excel_files:
        results = os.path.basename(file1)
        print("Result=", results, results.__contains__("800 FDD"),results.__ne__('800 FDD'))
        flag=0
        for item in results.split(' '):
            if(item.__eq__('1900')):
                flag=1
        print(flag)
        if results.__contains__("2.5 TDD"):
            con='20'
            fun(file1,con,'2500')
        elif (results.__contains__("800 FDD") & flag==0):
            print('i am inside of 800 FDD')
            con='5'
            fun(file1, con, '800')

        else:
            print("inside of 1900 FDD, 800 FDD")
            con = '5'
            fun(file1, con, '1900')
            fun1(file1, con, '800')
    fun4()
button = tk.Button(r, text='Generate', fg="blue",width=35, command=Gui)
button.pack()
frame= Frame(r,width=35, height=50)
frame.pack()
r.mainloop()