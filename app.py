from flask import Flask, request, render_template 
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Load the model
# model = tf.keras.models.load_model('model.h5')
model = tf.keras.models.load_model(r'c:\Users\Haider Ali\PycharmProjects\flaskapp\potato_disease_classification\model.h5')
class_names = ['bad_quality', 'empty_background','good_quality']
BATCH_SIZE = 32
IMAGE_SIZE = 255
CHANNEL = 3
EPOCHS = 20



# Function to preprocess and predict
def predict(img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

# Route to the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']  # Corrected line

        # If the user does not select a file, browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', message='No selected file')

        # If the file is allowed and has an allowed extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('static', filename)
            file.save(filepath)

            # Read the image
            img = tf.keras.preprocessing.image.load_img(filepath, target_size=(IMAGE_SIZE, IMAGE_SIZE))

            # Predict using the loaded model
            predicted_class, confidence = predict(img)

            # Render the template with the uploaded image, actual and predicted labels, and confidence
            return render_template('index.html', image_path=filepath, actual_label=predicted_class, predicted_label=predicted_class, confidence=confidence)

    return render_template('index.html', message='Upload an image')

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

# from openai import OpenAI

# client = OpenAI(
#   api_key="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"
# )

# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user", "content": "write a haiku about ai"}
#   ]
# )

# print(completion.choices[0].message);


if __name__ == '__main__':
    app.run(debug=True)




