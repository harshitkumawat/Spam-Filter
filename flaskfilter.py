import pickle
import os
from collections import Counter
from flask import Flask,render_template, redirect, url_for, request
from sklearn.externals import joblib
app = Flask(__name__)
loaded_pickle = joblib.load('spam_filter.pkl')
@app.route('/')
def main():
	return render_template('index.html')

def dictionary() :
	path="emails\\"
	files=os.listdir(path)
	emails=[path + email for email in files]
	words=[]
	for word in emails:
		f=open(word,errors='ignore')
		words+=f.read().split(" ")
	for word in range(len(words)):
		if not words[word].isalpha():
			words[word]=""
	dictionary=Counter(words)
	del dictionary[" "]
	return dictionary.most_common(2500)

@app.route('/spamfilter',methods=["GET","POST"])
def spamfilter():
	d = dictionary()
	features = []
	org = request.form['message']
	message = org.split()
	for word in d:
		features.append(message.count(word[0]))
	result = loaded_pickle.predict([features])
	if result == 0:
		return render_template('index.html',value=0,org=org)
	else:
	    return render_template('index.html',value=1,org=org)

@app.route('/reset',methods=["GET","POST"])
def reset():
	return render_template('index.html')
if __name__ == "__main__":
   app.run()