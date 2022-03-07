import joblib
import pandas as pd

if __name__ == '__main__':
    heart_model = joblib.load("./heart_model.pkl")
    new_sample = [[54, 'M', 'NAP', 150, 195, 0, 'Normal', 122, 'N', 0.0, 'Up']]
    new_sample_df = pd.DataFrame(data=new_sample,
                                 columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
                                          'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])

    y_pred = heart_model.predict(new_sample_df)
    print(y_pred)
