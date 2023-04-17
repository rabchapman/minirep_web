# MiniRep-Web
ISP452 Web Server for Minirep Feed

# Prerequisite Steps
1. Make an exception for port 5000 with firewalld: `sudo firewall-cmd --permanent --zone=public --add-port=5000/tcp` OR `sudo ufw allow 5000/tcp`

2. Install venv: `sudo apt install python3.8-venv`


Note that this is not recommended for production environments. This will be for testing purposes only.

# Installation (Linux)
1. Install python3-virtualenv (this is dependent on the OS you are running): `sudo apt install python3.10-venv`
2. Clone the repository: `git clone https://github.com/rabchapman/minirep_web.git`
3. Change directories into the repository folder: `cd minirep-web`
4. Create the virtual environment: `python -m venv .`
5. Activate the virtual environment: `source ./bin/activate`
6. Install the required packages: `pip3 install -r requirements.txt`
7. Run the flask application: `flask run`

# Verify
Open a browser and browse to the the http://server3/block/ips. You should receive as response with the data below:

`{"169.0.0.1":{"count":1,"date":"10/1/2019 8:57 PM"}}`

