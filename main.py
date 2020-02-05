from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from application_semantic_search_open_corpus import runAnalysis, addQueries
app = Flask(__name__)


# 업로드 HTML 렌더링
@app.route('/')
def render_file():
    return render_template('upload.html')


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
    input_value = request.form['input_query']
    addQueries(input_value)
    return redirect(url_for('run_file'))


@app.route('/runfile', methods=['GET', 'POST'])
def run_file():
    result = runAnalysis()
    return jsonify(result)


if __name__ == '__main__':
    # server execute
    app.run(host='0.0.0.0', port=80, debug=True)


"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from application_semantic_search_open_corpus import runAnalysis
app = Flask(__name__)


# 업로드 HTML 렌더링
@app.route('/')
def render_file():
    return render_template('upload.html')


@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save('/ainized-sentence-transformers/upload/' +
               secure_filename(f.filename))
        return redirect(url_for('run_file'))  # redirect할 것을 method명으로 처리함


@app.route('/runfile')
def run_file():
    result = runAnalysis()
    return jsonify(result)


if __name__ == '__main__':
    # server execute
    app.run(host='0.0.0.0', port=80, debug=True)
"""
