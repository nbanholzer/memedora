from flask import Flask, render_template, redirect, url_for
import scripts

app = Flask(__name__)

@app.route("/")
def home():
    return "whatev"

# @app.route("/setpref", methods=['GET','POST'])
# def setpref():
#     if request.method=="POST":
#         data = 

@app.route("/up", methods=['GET','POST'])
def up():
    link = {'link' : scripts.up() }
    return jsonify(link)
    
@app.route("/down", methods=['GET','POST'])
def down():
    link = {'link' : scripts.down() }
    return jsonify(link)

@app.route("/reset", methods=['GET','POST'])
def reset():
    scripts.reset()
    

if __name__ == "__main__":
    application.run('0.0.0.0', port = 8000)
    
