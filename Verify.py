import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from Running_Script import Query_DB as DB
from Running_Script import Run_Command as RC
from Running_Script import Check_config as CFG

#### Ver1.0 ####

########################################################
Result_File = '/data/NETOPS/AllinOne_Config/Results_DIR/'
########################################################

def Check_Syslog_Config(Device_Type, Config_Type, File):
	F.write('Hostname,Vendor,Source,IP#1,Facility#1,IP#2,Facility#2,IP#3,Facility#3,IP#4,Facility#4\n')
	Host_List = DB.Search_Device_by_Type(Device_Type)
	print(Host_List)
        for i in Host_List:
        	Vendor,POP = DB.Search_Host_NIDB(i)
		Syslog_DIC, SRC = CFG.Find_Syslog_Config(i,Vendor)
		List = []
		for j in Syslog_DIC.keys():
			List.append(j)
			List.append(Syslog_DIC[j])
		Line = ','.join(List)
		F.write(i+','+Vendor+','+SRC+','+Line+'\n')
	F.close()

if __name__ == "__main__":
	Device_Type = sys.argv[1]
	Config_Type = sys.argv[2]
        if Device_Type == 'ALL' or Device_Type =='BB1' or Device_Type =='BB2' or Device_Type =='BB3' or Device_Type =='ACC1' or Device_Type =='ACC2' or Device_Type =='ACC3' or Device_Type =='ACC4' or Device_Type =='ACC5' or Device_Type =='AGG' or Device_Type =='RMC1' or Device_Type =='RMC2' or Device_Type =='RMC3' or Device_Type =='ETC':
		F = open(Result_File+Device_Type+'_'+Type+'.csv','w')
		if Config_Type == 'Syslog':
			Check_Syslog_Config(Device_Type, Config_Type, F
		else:
			print('##### Need to define new function for this type of config #####')
