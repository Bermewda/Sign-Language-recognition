import os
#-----------------------------  open import ---------------------------------------

#----------------------------- close import ---------------------------------------
path='C:/Users/BEAMCONAN/project_finger/Dataset'
for fname in os.listdir(path):
    print(fname,end=' ')
    paths=path+'/'+str(fname)
    for iname in os.listdir(paths):
       # print(iname,end=' ')
        pathss=paths+'/'+str(iname)
        img=imread(pathss)
        #--------------------------------------- open my code-------------------------------------------------------------

        #---------------------------------------close my code-------------------------------------------------------------
    print("****************************************************************")
