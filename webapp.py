from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/response", methods=['POST', 'GET'])
def render_response():
    xval = request.form['xval']
    yval = request.form['yval']
    xval = int(xval)
    yval = int(yval)
    operation = request.form['operation']
    coloranswer = request.form['color']
    
    if operation == 'add':
        answer = int(xval+yval)
    if operation == 'sub':
        answer = int(xval-yval)
    if operation == 'mul':
        answer = int(xval*yval)
    if operation == 'div':
        answer = int(xval/yval)      
    
    return render_template('response.html', response = answer, color = coloranswer)
     
if __name__=="__main__":
    app.run(debug=False, port=54321)
