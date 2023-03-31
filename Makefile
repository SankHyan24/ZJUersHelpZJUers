.PHONY: debug run
# Debug Mode
# The server will be restarted on code changes and will provide a debugger shell on errors.
# Never use a debugger in a production environment!
debug:
	@echo "[Debug Mode]: Run Flask Server on port 5000"
	@export FLASK_ENV=development; \
	export FLASK_DEBUG=1; \
	export FLASK_APP=flaskr; \
	flask run --host=0.0.0.0 --port=5000

# Run Mode
run:
	@echo "Run Flask Server on port 5000"
	@export FLASK_DEBUG=0; \
	export FLASK_APP=flaskr; \
	flask run --host=0.0.0.0 --port=5000