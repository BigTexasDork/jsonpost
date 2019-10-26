# jsonpost
### installation
1. git clone
1. python -m venv venv
1. source venv/bin/activate
1. pip install -r requirements.txt
1. python app.py

## curl
curl \
 -d "@data.json" \
 -H "Content-Type: application/json" \
 -X POST http://localhost:5000/firings
