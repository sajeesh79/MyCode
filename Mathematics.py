from flask import Flask, render_template, abort, request, redirect, url_for
from flask import session
from Addition_within_100 import gen_random

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

no_of_q = 24
cols = 8
min_n = 1
# max_n = 5000

@app.route("/")
def welcome():
    return render_template('welcome.html')


# ----------------
# Addition
# ----------------
@app.route("/addition", defaults={"max_n": 50, "no_of_q": 16}, methods=['GET', 'POST'])
@app.route("/addition/<int:max_n>/<int:no_of_q>", methods=['GET', 'POST'])
def cal_addition_within_100(max_n, no_of_q):
    if request.method == 'POST':
        answers_add_within_100 = {}
        marks = 0
        for i in range(0, session['no_of_q']):
            input_name = "text" + str(i)
            answers_add_within_100[i] = request.form[input_name]
            if str(session['questions'][str(i)][2]) == answers_add_within_100[i]:
                marks = marks + 1
        session['marks'] = str(marks) + " / " + str(session['no_of_q'])
        session['answers'] = answers_add_within_100
        return redirect(url_for('display_answers'), code=307)
    else:
        session['answers'] = {}
        session['max_limit'] = max_n
        session['no_of_q'] = no_of_q
        dict_of_nums_to_add = {}
        for i in range(0, session['no_of_q']):
            nums_to_add = gen_random(min_n, session['max_limit'])
            dict_of_nums_to_add[i] = nums_to_add
        # print(dict_of_nums_to_add)
        session['questions'] = dict_of_nums_to_add
        return render_template('addition_within_100.html', nums_to_add=dict_of_nums_to_add, cols=cols, max_len=len(str(max_n))+1)


@app.route("/answers_add", methods=['GET', 'POST'])
def display_answers():
    if request.method == 'POST':
        print(session['questions'])
        print(session['answers'])
        return render_template('disp_add_within_100.html', answers_to_display=session['answers'], questions_to_display=session['questions'], cols=cols, marks=session['marks'])
    else:
        return render_template('disp_add_within_100.html', answers_to_display=session['answers'], questions_to_display=session['questions'])
