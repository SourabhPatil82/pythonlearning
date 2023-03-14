from flask import Flask, jsonify, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import mysql.connector as sql_db 
app = Flask(__name__)
app.secret_key = "djfljdfljfnkjsfhjfshjkfjfjfhjdhfdjhdfu"

userpass = "mysql+pymysql://root:8282@"
basedir = "127.0.0.1"
dbname = "/flask_rel"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8282'
app.config['MYSQL_DB'] = 'flask_rel'


db = SQLAlchemy(app)
app.app_context().push()
mysql = MySQL(app)

#one to many relationship

class Owner(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(100))
    pets=db.relationship("Pet",backref="owner")#pet is child ,putting new col in child
    
    def __init__(self,name, address):
        self.name = name
        self.address = address

class Pet(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    age=db.Column(db.Integer)
    owner_id=db.Column(db.Integer,db.ForeignKey("owner.id"))
    
    def __init__(self,name, age,owner_id):
        self.name = name
        self.age = age
        self.owner_id=owner_id






#one to one relationship
class Parent(db.Model):
    id = db.Column (db. Integer, primary_key=True)
    name=db.Column(db.String(500))
    child = db.relationship('Child', backref='parent', uselist=False)
class Child(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(500))
    parent_id = db.Column (db.Integer, db.ForeignKey('parent.id'))


@app.route('/getowner')
def index():
    users = Owner.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.id
        user_data['name'] = user.name
        user_data['password'] = user.address
        output.append(user_data)

  
    return jsonify({'user' : user_data})


@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
         data = request.get_json()
         
         name = data['name'],
         address =data['address'],
         
         add_data = Owner(name, address)
         
         db.session.add(add_data)
         db.session.commit()
         return jsonify({"key":"success"})

@app.route('/inputpet', methods=['GET', 'POST'])
def input_data1():
    try:
     if request.method == 'POST':
         data = request.get_json()
         
         name = data['name'],
         age =data['age'],
         owner=data['owner']

         add_data = Pet(name,age,owner)
         
         db.session.add(add_data)
         db.session.commit()

         return jsonify({"key":"success"})  
    
    except:
          db.session.rollback()

@app.route('/inputcustom', methods=['GET'])
def input_data2():
     
    cursor = mysql.connection.cursor()
    cursor.execute("select name from pet")
    #data = cursor.fetchall()
    data=cursor.fetchmany(size=1)
    cursor.close()
    return jsonify(data)
#https://forums.mysql.com/read.php?50,685798,685798
#https://linuxhint.com/cursor-execute-python/
#https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

#Path variables

@app.route('/fetch/<int:id>',methods=['GET'])
def edit_data(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM pet WHERE id='%s'", (id,))
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)
    




#pip install mysql-connector-python

#Insert query 

@app.route('/insert', methods=['GET'])
def inpconnut_data3():
     conn = sql_db.connect(
            host="localhost",
            user="root",
            password="8282",
            database="flask_rel",auth_plugin='mysql_native_password'
                    )

     mycursor = conn.cursor()
     query = 'INSERT INTO pet (name,age,owner_id) VALUES (%s, %s, %s)'
     val = ("ox",10,1)
     mycursor.execute(query,val)
     conn.commit()
     conn.close()
     return jsonify({"msg":mycursor.rowcount})

@app.route('/join')
def join ():
    # perform an inner join on two tables
    cur = mysql.connection.cursor()

    #JOIN
    #cur.execute("SELECT * FROM owner INNER JOIN pet ON owner.id = pet.owner_id")
    
    #LEFT OUTER JOIN
    #cur.execute("SELECT owner.name, pet.name FROM owner LEFT JOIN pet ON owner.id = pet.owner_id")
    
    #GROUP BY
    #cur.execute("SELECT name, COUNT(*) FROM pet GROUP BY name")
    
    #ORDER BY
    #cur.execute("SELECT name, age FROM pet ORDER BY name")
    
    #ORDER BY DESC
    #cur.execute("SELECT name, age FROM pet ORDER BY name DESC")

    #LIMIT
    cur.execute("SELECT name, age FROM pet LIMIT 2")
    
    
    results = cur.fetchall()
    cur.close()
    return jsonify(results)    
# mycursor = conn.cursor()

# EXECUTE THE QUERY WITH THEIR RECORD VALUE



# query = 'INSERT INTO MOVIE (id, name, year) VALUES (%s, %s, %s)'
# val = [(2, "Kung Fu panda", 2014),
#        (4, "Frozen", 2014),
#        (5, "Frozen2", 2020),
#        (6, "Iron Man", 2013)

#        ]

# mycursor.executemany(query,val)




    


if __name__ == '__main__':
  app.run(debug=True)