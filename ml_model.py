import pandas as pd
import matplotlib.pyplot as plt
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import permutation_test_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('merged.csv', index_col=False)
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
X_train = train_data[['views', 'likes','comment_total','compound_score']]
y_train = train_data["dislikes"]
X_test = test_data[["views", "likes",'comment_total','compound_score']]
y_test = test_data["dislikes"]

#scaling the dataset and predicting with linear regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
LRmodel = LinearRegression()
LRmodel.fit(X_train_scaled, y_train)
lr_y_pred = LRmodel.predict(X_test_scaled)
print('\n')
print("Mean Squared Error for Linear Regression:", round(mean_squared_error(y_test, lr_y_pred), 3))
print("Root Mean Squared Error for Linear Regression:", round(mean_squared_error(y_test, lr_y_pred, squared=False), 3))
print("R-squared Score for Linear Regression:", round(r2_score(y_test, lr_y_pred), 3))

# random forest
RFmodel = RandomForestRegressor()
RFmodel.fit(X_train_scaled, y_train)
rf_y_pred = RFmodel.predict(X_test_scaled)
print('\n')

print("Mean Squared Error for Random Forest:", round(mean_squared_error(y_test, rf_y_pred), 3))
print("Root Mean Squared Error for Random Forest:", round(mean_squared_error(y_test, rf_y_pred, squared=False), 3))
print("R-squared Score for Random Forest:", round(r2_score(y_test, rf_y_pred), 3))

# k-neighbour
KNmodel = KNeighborsRegressor(n_neighbors=20)
KNmodel.fit(X_train_scaled, y_train)
kn_y_pred = KNmodel.predict(X_test_scaled)
print('\n')
print("Mean Squared Error for K-Neighbour:", mean_squared_error(y_test, kn_y_pred))
print("Root Mean Squared Error for K-Neighbour:", mean_squared_error(y_test, kn_y_pred, squared=False))
print("R-squared Score for K-Neighbour:", r2_score(y_test, kn_y_pred))