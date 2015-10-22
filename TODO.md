### 1.97
1. Core

- [ ] fix invalid date bug
- [ ] speedup alerts
- [ ] add switch
- [ ] raise alert on not reachable only if we have 2 consecutive 
- [ ] Make test for first few times collector return nulls!
- [ ] Tables last online & admin_status do not update when new device is added.
- [ ] When dev is failing, no other data is collected.
- [ ] слишком много данных на графике. надо попроще

- [ ] Визуальный журнал для bx
- [ ] Разблокировку узлов и список заблокированных узлов в веб
- [ ] Автоматизированный режим загрузки узлов по галочке

* #lockproc node1
* #unlockproc node1
- [ ] web interface  + db entity добавление узлов в реш. поле  - автоматом
- [ ] добавление элементов данных /home/bx/bin/pm.2/ -> файл bx_so_add.py имя файла 


2. Web
- [ ] database size cached at start of server
- [ ] tooltip added 
- [ ] add measure of gpu utilization by time in web

3. Clean code:
- [ ] 1 Reconfiguration of bussol parameter groups
- [ ] clean tests
* no need to use mysql
* no need to use snmpd of given machine
* no need to use ipmiget 
* tools like ipmi and snmp must be checked in separate tests
* database for test need to be sqlite with minimum of data

6. Graceful shutdown:
standalone script

### Future:
- [ ] Parameter show icon -> looking glass
- [ ] Setup with rpm
- [ ] Test installation with virtualenv, scripts and rpm on other machine.
- [ ] Add uml diagrams
- [ ] fan status as gif
- [ ] add plot of rack
- [ ] Alert should blink
- [ ] Alert should be on index menu and blink

### Refactoring:
1. delete addressing from config
2. create hostname/ip for device
3. delete duplicate from context

Future work
======
- [ ] User shouldn't be able to start and stop all power from web constantly. Need to
1. add singleton GlobalPowerManger
2. add lock to command to GlobalPowerManger so no one can perform more than one command
3. inform user if lock is active by returnig status code by power_control_action
- [ ] 4 add priority to parameters to sort them in general device
- [ ] 3 Alerts are dynamic
- [ ] 2 404 error page with link to main page
- [ ] 3 delete alert from journal
- [ ] 3 Clear journal from journal
- [ ] Add basic TPO
- [ ] config can be stored in database in json and get by 
- [ ] all 3 managers need to be aggregated into one 

Not tested
====
- [ ] web: power on off, cluster
- [ ] web all json

Complex
====
- [ ] get ntp working
- [ ] full system backups
- [X] organize cables
- [ ] get fc on file server
- [ ] migrate on fileserver with bx

# check suppz
mqinfo &> /dev/null; echo $?

# make fft into bx task

Прикрутить питание к буссоли
