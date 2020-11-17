'''
copy and paste text into a text field, 
type in the word you want type in the label
submit it, on click, display the start 
point and end point submit again to save to csv
'''
import sqlite3
import processor as p
from flask import Flask, render_template, request, jsonify, redirect, url_for, json
from wtforms.fields.simple import TextAreaField
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
DATABASE = 'listing_database.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

class TextParseForm(FlaskForm):
    text_data = TextAreaField('Text', validators=[DataRequired()])
    word_data = StringField('word to tag', validators=[DataRequired()])
    tag_data = StringField('tag for word', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def find_string():
    form = TextParseForm()
    print('pewpy')
    if form.validate_on_submit():
        # send to csv file
        print('in if')
        location = p.loc_substr(form.text_data.data, form.word_data.data)
        print(location, type(location))
        return render_template('validate.html', text_loc=location)
    return render_template('index.html', form=form)