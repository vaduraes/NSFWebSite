from model import InputForm
from flask import Flask, render_template, request
from compute import compute
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        
        result = compute(form.A_Lat.data, form.A_Long.data,
                         form.B_Lat.data, form.B_Long.data)

    else:
        result = None

    return render_template('view1.html',form=form, result='oi')
#return render_template('view1.html',form=form, result=str(result).encode())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)



