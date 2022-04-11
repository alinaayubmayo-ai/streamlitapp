import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns 

def app():
    st.title('Model')

    st.write('This is the `Model` page of the multi-page app.')

    st.write('The model performance of the Iris dataset is presented below.')

    # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    # Model building
    st.header('Model performance')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    st.write('Accuracy:')
    st.write(score)

# Plotting Confusion Matrix
    Y_pred = clf.predict(X_test)
    cm = confusion_matrix(Y_test, Y_pred)
    fig = plt.figure()
    fig = plt.figure(figsize=(5,5))
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap="viridis")
    plt.ylabel("Actual Output")
    plt.xlabel("Predicted Output")
    all_sample_title = "Accuracy Score: {0}".format(score)
    plt.title(all_sample_title, size = 8)

    st.pyplot(fig)