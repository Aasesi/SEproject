from App import App
import pandas as pd
import random
import numpy as np


if __name__ == '__main__':
#    df = pd.read_csv("csvFiles/heart_disease_health_indicators_BRFSS2015.csv")
#    df2 = df.head(10)

#    print(len(df))
#    unique_numbers_list: list[str] = []
#    iteration = 0
#    while len(unique_numbers_list) < len(df2):
#        num = str(random.randint(0, 99999))
#        while len(num) < 5:
#            num = "0" + num
#        unique_numbers_list.append(num)
#        unique_numbers_list = list(set(unique_numbers_list))
#        iteration += 1
#        print(iteration)

#    df2.insert(0, "Patient_code", unique_numbers_list)
#    df2.to_csv("patients_data", index=False)

    app = App()
    app.mainloop()
