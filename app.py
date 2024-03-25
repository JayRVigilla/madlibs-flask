from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension

from stories import vacation_story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)

# Project promoted from:
# https://rithm-students-assets.s3.amazonaws.com/r32/exercises/flask-greet-calc/handout/index.html?AWSAccessKeyId=AKIA6I7NF475LYNA7YJL&Signature=VEY%2BrqzvkwyMhC0YnIZ1mAGvSvk%3D&Expires=1707903732

# TODO: Allow User to pick story from home page
# * dropdown menu of story templates
# * after selection, goes to that page for prompts

# TODO: create your own MadLIbs Page
# * persist to database


@app.get('/')
def root_screen():
		""" return initial screen of prompts for a static story"""
		# TODO: use an API to getStories
		html = render_template("questions.html", prompts=story.prompts)
		return html

@app.get('/results')
def results_screen():
		""" return  screen of  story knit together"""
		res = request.args
		# print("**", res)
		html = render_template(
			"results.html", story=story.get_result_text(res), title=story.title)
		return html

