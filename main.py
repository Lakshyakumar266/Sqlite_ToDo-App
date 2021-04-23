from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    msg = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"{sno} - {name} - {msg}"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form['name']
        msg = request.form['msg']

        Data = User(name=name, msg=msg)
        db.session.add(Data)
        db.session.commit()
    
    listusr = User.query.filter_by().all()
    return render_template('index.html', listusr=listusr)

@app.route('/delete/<int:sno>')
def delete(sno):
    deletedata = User.query.filter_by(sno=sno).first()
    db.session.delete(deletedata)
    db.session.commit()
    return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)
