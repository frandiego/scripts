ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
MAIN_FILE:=$(ROOT_DIR)/main.py
PYTHON_RUN:=pipenv run --quiet python $(MAIN_FILE) 

aws-show-profiles:
	@$(PYTHON_RUN) aws-show-profiles

aws-login:	
	@$(PYTHON_RUN) aws-login
