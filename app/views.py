from app import app

@app.route('/')
def home():
   return "hello app h"
