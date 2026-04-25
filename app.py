from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model and the dictionary of encoders
model = joblib.load('fraud_model.pkl')
encoders_dict = joblib.load('encoders_dict.pkl')
model_features = model.feature_names_in_

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        query_df = pd.DataFrame([data])
        
        # 1. Align features (Ensures correct order and handles missing columns)
        query_df = query_df.reindex(columns=model_features)

        # 2. Encode categorical columns using the correct saved encoder
        for col, encoder in encoders_dict.items():
            if col in query_df.columns:
                val = str(query_df[col].iloc[0])
                try:
                    # Transform the value using the specific encoder for this column
                    query_df[col] = encoder.transform([val])
                except:
                    # If the value wasn't seen in training, assign a default (-1)
                    query_df[col] = -1
            
        # 3. Make prediction
        prediction = model.predict(query_df)
        result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
        
        return jsonify({
            'prediction': result,
            'status': 'success'
        })
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({'error': str(e), 'status': 'fail'})

# if __name__ == '__main__':
#     app.run(debug=True, port=5002)
import os

if __name__ == '__main__':
    # Use the PORT environment variable if it exists (for Render), 
    # otherwise default to 5002 for local testing.
    port = int(os.environ.get("PORT", 5002))
    
    # Set debug=False for deployment; host="0.0.0.0" is required for cloud access
    app.run(host="0.0.0.0", port=port, debug=False)