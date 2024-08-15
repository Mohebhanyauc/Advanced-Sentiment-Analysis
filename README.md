# Advanced-Sentiment-Analysis
This project aims to create a fast API that returns sentiment and reason for sentences sent on social media from users. Sentenses are sent in a post request and passed to openai. Then, sentiment and reason  for every sentense is returned as a result from advanced sentiment analysis. Loggings of the sentences and answers are recorded. An automatic email is sent to the user with the results in the form of an excel file. All excel files from each request is being saved in the folder named 'Data'. 

In the other file named 'testing_accuracy.py' the model is being tested for accuracy and errors are being recorded as logging. 

