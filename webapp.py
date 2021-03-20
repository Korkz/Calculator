from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/response")
def render_response():
    int xval = request.args.get['xval']
    int yval = request.args.get['yval']
    operation = request.args['operation']
    
    if operation == 'add':
        answer = xval+yval
    if operation == 'sub':
        answer = xval-yval 
    if operation == 'mul':
        answer = xval*yval 
    if operation == 'div':
        answer = xval/yval        
    
    return render_template('response.html', response = answer)
     
if __name__=="__main__":
    app.run(debug=False, port=54321)
