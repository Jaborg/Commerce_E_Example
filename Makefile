setup:
	 python3.11 -m venv env
	 env/bin/python3.11 -m pip install --upgrade pip
	 env/bin/pip3.11 install -r requirement.txt


clean_env:
	rm -r env

containers:
	docker-compose up -d

down:
	docker-compose down

produce-to-kafka:
	env/bin/python -m utils.cli_parser --command produce

consume_from-kafka:
	env/bin/python -m utils.cli_parser --command consume