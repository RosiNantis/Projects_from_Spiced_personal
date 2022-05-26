import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


########    Start the project    #############
df = pd.read_csv('save_frames_artists/lyrics_clean.csv')
df.artist_name.loc[df.artist_name == 'bob_dylan'] =0
df.artist_name.loc[df.artist_name == 'eminem'] =1

X = pd.DataFrame(df['lyrics'])
y = df.artist_name
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33,random_state=42)
y_test=y_test.astype(int)
y_train=y_train.astype(int)
def Countvect_fit_transf(trainX, trainY): # sample is the df.song_lyric[:2]
    vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1, 3))
    X = vectorizer.fit_transform(trainX.apply(lambda x: np.str_(x)))    
    X_cv= pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names_out(),index = trainY)


    return X_cv , vectorizer

def Countvect_transf(testX, testY, self_vectorizer): # sample is the df.song_lyric[:2]
    X = self_vectorizer.transform(testX.apply(lambda x: np.str_(x)))    
    X_cv= pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names_out(),index = testY)

    return X_cv

def Countvect_transf_input(inputX, self_vectorizer): # sample is the df.song_lyric[:2]
    X = self_vectorizer.transform([inputX])    
    X_cv= pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names_out())

    return X_cv

input_lyr = input('Give me your lyrics: ')
frame_cv_train, vectorizer =Countvect_fit_transf(X_train['lyrics'], y_train)
frame_cv_test =Countvect_transf(X_test['lyrics'], y_test, vectorizer)
frame_cv_input =Countvect_transf_input(input_lyr, vectorizer)
frame_cv_train.shape, frame_cv_test.shape, frame_cv_input.shape, y_test.shape, y_train.shape


#########        model_training      ########


def pipe_line(model,frame_cv_train, y_train,frame_cv_test, y_test,frame_cv_input,input_lyr):
    if model == 'LogisticRegression':
        pipe = Pipeline([('LogisticRegression', LogisticRegression(class_weight='balanced_subsample'))])
        lr = pipe.fit(frame_cv_train, y_train)  
        train_accuracy = lr.score(frame_cv_train, y_train)
        test_accuracy = lr.score(frame_cv_test, y_test)
        ypred = lr.predict(frame_cv_input) 
        prediction = ypred
        if prediction == 0:
            name = 'Bob_Dylan'
        else:
            name = 'Eminem'
        print(f'The model gives that the \'{input_lyr}\' was said by {name}, with accuracy = {round(test_accuracy,2)*100}%. ')
    elif model == 'RandomForest':
        pipe = Pipeline([('RandomForest', RandomForestClassifier(max_depth=3, n_estimators=10, random_state=42, class_weight='balanced'))])
        parameter_grid = {
                        'RandomForest__max_depth' : [2,3,4,5,6]
                        }
        gridsearch = GridSearchCV(pipe, 
                          parameter_grid, 
                          scoring=None,
                          verbose=3)
        gridsearch.fit(frame_cv_train, y_train)
        gridsearch.best_estimator_.score(frame_cv_test, y_test)
        ypred = gridsearch.best_estimator_.predict(frame_cv_test)
        accuracy_score(ypred, y_test)
        prediction = ypred[0]
        if prediction == 0:
            name = 'Bob_Dylan'
        else:
            name = 'Eminem'
        print(f'The model gives that the \'{input_lyr}\' was said by {name}, with accuracy = {round(accuracy_score(ypred, y_test),2)*100}%.')
    else:
        print('That is not a valid name_model!! Try between \'LogisticRegression\', \'RandomForest\' and \'NEW\'.')

input_model = str(input('Give me which model I should use between \'LogisticRegression\', \'RandomForest\' and \'NEW\'   :    '))
pipe_line(input_model,frame_cv_train, y_train,frame_cv_test, y_test,frame_cv_input,input_lyr)  
 
