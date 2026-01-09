# -----------------------------------LOGGING----------------------------

#Logging: Its widely use instead of just using print() because it gives you levels, formatting, file writing and better control 
 
    #  DEBUG   --> Detailed info (fro debugging) #10 
    #  INFO    --> Confirmation that things are working as expected #20 
    #  WARNING --> Something unexpected happened, but program still works #30 
    #  ERROR   --> More serious issue program might not work corretly # 40 
    #  CRITICAL --> Very serious error, program may not continue #50 
  
# logging.basicConfig(
#     filename="app.log",
#     level="logging.INFO",
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

#filename 
# lineno
# filename 
# message 

# print is temporary when console is there upto to that only 
# logging is permanent(persisstent) 

# logs --we give file name it create file and  store the logs in that file 
# print- statements are upto that console only ok 

#  HOW to implement Logging  
# ---------------------------- 
# we have to store  

# logging.basicConfig(filename='log.txt',level=logging.WARNING)  #---syntax 

# logging.debug(message) 
# logging.info(message) 
# logging.warning(message) 
# logging.error(message) 
# logging.critical(message)  

# import logging  
# # logging.basicConfig(level=logging.WARNING) # here lower than warnings it ignores it  automatically  
# # logging.basicConfig(level=logging.INFO) 
# # logging.basicConfig(level=logging.DEBUG)  # here we did not give anything but it takes by default 'from warning,info,debug')
# logging.basicConfig()
# logging.basicConfig(level=30) # we can mention sizes also  ok 

# logging.debug('debug') 
# logging.info('info') 
# logging.warning('warning') 
# logging.error('error') 
# logging.critical('critical')  

# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical 

import logging
logging.basicConfig(filename='app.logs',  # file 'app.logs' will create in vscode and store logs in that file ok 
                    
                    #level=logging.INFO   
                    format = '%(asctime)s -%(levelname)s -%(message)s'

                    )
logging.debug('debug') 
logging.info('info') 
logging.warning('warning') 
logging.error('error') 
logging.critical('critical')  
logging.critical('critical added')  
