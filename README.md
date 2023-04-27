# MiniRep-Web
ISP452 Web Server for Minirep Feed

# Prerequisite Steps
1. Make an exception for port 5000 with firewalld: `sudo firewall-cmd --permanent --zone=public --add-port=5000/tcp` OR `sudo ufw allow 5000/tcp`

2. Install venv: `sudo apt install python3.8-venv`


Note that this is not recommended for production environments. This will be for testing purposes only.

# Installation (Linux)
1. Clone the repository: `git clone https://github.com/rabchapman/minirep_web.git`
2. Change directories into the repository folder: `cd minirep-web`
3. Create the virtual environment: `python -m venv .`
4. Activate the virtual environment: `source ./bin/activate`
5. Install the required packages: `pip3 install -r requirements.txt`
6. Run the flask application: `flask run --host=0.0.0.0`

# Verify
Open a browser and browse to the following URL http://server3:5000/block/ips. You should receive as response with the data below:

`{"169.0.0.1":{"count":1,"date":"10/1/2019 8:57 PM"}}`

