ci: deps lint test

define python_venv
	. .venv/bin/activate && $(1)
endef

deps:
	python3 -m venv .venv
	$(call python_venv,python3 -m pip install -r requirements.txt)

lint:
	$(call python_venv,molecule lint)

test:
	$(call python_venv,molecule test)

.PHONY: ci deps lint test
