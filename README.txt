Programming Language Required:
Python v3.7 (or above)

Libraries Required:
numpy 
pandas
tensorflow
elasticsearch
streamlit
PIL
re
nltk
warnings
logging
json
csv
time
fse

Note for libraries:
Please install tensorflow and elastic search in your local system before proceeding with the steps. 
We have installed the libraries in a Linux system (Ubuntu 20.04 LTS). Make sure you have installed
them as per your system (MacOS, Linux or Windows) as per their official documentation.

Dataset Required:
The dataset used in this project can be downloaded from the following link
"https://www.kaggle.com/datasets/stackoverflow/stacksample"
The dataset is a zip file containing 3 files namely "Answers.csv", "Questions.csv" and "Tags.csv".
It contains 1264216 Questions and the corresponding answers and tags on stackoverflow website.

Steps to run:

Step 1: Download the dataset and extract the files ("Answers.csv", "Questions.csv" and "Tags.csv") in a folder
        in your local system.

Step 2: Extract group-8-project.zip in the same folder.

Step 3: Run "1_reading_dataset.ipynb". (It may take 1 hr to 5 hr depending on your processor).
        A file named "questions_answers_tags.csv" will be created in the same folder.

Step 4: Run "2_reduce_dataset.ipynb". (It may take upto 5 minutes to 30 minutes depending on your processor).
        A file named "QAs_cleaned.csv" will be created in the same folder.

Step 5: Run "3_fse.ipynb". (It may take upto 30 minutes to 1 hour depending on your processor).
        A file named "final1.pkl" will be created in the same folder. This file has sentence vectors added.

[At this point, our dataset is finally ready.Now we will proceed with data ingestion into Elastic Seach (ES).]

Step 6: Run "4_ingest.ipynb". (It may take upto 2 hour to 5 hours depending on your processor).

Step 7: Open terminal in the same folder and type "streamlit run WebApp_new.py" (without the quotes) and the 
        application will be deployed on your localhost 8051. It will show a link in the terminal, clicking on 
        which will open the app in the browser.

Step 8: When the application is deployed, a new webpage will open where you can enter your query and see the outputs.

Step 9: When the results are displayed for each query, you can click on any question and it will directly link you to 
        the stackoverflow webpage containing all the answers for that particular question.

Step 10: To terminate the application, press Ctrl+X or Ctrl+C to terminate the session and stop the app.

Contact:
If you have any issues to run the project, please mail at any one of the following email ids.
{gajenders21@iitk.ac.in}, {kajals21@iitk.ac.in}, {pranshus21@iitk.ac.in}, {utkarshs21@iitk.ac.in}.