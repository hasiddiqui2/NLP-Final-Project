import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
us_url = 'https://raw.githubusercontent.com/MayurDeshmukh10/youtube_analysis/master/USvideos.csv'
us_data = pd.read_csv(us_url, usecols=['video_id', 'views', 'likes', 'dislikes','comment_count'], index_col=None)

our_data = pd.read_csv('merged.csv', index_col=False)


# bag-of-words model
def detect_word_score(text):
    positive = ['amazing', 'awesome', 'great', 'fantastic', 'excellent','fabulous', 
                'wonderful', 'terrific','impressive','superb','spectacular','phenomenal', 
                'incredible', 'outstanding','marvelous','perfect','splendid', 'delightful', 
                    'lovely','fantabulous']

    negative = ['terrible', 'awful','horrible', 'disappointing','pathetic','dismal','poor', 'bad',
                'gross', 'unpleasant','mediocre','subpar', 'dreadful', 'unfortunate','miserable',
                'lousy', 'unsatisfactory','inferior','atrocious','abysmal']

    score = 0

    text_words = text.lower().split()
    for word in text_words:
        if word in positive:
            score += 1
        if word in negative:
            score -= 1
    return score

# df['score'] = df.apply(detect_word_score)
# count = df.groupby('video_id')['score'].count()
# df.groupby("video_id")['score'].sum()/count


#toggle comment between train_test to use our_data and,or us_data

train_data, test_data = train_test_split(us_data, test_size=0.2, random_state=42)
X_train = train_data[['views', 'likes','comment_count']]
y_train = train_data["dislikes"]
X_test = test_data[["views", "likes",'comment_count']]
y_test = test_data["dislikes"]


train_data, test_data = train_test_split(our_data, test_size=0.2, random_state=42)
X_train = train_data[['views','likes','comment_total','compound_score']]
y_train = train_data['dislikes']
X_test = test_data[['views','likes','comment_total','compound_score' ]]
y_test = test_data['dislikes']

# scaling the dataset and predicting with linear regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
LRmodel = LinearRegression()
LRmodel.fit(X_train_scaled, y_train)
lr_y_pred = LRmodel.predict(X_test_scaled)
print("Mean Squared Error for Linear Regression:", round(mean_squared_error(y_test, lr_y_pred), 3))
print("Root Mean Squared Error for Linear Regression:", round(mean_squared_error(y_test, lr_y_pred, squared=False), 3))
print("R-squared Score for Linear Regression:", round(r2_score(y_test, lr_y_pred), 3))
print('\n')

# random forest
RFmodel = RandomForestRegressor()
RFmodel.fit(X_train_scaled, y_train)
rf_y_pred = RFmodel.predict(X_test_scaled)
print("Mean Squared Error for Random Forest:", round(mean_squared_error(y_test, rf_y_pred), 3))
print("Root Mean Squared Error for Random Forest:", round(mean_squared_error(y_test, rf_y_pred, squared=False), 3))
print("R-squared Score for Random Forest:", round(r2_score(y_test, rf_y_pred), 3))
print('\n')

# k-neighbour
KNmodel = KNeighborsRegressor(n_neighbors=20)
KNmodel.fit(X_train_scaled, y_train)
kn_y_pred = KNmodel.predict(X_test_scaled)
print("Mean Squared Error for K-Neighbour:", mean_squared_error(y_test, kn_y_pred))
print("Root Mean Squared Error for K-Neighbour:", mean_squared_error(y_test, kn_y_pred, squared=False))
print("R-squared Score for K-Neighbour:", round(r2_score(y_test, kn_y_pred),3))
print('\n')

#sns.regplot(data = our_data, x = 'compound_score', y = 'likes')
#plt.show()

sns.regplot(data=our_data,x='likes',y='compound_score')
plt.title('Regression plot for views & likes')
plt.show()

corr = our_data['views'].corr(our_data['compound_score'])
corr1 = our_data['dislikes'].corr(our_data['compound_score'])
corr2 = our_data['likes'].corr(our_data['compound_score'])
corr3 = our_data['comment_total'].corr(our_data['compound_score'])

print(f'Correlation between views and sentiment is: {corr}')
print(f'Correlation between dislikes and sentiment is: {corr1}')
print(f'Correlation between likes and sentiment is: {corr2}')
print(f'Correlation between comment count and sentiment is: {corr3}')