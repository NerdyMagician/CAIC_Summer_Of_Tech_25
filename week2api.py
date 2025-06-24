
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([
        data['word_count'],
        data['char_count'],
        data['has_media'],
        data['hour'],
        data['sentiment']
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return (jsonify({'predicted_likes': int(prediction)}))


if __name__ == '__main__':
    app.run()
