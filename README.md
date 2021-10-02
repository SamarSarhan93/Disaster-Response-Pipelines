# Disaster-Response-Pipelines

This project is to classify disaster response messages through machine learning From  Udacity Data Scientist nanodegree programme.

## File Structure

- app<br>
| - template<br>
| |- master.html  # main page of web app<br>
| |- go.html  # classification result page of web app<br>
|- run.py  # Flask file that runs app<br>

- data<br>
|- disaster_categories.csv  # data to process<br> 
|- disaster_messages.csv  # data to process<br>
|- process_data.py<br>
|- CleanDatabase.db   # database to save clean data to<br>

- models<br>
|- train_classifier.py<br>
|- cv_AdaBoostr.pkl  # saved model <br>

## Content
- Data
  - process_data.py: reads in the data, cleans and stores it in a SQL database. Basic usage is python process_data.py MESSAGES_DATA CATEGORIES_DATA NAME_FOR_DATABASE
  - disaster_categories.csv and disaster_messages.csv (dataset)
  - DisasterResponse.db: created database from transformed and cleaned data.
- Models
  - train_classifier.py: includes the code necessary to load data, transform it using natural language processing, run a machine learning model using GridSearchCV and train it. Basic usage is python train_classifier.py DATABASE_DIRECTORY SAVENAME_FOR_MODEL  
- App
  - run.py: Flask app and the user interface used to predict results and display them.
  - templates: folder containing the html templates

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
        
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/cv_AdaBoost.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Screenshots
This is the frontpage:
![screen1](https://user-images.githubusercontent.com/91026154/135733020-090338bc-205b-4266-b068-ab8d5b1cb417.jpg)
![screen2](https://user-images.githubusercontent.com/91026154/135733038-a76544e2-aa87-4ad8-baaf-9f65d54b129d.jpg)




By inputting a word, you can check its category:
![screen3](https://user-images.githubusercontent.com/91026154/135733048-d7091d14-278a-4a1e-b0f0-6cacc5791c0e.jpg)


## About
This project was prepared as part of the Udacity Data Scientist nanodegree programme. The data was provided by Figure Eight.
