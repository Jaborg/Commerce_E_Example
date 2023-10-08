setup:
	 python3.11 -m venv env
	 env/bin/python3.11 -m pip install --upgrade pip
	 env/bin/pip3.11 install -r requirements.txt


clean_env:
	rm -r env

containers:
	docker-compose up -d

