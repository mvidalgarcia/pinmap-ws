# pinmap-ws
RESTful API for [Pinmap](https://github.com/mvidalgarcia/pinmap) Android app.

##  REST API

The following table represents all the endpoints of the current Pinmap REST API.  

| Method | URI             | Description                     |
|--------|-----------------|---------------------------------|
| GET    | /pins/[user_id] | Gets all the existing user pins |
| GET    | /pin/[pin_id]   | Gets user existing pin          |
| POST   | /pin            | Creates new user pin            |
| DELETE | /pin/[pin_id]   | Removes existing user pin       |

##  Install

This RESTful web service was tested under Python 3.4.0

Install Python 3 tools:

* Ubuntu:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install python3 python3-pip
sudo pip3 install virtualenv
```

* Mac OS X ([brew](http://brew.sh) required):
```bash
sudo brew update
brew install python3
sudo pip3 install virtualenv
```

Clone repository:

```bash
git clone https://github.com/mvidalgarcia/pinmap-ws.git
cd pinmap-ws
```

Create virtual environment:

```bash
virtualenv venv
```

Activate virtual environment:

```bash
. venv/bin/activate
```

Install dependencies:

```bash
pip3 install -r dependencies
```

Deactivate virtual environment:

```bash
deactivate
```


## Run

Activate virtual environment:

```bash
. venv/bin/activate
```

Run server:
```bash
python3 run.py
```

Deactivate virtual environment:
```bash
deactivate
```

Note that virtual environment must be activated in order to run the server.
  
I recommend using `screen` in order to launch python files and leave them running.
More information about `screen` in Unix environments [here](https://kb.iu.edu/d/acuy). 
