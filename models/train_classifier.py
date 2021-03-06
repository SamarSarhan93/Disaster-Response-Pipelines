import sys
import pandas as pd
from sqlalchemy import create_engine
import nltk
import re
import pickle
nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

def load_data(database_filepath):
    """Load database from filepath

    INPUT
    database_filepath -- str, link to file

    OUTPUT
    X - pandas DataFrame
    Y - pandas DataFrame
    categories - pandas DataFrame
    """
    engine_path = 'sqlite:///' + database_filepath
    engine = create_engine(engine_path)
    df = pd.read_sql_table('Disasters', con=engine)
    X = df['message']
    y = df.iloc[:, 4:39]
    #inplace 2 with 1 in y
    y['related'].replace(2, 1, inplace=True)
    categories = y.columns.tolist()
    return X, y, categories

def tokenize(text):
    """tokenize text

    INPUT
    text -- str

    OUTPUT
    cleaned - str
    """
    new_text = re.sub(r'[^\w\s]','',text)
    tokens = word_tokenize(new_text)
    lemmatizer = WordNetLemmatizer()

    cleaned = []
    for token in tokens:
        cleaned.append(lemmatizer.lemmatize(token).lower().strip())

    return cleaned

def build_model():
    """build model

    OUTPUT
    model - pandas DataFrame
    """
    pipeline = Pipeline([
            ('vect', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(AdaBoostClassifier()))
        ])
    parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
    model = GridSearchCV(pipeline, parameters)

    return model
    
def evaluate_model(model, X_test, Y_test, category_names):
    """evaluate model

    INPUT
    model -- model
    X_test -- df
    Y_test -- df
    category_names -- list of str

    OUTPUT
    classification reports - str
    """
    y_pred = model.predict(X_test)
    for i in range(35):
        print("Precision, Recall, F1 Score for {}".format(y_test.columns[i]))
        print(classification_report(y_test.iloc[:,i], y_pred[:,i]))

def save_model(model, model_filepath):
    """save model

    INPUT
    model -- model
    model_filepath -- str
    
    """
    pickle.dump(model, open(model_filepath, 'wb'))

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
