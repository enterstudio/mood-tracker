#Installation to help dev:

##Step 1:

`git clone git@github.com:lucasmarcelli/mood-tracker.git`

`cd mood_tracker`

##Step 2:

Linux:
`sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev`

`sudo mysql_install_db`

`sudo mysql_secure_installation`


Mac: 
download mysql community server from https://dev.mysql.com/downloads/mysql/
then

`which mysql`

if the above doesn't output anything add: `$PATH=$PATH:/usr/bin/mysql` to your `.bash_profile`
ensure you start the server

##Step 3:
`mysql -u root -p`

`CREATE DATABASE mood CHARACTER SET UTF8;`

`CREATE USER userperson@localhost IDENTIFIED BY 'password';`

`GRANT ALL PRIVILEGES ON mood.* TO userperson@localhost;`

`FLUSH PRIVILEGES;`

`exit`

##Step 4:
`sudo pip install virtualenv`

`virtualenv moodenv`

`source moodenv/bin/activate`

`pip install -r requirements.txt'

##Step 5:
`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

follow the instructions to create superuser

`python manage.py runserver`

go to 127.0.0.1:8000

#Everytime you want to dev you MUST
`virtualenv moodenv`

`source moodenv/bin/activate`

first






