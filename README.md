# how to start this app



## 1. install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2. setup env
Download `env` from Discord and paste the file in the root directory.
Change the name to `.env`

## 3. setup database
```
python3 manage.py migrate
```

## 4. run server
```
python3 manage.py runserver
```