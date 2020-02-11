# COCKROACH BOILERPLATE WITH JWT PROJECT


## Environment File
move env.local to .env see example value
``` bash
APP_NAME = Cockroach Boilerplate
APP_HOST = 127.0.0.1
APP_PORT = 5000
SECRET_KEY = YOUR SECRET

MEMCACHE_HOST=127.0.0.1
MEMCACHE_PORT=11211

FLASK_DEBUG = True

JWT_SECRET_KEY = YOUR SECRET

SWAGGER_URL = '/api/docs'
SWAGGER_API_URL = 'http://petstore.swagger.io/v2/swagger.json'
```

## Local Development

Installing Requirements
``` bash
pip install -r requirements.txt
```

run server
``` bash
python manage.py server
```


## With Virtualenv

Installing virtualenv firts

```
virtualenv -p python3 env
```
Activate virtualenv
```
# in linux or mac
source env/bin/activate

# in Windows
\env\Scripts\activate.bat
```
Installing Requirements
``` bash
pip install -r requirements.txt
```

run server
``` bash
python manage.py server
```
