setup:
	 python3.9 -m venv env
	 env/bin/python3.9 -m pip install --upgrade pip
	 env/bin/pip3.9 install -r requirements.txt


clean_env:
	rm -r env

containers:
	docker-compose up -d

stop:
	docker stop $(docker ps -a -q)