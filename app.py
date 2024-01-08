#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import os
import dataTransformation as data_trans
from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder='static')
app.config['UPLOAD_FOLDER'] = '/workspaces/data-analysis/static'

@app.route("/")
def challenge_page():
    return render_template("index.html")
    #return app.send_static_file("index.html") 

@app.route("/upload", methods=['GET','POST'])
def upload():

    if request.method == 'POST':

        # getting the json file from input "file"
        f = request.files['file']

        # saving json file within the path
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))    

        msg = data_trans.fileTransform(app.config['UPLOAD_FOLDER']+'/'+f.filename)

        return render_template("index.html", msg=msg)  

@app.route("/download", methods=['GET','POST'])
def download():
    
    msg = send_file(os.path.join(app.config['UPLOAD_FOLDER']+'/csv_file.csv'), as_attachment=True)
    return msg


"""
@app.route("/analysis", methods=['GET','POST'])
def analysis():
    list_tables = data_analysis.dataAnalysis()
    return render_template("index.html", list_tables=list_tables['tables'], titles=list_tables['titles'])
"""

if __name__ == '__main__':
    app.run(debug=True, port=5001)