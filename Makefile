-include .env
.PHONY: $(MAKECMDGOALS)


install:
	@pip3 install -r requirements.txt

run:
	@python3 -m src
