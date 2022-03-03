import os
from datetime import datetime

print(dir(os))
print(os.getcwd())  # current working directory, C:\D-Drive\learning\Corey-Schafer
os.chdir('C:\\Users\\GHarsh\\Desktop')
print(os.getcwd())  # C:\Users\GHarsh\Desktop

# listdir returns folder and files in current working directory in the form of list
print(os.listdir())  # ['500_devices.xlsx', 'abc.csv', 'automation-20201222.log', 'AutoPilotHWID.csv', 'DBeaver.lnk', 'desktop.ini', 'failed_devices.xlsx', 'fsquirt.exe', 'gavya.png', 'harsh.txt', 'hdfc_voucher.PNG', 'impersonate.py', 'InFocus.url', 'Internet Explorer.lnk', 'ipc_error_tracker.txt', 'issu1.PNG', 'lips-icon-outline-illustration-vector-260nw-544349605.webp', 'list_with_languages.PNG', 'manageServices.py', 'MDMSync.py', 'Microsoft Teams.lnk', 'mini-pst-plan.xlsx', 'mini-pst-tracker.xlsx', 'mini_pst.txt', 'new', 'New folder1', 'nippon_etf.PNG', 'njwc.jar', 'note.txt', 'OL-2021-10239.pdf', 'oneplus_nord.PNG', 'overall_sync_time.txt', 'policy.xlsx', 'Postman.lnk', 'ppkg_enroll.ppkg', 'ppkg_enroll_logs.txt', 'python.PNG', 'qtns.txt', 'qt_unenroll.PNG', 'Ra_ProfileSwitch_AD_SSL_logging_23_profile.py', 'root_cert.ppkg', 'share', 'ssl.ppkg', 'Statutory Nomination Form - India .pdf', 'surabhi', 'surabhi.zip', 'sync_time.csv', 'sync_time.txt', 'sync_timings.xlsx', 'This PC - Shortcut.lnk', 'thread_dumps', 'thread_dumps.zip', 'timetable.txt', 'TLauncher.lnk', 'voucher.PNG', 'vpn.txt', 'Webex.lnk', 'Windows_MDM_Enroll_PPKG', 'Windows_MDM_Enroll_PPKG.zip', 'wireshark_eth0_20201216165251_uIeftO.pcapng', 'zenagent.py', 'ZenserverMonitor', 'zen_mdm_devicesids.py', 'zip.jpg', 'zmd-messages.log', 'Zoom.lnk']

#mkdir and makedirs, mkdirs help in creating subsdirectory at one go
# os.mkdir('NewFolder')
# os.makedirs('OS-Demo-2\\test')  # creates a directory name OS-Demo-2 and inside test folder

# os.rmdir('OS-Demo-2')  # OSError: [WinError 145] The directory is not empty: 'OS-Demo-2'
# os.removedirs('OS-Demo-2\\test')

# os.rename('abc.csv', 'def.csv')
print(os.listdir())
print(os.stat('def.csv').st_size)  # 13030
print(os.stat('def.csv').st_mtime) # 1606732940.3809738
print(datetime.fromtimestamp(os.stat('def.csv').st_mtime))  # 2020-11-30 16:12:20.380974

for dirpath, dirnames, filenames in os.walk('C:\\D-Drive\\resume'):
    print('Current Path: ', dirpath)
    print('Dir names: ', dirnames)
    print('File names: ', filenames)
    print()
    print(type(dirpath))


# output, it will traverse through each of the folder, subfolders and list files in it
# dirpath-string
# dir names - list
# filenames - list

# Current Path:  C:\D-Drive\resume
# Dir names:  ['November-rsa']
# File names:  ['Harsh_Grover-ol2.pdf', 'Harsh_Grover-old.pdf', 'Harsh_Grover.docx', 'Harsh_Grover.pdf', 'Harsh_Grover1.pdf', 'Harsh_Grover_old.docx', 'Harsh_Grover_old.pdf', 'Harsh_Grover_old4.pdf', 'Harsh_Grover_previous.pdf', 'Harsh_Grover__old3.pdf', '~$rsh_Grover.docx']

# Current Path:  C:\D-Drive\resume\November-rsa
# Dir names:  []
# File names:  ['Harsh_Grover.pdf']

# prints value set for HOME environment variable
print(os.environ.get('HOME'))
print(os.environ.get('PYTHONPATH'))  # C:\D-Drive\learning\Corey-Schafer

file_path = os.path.join(os.environ.get('PYTHONPATH'), 'test.txt')
print(file_path)  # C:\D-Drive\learning\Corey-Schafer\test.txt

print(os.path.basename(file_path))  # test.txt
print(os.path.dirname(file_path))  # C:\D-Drive\learning\Corey-Schafer
print(os.path.split(file_path))  # ('C:\\D-Drive\\learning\\Corey-Schafer', 'test.txt')
print(os.path.exists(file_path))  # False as test.txt isn not present here
print(os.path.isdir(file_path))  # False
print(os.path.splitext(file_path))  # ('C:\\D-Drive\\learning\\Corey-Schafer\\test', '.txt')
print(dir(os.path))
print(os.path.relpath(file_path))
print(os.path.ismount(file_path))
'''
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'_abspath_fallback', '_get_bothseps', '_getfinalpathname', '_getfullpathname', '_getvolumepathname', 'abspath', 
'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 
'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile',
 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 
 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 
 'stat', 'supports_unicode_filenames', 'sys']
'''