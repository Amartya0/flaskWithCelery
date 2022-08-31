
from flask import Flask, render_template, request
from task import *




app = Flask(__name__)


@app.route("/")
def home():
    return "sup!"

@app.route('/cal', methods=["POST", "GET"])
def cal():
  if request.method == "POST":
    val1 = int(request.form["field1"])
    val2 = int(request.form["field2"])
    if (request.form.get("add")):
      #res = val1 - val2
      res = addition.delay(val1,val2)
      return render_template('index.html', val=res.get())
    if (request.form.get("sub")):
      #res = val1 - val2
      res = sub.delay(val1,val2)
      return render_template('index.html', val=res.get())

    return render_template('index.html')
  else:
    return render_template('index.html', val="na")

@app.route("/wait")
def wait_a_min():
    a_min.delay()
    return "waiter added sucessfully."

if __name__ == '__main__':
    app.run(use_reloader=True)
    