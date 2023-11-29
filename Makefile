ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
MAIN_FILE:=$(ROOT_DIR)/main.py
PYTHON_RUN:=pipenv run --quiet python $(MAIN_FILE) 

aws-show-roles:
	@$(PYTHON_RUN) aws-show-roles

aws-show-profiles:
	@$(PYTHON_RUN) aws-show-profiles

aws-show-regions:
	@$(PYTHON_RUN) aws-show-regions

aws-select-role:
	@$(PYTHON_RUN) aws-select-role

aws-login:
	@$(PYTHON_RUN) aws-login

kube-pods:
	@$(PYTHON_RUN) kube-pods

kube-switch-context:
	@$(PYTHON_RUN) kube-switch-context

kube-show-contexts:
	@$(PYTHON_RUN) kube-show-contexts

