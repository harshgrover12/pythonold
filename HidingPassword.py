import os
'''
For linux:
Edit .bash_profile file and add below
export DB_USER="test"
export DB_PASS="novell123"
'''
db_user = os.environ.get('DB_USER')
db_pwd = os.environ.get('DB_PASS')
print(db_user)  # This will return the value set at environment variable
print(db_pwd)
