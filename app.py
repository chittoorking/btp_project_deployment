import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from keras.models import model_from_json

app = Flask(__name__)
def load_model():
# load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    anomaly_model = pickle.load(open('clf_model.pkl', 'rb'))
    return loaded_model,anomaly_model
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
# @app.route('/predict',methods=['GET','POST'])
def predict():
    # pca_np=np.array([P_j1_t,P_j2_t,P_j3_t,P_j4_t,P_j5_t,P_j6_t,P_j7_t,V_j1_t,V_j2_t,V_j3_t,V_j4_t,V_j5_t,V_j6_t,V_j7_t,T_j1_t,T_j2_t,T_j3_t,T_j4_t,T_j5_t,T_j6_t,T_j7_t]).reshape(1,21).astype(np.float64)
    # pca_df=pd.DataFrame(pca_np,columns=["P_j1_t","P_j2_t","P_j3_t","P_j4_t","P_j5_t","P_j6_t","P_j7_t","V_j1_t","V_j2_t","V_j3_t","V_j4_t","V_j5_t","V_j6_t","V_j7_t","T_j1_t","T_j2_t","T_j3_t","T_j4_t","T_j5_t","T_j6_t","T_j7_t"])
    float_features = [float(x) for x in request.form.values()]
    float_features = np.array(float_features).reshape(1,21).astype(np.float64)
    final_features =pd.DataFrame(float_features,columns=["P_j1_t","P_j2_t","P_j3_t","P_j4_t","P_j5_t","P_j6_t","P_j7_t","V_j1_t","V_j2_t","V_j3_t","V_j4_t","V_j5_t","V_j6_t","V_j7_t","T_j1_t","T_j2_t","T_j3_t","T_j4_t","T_j5_t","T_j6_t","T_j7_t"])
    loaded_model,anomaly_model = load_model()
    prediction = loaded_model.predict(final_features)
    output=anomaly_model.predict(prediction)
    return render_template('index.html', prediction_text='Anomaly status $ {}'.format(output[0]))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    float_features = [float(x) for x in list(data.values())]
    float_features = np.array(float_features).reshape(1,21).astype(np.float64)
    final_features =pd.DataFrame(float_features,columns=["P_j1_t","P_j2_t","P_j3_t","P_j4_t","P_j5_t","P_j6_t","P_j7_t","V_j1_t","V_j2_t","V_j3_t","V_j4_t","V_j5_t","V_j6_t","V_j7_t","T_j1_t","T_j2_t","T_j3_t","T_j4_t","T_j5_t","T_j6_t","T_j7_t"])
    loaded_model,anomaly_model = load_model()
    prediction = loaded_model.predict(final_features)
    output=anomaly_model.predict(prediction)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
# app.run(host='0.0.0.0', port = 80)
