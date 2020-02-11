# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from application_semantic_search_open_corpus import runAnalysis, addQueries
from application_semantic_search import runSample
from application_semantic_search_ko import runSampleKo
from application_semantic_search_open_corpus_ko import runAnalysisKo, addQueriesKo
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


# 업로드 HTML 렌더링
@app.route('/')
def render_file():
    return render_template('initial_check.html')


@app.route('/initialCheck', methods=['GET', 'POST'])
def initial_check():
    check_value = request.form['checkValue']
    if check_value == "0":
        return render_template('check_ko_eng.html')
    elif check_value == "1":
        return render_template('upload.html')


@app.route('/check_ko_eng', methods=['GET', 'POST'])
def check_ko_eng():
    check_value = request.form['checkValue']
    if check_value == "0":
        return redirect(url_for('sample_run'))
    elif check_value == "1":
        return redirect(url_for('sample_ko'))


@app.route('/sample', methods=['GET', 'POST'])
def sample_run():
    sample_result = runSample()
    return jsonify(sample_result)


@app.route('/sample_ko', methods=['GET', 'POST'])
def sample_ko():
    sample_result = runSampleKo()
    return jsonify(sample_result)


@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save('/ainized-sentence-transformers/upload/' +
               secure_filename(f.filename))
        # redirect할 것을 method명으로 처리함
        return redirect(url_for('render_query'))


@app.route('/renderQuery', methods=['GET', 'POST'])
def render_query():
    return render_template('input.html')


@app.route('/changeQuery', methods=['GET', 'POST'])
def change_query():
    split_input_value = []
    input_value = []
    input_value.append(request.form['input_query'])
    for i in range(1):
        split_input_value = input_value[i].split(",")
    split_input_value = [line.strip() for line in split_input_value]

    check_value = request.form['check_language']
    if check_value == "en":
        addQueries(split_input_value)
        return redirect(url_for('run_file'))
    elif check_value == "ko":
        addQueriesKo(split_input_value)
        return redirect(url_for('run_ko_file'))


@app.route('/runfile', methods=['GET', 'POST'])
def run_file():
    result = runAnalysis()
    return jsonify(result)


@app.route('/run_ko_file', methods=['GET', 'post'])
def run_ko_file():
    result = runAnalysisKo()
    return jsonify(result)


@app.route('/upload_your_sample', methods=['GET', 'POST'])
def upload_your_sample():
    upload_file()
    change_query()
    return run_file()


@app.route('/upload_your_sample_ko', methods=['GET', 'POST'])
def upload_your_sample_ko():
    upload_file()
    change_query()
    return run_ko_file()


if __name__ == '__main__':
    # server execute
    app.run(host='0.0.0.0', port=80, debug=True)
