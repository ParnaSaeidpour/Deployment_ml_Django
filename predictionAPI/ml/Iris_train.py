
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import joblib


test_size=0.2 
random_state=42


iris = pd.read_csv("Iris.csv")
iris.drop('Id',inplace=True, axis=1)


X=iris.drop(['Species'],axis=1)
y=iris['Species']
encoder=LabelEncoder()
y=encoder.fit_transform(y)

joblib.dump(encoder,'encoder.joblib')


pipeline_KNeighbors = Pipeline([('pca1', PCA(n_components=3)),
    ('KNeighbors',KNeighborsClassifier(n_neighbors=3))
])
pipeline_KNeighbors.fit(X,y)

joblib.dump(pipeline_KNeighbors,'my_model.joblib')




