import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from pickle5 import pickle 

def create_model(data):
    # setting independent and dependent variables
    X = data.drop(['diagnosis'],axis = 1)
    y = data.diagnosis 

    # scaling values 
    scaler = StandardScaler()
    X = scaler.fit_transform(X) 

    # split the data 
    X_train, X_test, y_train, y_test = train_test_split(
        X,y, test_size=0.2, random_state= 42
    )

    # train the model
    model = LogisticRegression()
    model.fit(X_train,y_train) 

    # test the model
    y_preds = model.predict(X_test)
    print("Test set accuracy:",accuracy_score(y_test,y_preds))
    print("Classification Report: \n", classification_report(y_test,y_preds))

    return model, scaler 

def clean_data():
    data = pd.read_csv("/Users/akhil/Downloads/breast cancer/data/data.csv")
    data = data.drop(['Unnamed: 32','id'],axis = 1)
    data['diagnosis'] = data['diagnosis'].map({"M":1,"B":0})
    
    print(data.head()) 
    return data 

def main():
    data = clean_data()
    model,scaler = create_model(data) 

    with open('model/model.pkl','wb') as f:
        pickle.dump(model,f)
    with open('model/scaler.pkl', 'wb') as f:
        pickle.dump(scaler,f) 


if __name__ == '__main__':
    main() 

