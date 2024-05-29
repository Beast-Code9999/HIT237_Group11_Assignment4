# HIT237_Group11_Assignment4

# Admin:  unit_coordinator
# Password: password

# Admin: yakub_unit_coordinator
# Password: yakubpassword

# Supervisors
- Yakub
username: yakub_sebastian
email: yakubgroup11@gmail.com
password: yakub

- Bharanidharan
username: bharanidharan_shanmugam
email: bharanidharangroup11@gmail.com
password: Bharanidharan

- Sami
username: sami_azam
email: samigroup11@gmail.com
password: sami

- Asif
username: asif_karim
email: asifgroup11@gmail.com
password: asif


# Students
- Jason
username: jason_lay
email: jasonlayStudent@gmail.com
password: jasonpassword

- Micia
username: micia_gusmao
email: miciagusmaoStudent@gmail.com
password: miciapassword

NOTE: 

project
|_accounts
|    |_management
|    |    |_command
|    |    |    |_groups.py
|    |    |    |_supervisors.py
|    |    |    |_unit_coordinators.py

- within this command folder contains three python files that handles creating groups, supervisors, and unit_coordinators


NOTE: If any predefined users or groups are deleted, the above files should be run in the terminal once more, in case the data entries are already removed from the database


Comments:
Tried to mirror Project and ProjectChangeRequest for data integrity but seems to be too difficult for current level or takes too much time
Tried to use pip install django-moderation to moderate two django objects (Project and ProjectChangeRequest)
- limitation: Does not support many-to-many relationships