# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/')
def load_form():
    return render_template('upload.html')
@app.route('/grey', methods=['POST'])
def ui():
    file = request.files['file']
    filename = request.files(file.filename)
    file.save(os.path.join('static/', filename))
    dm= "image uploaded successfully. Displayed below."
    return render_template('upload.html', filename = filename, message = dm)
@app.route('/display/<filename>')
def di(filename):
    return redirect(url_for('static', filename=filename))
if __name__=="__main__":
    app.run()

# Write load_form function below to Open and redirect to default upload webpage





# Write upload_image Function to upload image and redirect to new webpage









# Write display_image Function to display the uploaded image





if __name__ == "__main__":
    app.run()