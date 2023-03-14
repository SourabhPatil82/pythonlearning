import datetime
from flask import Flask,jsonify,request,make_response
import jwt  # pip install pyjwt
from functools import wraps

app=Flask(__name__)

app.config["SECRET_KEY"]="jdhfkjdhfk"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        #token=request.args.get("token")
        if "x-access-token" in request.headers:
            token=request.headers['x-access-token']

        if not token:
            return jsonify({"message":"Token is missing"}),403
        try:
            data:jwt.decode(token,app.config["SECRET_KEY"])
        except:
            return jsonify({"message":"token is required"}),403
        
        return f(*args,**kwargs)
    return decorated



@app.route("/unprotected")
def unprotected():
    return  jsonify({"message":"accessing unprotected resource"})

#http://localhost:5000/protected?token=
@app.route("/protected")
@token_required
def protected():
    return jsonify({"message":"accessing protected with json token"})

@app.route("/login")
def login():
    auth=request.authorization

    if auth and auth.password=="pswd":

        token=jwt.encode({"user":auth.username,"exp":datetime.datetime.utcnow()+datetime.timedelta(seconds=50)},app.config['SECRET_KEY'])
        return jsonify({'token':token})
       # return jsonify({'token':token.decode('UTF-8')})#beacuse python3 token generated in bytes hence decoding
    return make_response("could not verify",401 ,{"www-authenticate":"Login required"})

if __name__=="__main__":
    app.run(debug=True)
