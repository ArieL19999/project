
from flask import Flask, render_template
import score, settings


app = Flask(__name__)

def get_name():
  name = Utils.USER_NAME
  return name

def get_score():
  file_name = Utils.SCORES_FILE_NAME
  last_score = score.get_last_line(file_name)
  return last_score 

@app.route("/")
def home():
  name = get_name()
  score = get_score()
  return render_template('home_page.html', name = name, score = score)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error = "No Score and no Page"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error = "No score and Internal Server Error"), 500


if __name__ == "__main__":
  app.run()
  
