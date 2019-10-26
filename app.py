import logging
import traceback
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/firings', methods=['POST'])
def firings():
   # only checks mime type, not validity
   logging.info(request.is_json)

   try:
      retval = jsonify(request.json)
      return retval
   except:
      return jsonify(exception=traceback.format_exc())
  

if __name__ == '__main__':
    app.run()