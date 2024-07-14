from flask import Flask,render_template,request
from textsummary import summarizer


app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == "POST":
        rawtext = request.form['rawtext']
        summary, original_text, length_of_originaltext, length_of_summary = summarizer(rawtext)
    return render_template('summary.html', summary=summary, original_text=original_text, length_of_originaltext=length_of_originaltext, length_of_summary=length_of_summary)    
if __name__=="__main__":
    app.run(debug=True)
