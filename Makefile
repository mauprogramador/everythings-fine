-include .env
.PHONY: $(MAKECMDGOALS)


setup:
	@bash setup.sh

run:
	@python3 -m src
