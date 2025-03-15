from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open(r"C:\Users\user\Projects\Brent-Oil-Price-Analysis-for-Birhan-Energies\models\model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    
    prediction = model.predict(df)  # Assuming the model takes a DataFrame as input
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
