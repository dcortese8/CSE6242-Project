import pandas as pd
import numpy as np
import os
import pickle

class models():
    avg_prediction = None
    models = {}
    predictions = {}
    r2_scores = {}
    mse_scores = {}
    rmse_scores = {}
    mae_scores = {}

    def __init__(self, model_list):
        # self.model_type = model_type
        self.load_models(model_list)

    def load_models(self, model_list):
        model_list = [" ".join(x.capitalize() for x in file.split(".")[0].split("_")) for file in os.listdir("./saved_models")]
        for model_name in model_list:
            model_file = "_".join(x.lower() for x in model_name.split(" "))
            mod = "".join(["./saved_models/", model_file, ".pkl"])
            with open(mod, 'rb') as f:
                self.models[model_name] = pickle.load(f)

    def make_predictions(self, input_data):
        for name, mod in self.models.items():
            print('predicting... ' + str(round(mod.predict(input_data)[0], 2)))
            self.predictions[name] = str(round(mod.predict(input_data)[0], 2))
        self.avg_prediction = np.mean([float(x) for x in self.predictions.values()])
