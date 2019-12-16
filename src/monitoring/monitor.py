import os

import numpy as np
import pandas as pd
import joblib
import keras.backend as K
from keras.models import load_model


def predict_CTF():
    df = load_data()
    seq_length = 50
    features = [x for x in df.columns if x not in ["id", "cycle", "reg_label", "bnc_label", "mcc_label"]]

    df = scale_input(df, features)
    model = load_LSTM()
    model_input = reshape_input(df, features, seq_length)

    predictions = model.predict(model_input)

    engines = [id for id in df['id'].unique() if len(df[df['id'] == id]) >= seq_length]
    output = prepare_output(engines, predictions)
    return output


def load_data():
    df = pd.read_csv(os.sep.join([os.environ.get("DATA_PATH", "./src/monitoring/data"), "data_to_predict.csv"]))
    return df


def scale_input(df, features):
    features = [x for x in df.columns if x not in ["id", "cycle", "reg_label", "bnc_label", "mcc_label"]]
    X_real = df[features]

    scaler_path = os.sep.join([os.environ.get("MODELS_PATH", "./src/monitoring/data"), "scaler.save"])
    scaler = joblib.load(scaler_path)
    X_scaled = scaler.transform(X_real)
    df[features] = X_scaled
    return df


def load_LSTM():
    model_path = os.sep.join([os.environ.get("MODELS_PATH", "./src/monitoring/data"), "modelLSTM_regre.h5"])
    model = load_model(model_path, custom_objects={"r2_keras": r2_keras}, compile=False)
    return model


def r2_keras(y_true, y_pred):
    """Coefficient of Determination 
    """
    SS_res = K.sum(K.square(y_true - y_pred))
    SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
    return (1 - SS_res/(SS_tot + K.epsilon()))


def reshape_input(df, seq_cols, seq_length):
    real_data_last = [df[df['id']==id][seq_cols].values[-seq_length:]
                      for id in df['id'].unique()
                      if len(df[df['id'] == id]) >= seq_length]
    X_real_last = np.asarray(real_data_last).astype(np.float32)
    return X_real_last


def prepare_output(engines, predictions):
    output = {"success": True}
    pred_x_engine = zip(engines, predictions)
    output["engines"] = {str(k): str(np.round(v[0],1)) + " CTF" for k, v in pred_x_engine}
    print(output)
    return output
