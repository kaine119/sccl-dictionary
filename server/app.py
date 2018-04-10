from flask import Flask, redirect, render_template, request, url_for, session, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key = 'any random string'


# local ???
SQLALCHEMY_DATABASE_URI = "sqlite:///sccl/test.db"

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

'''
Models for db
'''
class Dictionary(db.Model):
    '''
    the definition etc. table
    data shld be provided by SCCL
    '''

    __tablename__ = "dictionary"

    id = db.Column(db.Integer, primary_key=True)

    word = db.Column(db.Text())

    definitionXianHanId = db.Column(db.Text(1000))
    definitionUser = db.Column(db.Text(400))

    # some more columns not used yet

    POS = db.Column(db.Text())
    pinYin = db.Column(db.Text())

    pinYinNumber = db.Column(db.Integer)
    yuYiId = db.Column(db.Integer)
    sentenceId = db.Column(db.Integer)

    paragraphIdx = db.Column(db.Integer)
    sentenceIdx = db.Column(db.Integer)
    source = db.Column(db.Text())
    filePath = db.Column(db.Text())

    word_level =  db.Column(db.Text())	# represent grade, stream, & lesson
    abnormal = db.Column(db.Text())
    abnormalRemarks = db.Column(db.Text())
    isXianHan = db.Column(db.Integer) # boolean

    example = db.Column(db.Text())
    imagePath = db.Column(db.Text())
    videoPath = db.Column(db.Text())

db.create_all()

# search page
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search_PAGE_NAME.html") # page name tbc
    currWord = request.form['word_searched'] # var name 'word_searched' tbc
    session['currWord'] = currWord

    return redirect(url_for('result'))


# search result page
@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "GET":
        # search for all possible words
        currWord = session['currWord']
        likeStr = '%' + currWord + '%'
        words = Dictionary.query.filter(Dictionary.word.like(likeStr)).all()

        return jsonify(words)

    selectWord = request.form['word_selected'] # var name 'word_selected' tbc
    session['selectWord'] = selectWord
    return redirect(url_for('definition'))

# definition of the word selected
@app.route("/definition")
def definition():
	selectWord = session['selectWord']
	return jsonify(selectWord)



