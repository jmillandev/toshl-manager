dev:
	./init.sh run --rm finance-manage

show:
	python application.py roomie:expenses:show --from=01/02/25 --to=01/03/25
	python application.py roomie:loans:show --from=01/02/25 --to=01/03/25

clean:
	python application.py roomie:expenses:clean --from=01/02/25 --to=01/03/25
	python application.py roomie:loans:clean --from=01/02/25 --to=01/03/25

budgets:
	python application.py buggets:show
