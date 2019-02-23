import os
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.svm import SVC , LinearSVC

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

def dataset(dictionary):
	path="emails\\"
	files=os.listdir(path)
	emails=[path + email for email in files]
	feature_vec = []
	label = []
	for email in emails:
		data=[]
		f=open(email,errors='ignore')
		words=f.read().split(" ")
		for entry in dictionary:
			data.append(words.count(entry[0]))
		feature_vec.append(data)
		if 'ham' in email:
			label.append(0)
		elif 'spam' in email:
			label.append(1)
	return feature_vec,label

d=dictionary()
features,label=dataset(d)
print("feature_vector length -: ",len(features))
print("\nlabel length -: ",len(label))

x_train,x_test,y_train,y_test=train_test_split(features,label,test_size=0.2)
model = MultinomialNB()
model1 = LinearSVC()
model.fit(x_train, y_train)
model1.fit(x_train, y_train)
pred = model.predict(x_test)
pred1 = model1.predict(x_test)
print(pred)
print(accuracy_score(y_test, pred))
print(accuracy_score(y_test, pred1))
joblib.dump(model, 'spam_filter.pkl')
'''f=open("mail.txt",errors='ignore')
features = []
words=f.read().split()
for word in d:
    features.append(words.count(word[0]))
result = model.predict([features])
if result == 0:
    print('Not spam')
else:
    print('Spam!')
more="y"
while True:
	features = []
	more=input("Want to check Email...(y/n)")
	if more == "n":
	    joblib.dump(model, 'spam_filter.pkl')
	    print('Exiting... Model saved as spam_filter.pkl')
	    exit(0)
	else:
		message = input('Message: ').split()
		for word in d:
			features.append(message.count(word[0]))
		result = model.predict([features])
		if result == 0:
		    print('Not spam')
		else:
		    print('Spam!')'''