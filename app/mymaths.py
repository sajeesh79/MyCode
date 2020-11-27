from flask import render_template, request, redirect, url_for
from flask import session
from Addition import gen_random, gen_random_for_first, gen_random_for_second

from flask import Flask
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


cols = 5
min_n = 1
no_of_q = 20
# max_n = 5000

@app.route("/")
def welcome():
    return render_template('welcome.html')


# ----------------
# Addition
# ----------------
@app.route("/addition", methods=['GET', 'POST'])
def display_questions():
    if request.method == 'POST':
        session['max_n'] = int(request.form['limit_max1'])
        session['no_of_q'] = int(request.form['questions'])
        # session['no_of_q'] = no_of_q
        dict_of_nums_to_add = {}
        for i in range(0, session['no_of_q']):
            if request.form['limit_max2'] != "":
                session['max_2'] = int(request.form['limit_max2'])
                num1_to_add = gen_random_for_first(min_n, session['max_n'])
                num2_to_add = gen_random_for_second(min_n, session['max_2'])
                nums_to_add = [num1_to_add, num2_to_add, (num1_to_add + num2_to_add)]
            else:
                nums_to_add = gen_random(min_n, session['max_n'])
            dict_of_nums_to_add[i] = nums_to_add
        # print(dict_of_nums_to_add)
        session['questions'] = dict_of_nums_to_add
        max_of_limits = max(session['max_n'], session['max_2'])
        return render_template('addition.html', nums_to_add=dict_of_nums_to_add, cols=cols, max_len=len(str(max_of_limits))+1)
    else:
        return render_template('welcome.html')

@app.route("/calculate_answers", methods=['GET', 'POST'])
def calculate_answers():
    answers_add = {}
    marks = 0
    if request.method == 'POST':
        for i in range(0, session['no_of_q']):
            input_name = "text" + str(i)
            answers_add[i] = request.form[input_name]
            if str(session['questions'][str(i)][2]) == answers_add[i]:
                marks = marks + 1
        session['marks'] = str(marks) + " / " + str(session['no_of_q'])
        session['answers'] = answers_add
        return redirect(url_for('display_answers'), code=307)
    else:
        return render_template('disp_add.html', answers_to_display=session['answers'], questions_to_display=session['questions'])


@app.route("/answers_add", methods=['GET', 'POST'])
def display_answers():
    if request.method == 'POST':
        print(session['questions'])
        print(session['answers'])
        return render_template('disp_add.html', answers_to_display=session['answers'], questions_to_display=session['questions'], cols=cols, marks=session['marks'])
    else:
        return render_template('disp_add.html', answers_to_display=session['answers'], questions_to_display=session['questions'])


if __name__ == '__main__':
    app.run()

