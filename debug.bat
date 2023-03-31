@echo "[Debug Mode]: Run Flask Server on port 5000"
@set FLASK_ENV=development
set FLASK_DEBUG=1
set FLASK_APP=flaskr
flask run --host=0.0.0.0 --port=5000