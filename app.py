'''
copy and paste text into a text field, 
type in the word you want type in the label
submit it, on click, display the start 
point and end point submit again to save to csv
'''
import sqlite3
import processor as p
import scraper
from flask import Flask, session, render_template, request, jsonify, redirect, url_for, json
from wtforms.fields.simple import TextAreaField
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.validators import DataRequired, Regexp
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
# DATABASE = 'listing_database.db'
Bootstrap(app)

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

class TextParseForm(FlaskForm):
    # text_data = TextAreaField('Text', validators=[DataRequired()])
    word_data = TextAreaField('word:tag', validators=[DataRequired()])
    # tag_data = StringField('tag for word', validators=[DataRequired()])


class ListingURLForm(FlaskForm):
    url = StringField('listing url', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ListingURLForm()
    print('ploop')
    if form.validate_on_submit():
        print('scraping data')
        listing = scraper.get_listing(form.url.data)
        p.store_temp(listing)
        # session['listinginfo'] = listing
        print('stored listing in pickle')
        return redirect(url_for('find_string'))
    return render_template('index.html', form=form)


@app.route('/entryForm', methods=['GET', 'POST'])
def find_string():
    txt_parse_form = TextParseForm()
    # listing = request.args['listinginfo']
    # listing = session.get('listinginfo')
    listing = p.get_temp()
    print('got listing')
    print('==================')
    print(listing)
    print('pewpy')
    if txt_parse_form.validate_on_submit():
        # send to csv file
        print('in if')
        location = p.loc_substr(listing, txt_parse_form.word_data.data)
        print(location, type(location))
        return render_template('validate.html', text_loc=location)
    return render_template('nerDataForm.html', prsform=txt_parse_form, listing=listing)


# @app.route('/validate', methods=['GET', 'POST'])
# def validate_data():
#     listing=p.get_temp()