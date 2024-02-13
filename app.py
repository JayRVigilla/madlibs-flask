from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def root_screen():
		""" return initial screen of prompts for a static story"""
		html = render_template("questions.html", prompts=silly_story.prompts)
		return html

@app.get('/results')
def results_screen():
		""" return  screen of  story knit together"""
		res = request.args
		# print("**", res)
		html = render_template("results.html", story=silly_story.get_result_text(res))
		return html

