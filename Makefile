LOCAL_COMPOSE = docker compose run web
PIP_BIN =  $(LOCAL_COMPOSE) python -m pip
MANAGE_PY =  $(LOCAL_COMPOSE) python manage.py
ARG1 := $(word 2, $(MAKECMDGOALS) )
ARG2 := $(word 3, $(MAKECMDGOALS) )
ARG3 := $(word 4, $(MAKECMDGOALS) )

update:
	@ $(PIP_BIN) install -r requirements/local.txt

createsuperuser:
	@ $(MANAGE_PY) createsuperuser

shell:
	@ $(MANAGE_PY) shell

startapp:
	@ [ -z "$ARG2" ] && $(MANAGE_PY) startapp $(ARG1) --appdir $(ARG2) || $(MANAGE_PY) startapp $(ARG1)


startapi:
	@ [ -z "$ARG2" ] && $(MANAGE_PY) startapi $(ARG1) --appdir $(ARG2) || $(MANAGE_PY) startapi $(ARG1)


checkdb:
	@ [ -z "$ARG1" ] && $(MANAGE_PY) checkdb $(ARG1) || $(MANAGE_PY) checkdb



%:
	@: