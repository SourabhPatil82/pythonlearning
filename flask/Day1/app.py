from datetime import datetime
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy#ORM tool
app = Flask(__name__)#to initialize app
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydatabase.db"
app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)


#To define database skima
class Todo(db.Model):
    SrNo=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SrNo} - {self.title}"


@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':#import req and use it to trace post req from form
       
       #taken info from index.html
       title1=request.form['title']#to get info from the from with name=title
       desc2=request.form['desc']
       print(request.form['title'])
       print(request.form['desc'])

       todo=Todo(title=title1,desc=desc2)
       db.session.add(todo)
       db.session.commit()

    allTodo=Todo.query.all()
    print(allTodo)  #__repr__ funct  #to render the index.html we used render_template with return
    return render_template("index.html",allTodo=allTodo) #jinja2 is templating engine extension
  #passing the vaiable and accessing in index.html using jinja template


@app.route('/show')
def product():
    allTodo=Todo.query.all()
    print(allTodo)
    return 'This is product page!'



@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(SrNo=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=="POST":
     title1=request.form['title']
     desc2=request.form['desc']
     todo=Todo.query.filter_by(SrNo=sno).first()
     todo.title=title1
     todo.desc=desc2
     db.session.add(todo)
     db.session.commit()
     return redirect("/")


    todo=Todo.query.filter_by(SrNo=sno).first()
    return render_template("update.html",todo=todo)

if __name__=="__main__":              #To run the app
    app.run(debug=True, port=8000)