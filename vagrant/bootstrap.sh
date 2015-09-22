sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password password'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password password'
sudo apt-get update
sudo apt-get install -y mysql-server
sudo apt-get install -y build-essential python-dev libmysqlclient-dev

sudo apt-get install -y python-setuptools
sudo apt-get install -y python-pip
sudo apt-get install -y python-virtualenv

mysql -uroot -ppassword < /vagrant/schema.sql