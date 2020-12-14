from app import app

@app.route("/")
@app.route("/index")

def get(): 
    return ({'hello': "world"})