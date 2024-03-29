import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Running_Script import Query_DB as DB
from Running_Script import Run_Command as RC

#### Ver1.0 ####

########################################################
CFG_file = {
        'cisco-nx':'/XXXXXX/NXOS.txt',
        'cisco':'/XXXXXX/IOS.txt',
        'ubiquoss':'/XXXXXX/UBI.txt',
        'huawei':'/XXXXXX/HUAWEI.txt',
        'juniper':'/XXXXXX/JUNOS.txt',
        'foundry':'/XXXXXX/FOUNDRY.txt',
        'brocade_fabric':'/XXXXXX/BROCADE.txt',
        'dell':'/XXXXXX/DELL.txt',
        'arista':'/XXXXXX/EOS.txt',
        'ruijie':'/XXXXXX/RUIJIE.txt',
}
Result_DIC = '/XXXXXX/Results_DIR/'
########################################################

if __name__ == "__main__":
	Value = sys.argv[1]
	Fail_List = []
	Fail_File = open(Result_DIC+'FailList.txt','a')
	Success_File = open(Result_DIC+'SuccessList.txt','a')
    if Value == 'ALL' or Value =='BB1' or Value =='BB2' or Value =='BB3' or Value =='ACC1' or Value =='ACC2' or Value =='ACC3' or Value =='ACC4' or Value =='ACC5' or Value =='AGG' or Value =='RMC1' or Value =='RMC2' or Value =='RMC3' or Value =='ETC':
		Host_List = DB.Search_Device_by_Type(Value)
		print(Host_List)
		for i in Host_List:
			print(i)
       		Vendor,POP = DB.Search_Host_NIDB(i)
			CFG = CFG_file[Vendor]
			Check = RC.Apply_Config(i,Vendor,CFG)
			if Check:
            	Success_File.write(i+'\n')
			else:
            	Fail_File.write(i+'\n')
	else:
        print('host configuration mode: '+Value+'\n')
       	Vendor,POP = DB.Search_Host_NIDB(Value)
		CFG = CFG_file[Vendor]
		RC.Apply_Config(Value,Vendor,CFG)
