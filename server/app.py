from flask import Flask, redirect, render_template, request, url_for, session, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import NVARCHAR

app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key = 'any random string'


# local ???
SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

'''
Models for db
'''
class Xianhan(db.Model):
    """
    definition from xianhan
    'xianhan' table
    """

    __tablename__ = "xianhan"

    _id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text)
    POS = db.Column(db.Text)
    pinYin = db.Column(db.Text)
    definition = db.Column(db.Text)
    TRPWordId = db.Column(db.Integer)
    active = db.Column(db.Integer)  # boolean

class Sentences(db.Model):
    """
    example sentences
    'sentences' table
    """

    __tablename__ = "sentences"

    _id = db.Column(db.Integer, primary_key=True)
    previousSentence = db.Column(db.Text)
    senntence = db.Column(db.Text)
    nextSentence = db.Column(db.Text)
    grade = db.Column(db.Integer)
    stream = db.Column(db.Text)
    lesson = db.Column(db.Integer)
    filePath = db.Column(db.Text)
    source = db.Column(db.Text)

class Yuyi(db.Model):
    """
    yuyi (meaning) of words in sentences
    'yuyi' table
    """

    __tablename__ = "yuyi"

    _id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer)
    label = db.Column(db.Text)
    text = db.Column(db.NVARCHAR)
    description = db.Column(db.NVARCHAR)
    _type = db.Column(db.Text)      # POS? tbc
    active = db.Column(db.Integer)  # boolean


class Dictionary(db.Model):
    '''
    the definition etc. table
    'main' table of the provided .xls file for data
    '''

    __tablename__ = "dictionary"

    _id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text())
    POS = db.Column(db.Text())
    pinYin = db.Column(db.Text())
    pinYinNumber = db.Column(db.Integer)    # pinyin with no.

    yuYiId = db.Column(db.Integer)
    sentenceId = db.Column(db.Integer)

    paragraphIdx = db.Column(db.Integer)
    sentenceIdx = db.Column(db.Integer)
    wordIdx = db.Column(db.Integer)
    positionIdx = db.Column(db.Integer)

    source = db.Column(db.Text())       # textbook name
    filePath = db.Column(db.Text())

    word_level =  db.Column(db.Text())  # representing the following 3
    grade = db.Column(db.Integer)
    stream =  db.Column(db.Text())
    lesson = db.Column(db.Integer)
    
    definitionXianHanId = db.Column(db.Integer)
    definitionUser = db.Column(db.Text(400))

    abnormal = db.Column(db.Text()) # boolean
    abnormalRemarks = db.Column(db.Text())

    isXianHan = db.Column(db.Integer) # boolean
    example = db.Column(db.Text())

    imagePath = db.Column(db.Text())
    videoPath = db.Column(db.Text())

    tagStatusLL = db.Column(db.Integer) # boolean
    tagStatusGHH = db.Column(db.Integer) # boolean

db.create_all()
db.session.commit()    

@app.route("/search", methods=["GET", "POST"])
def search():
    '''earch page'''
    
    if request.method == "GET":
        return render_template("search_PAGE_NAME.html") # page name tbc
    word_searched = request.form['word_searched'] # var name 'word_searched' tbc
    url = 'result/<' + word_searched + '>'

    return redirect(url_for(url))


@app.route("/api/result/<searchingword>", methods=["GET"])
def result(searchingword):
    '''search result page'''
    
    # search for all possible words
    likeStr = '%' + searchingword + '%'

    words = Dictionary.query.filter(Dictionary.word.like(likeStr)).all()
    json_object = {"words": words}   # return the entire list of all possible words for json, then for word in words, word._id -> its id, word.word -> the word etc.

    return jsonify(json_object)

# word definition page
@app.route('/api/get-definitions/<id>', methods=["GET"])
def get_definitions(id):
    definition_to_return = Dictionary.query.filter(Dictionary._id==id).first()
    json_object = {"word_id": definition_to_return._id, "word": definition_to_return.word, "word_def":  definition_to_return.definitionUser}    # return the id, word itself, & definition for json
    return jsonify(json_object)


if __name__ == "__main__":
    app.run(port=5050)

