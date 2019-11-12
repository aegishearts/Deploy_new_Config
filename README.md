# One click configuration deployment
Deploy new configuration to all managed device by one click.
This automation script is temporary solution before Ansible migration.

[Purpose]
 - Change configuration by one time : Reduce human resources

[Function]
 - Script read pre-configuration from .txt file that defined by engineer for each vendor.
 - Script login automatically via SSH and apply pre-configuration, then save permenantly.
 - After running script, result file is created
    - SSH connection fail list : Need to make a change by ourselves
    - Configuration change success list
 - Collect current configuration and parshing data for each parts of configuration
    - Syslog configuration
    *** Keep to update new function (TACACS+, SNMP, ACL,....so on)
 
    
[Manual]
 - how to run script and input option 

        Run.py [Device Type]              # Deploy pre-configuration to target 
            [Device Type]   : Select Switch/Router type
                              - All : all device is managed by network team
                              - BB1~3 : backbone router that hostname include "bb1","bb2","bb3" string
                              - ACC1~5 : access switch that hostname include "acc1~5" string
                              - rmc1~3 : remote switch(IPMI) that hostname include "rmc1~3" string
                              - ETC : other switches except upper case
            *** Why seperate many type option
                To run script for each type and make multiple SSH session at once. It will reduce working time.
                Because, "All" type take over a day to deploy config over 3000 devices with one SSH session. 
                 
            1) Create .txt file include pre-configuration for each vendor
            2) Execute Run.py script with Device Type
            3) Read result file and check which device is failed to change configuration
            4) Login via SSH and change configuration manually for fail list
        
        Verify.py [Device Type] [Configuration Type]        # Verify configuration change
            [Device Type]   : Select Switch/Router type
            [Configuration Type]    : Select parts of configuration
                                        - Syslog    : Check syslog IP, source IP, facility level
            
[Requirement]
 - Python Version higher than 3.0
 - Running_Script repository
 
[Supported Vendor]
 - Juniper EX/QFX/MX series with JUNOS
 - Cisco Catalyst series with IOS
 - Cisco Nexus series with NXOS
 - Arista with EOS
 - Ubiquoss
 - Huawei
 - Foundry & Broucade
 - Dell
 - Ruijie
