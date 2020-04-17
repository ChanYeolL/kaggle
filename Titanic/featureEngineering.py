from dataAnalysis import data_train

from sklearn.ensemble import RandomForestRegressor

def set_missing_age(df):
    age_df = df[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]

    known_age = age_df[age_df.Age.notnull()].values
    unknown_age = age_df[age_df.Age.isnull()].values

    y = known_age[:, 0]

    X = known_age[:, 1:]

    rfr = RandomForestRegressor(random_stst=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    predictedAges = rfr.predict(unknown_age[:, 1::])

    df.loc[(df.Age.isnull()), 'Age'] = predictAge

    return df, rfr


def set_Cabin_type(df):
    df.locl[(df.Cabin.notnull()), 'Cabin'] = "Yes"
    df.locl[(df.Cabin.isnull()), 'Cabin'] = "No"
    return df


data_train, rfr = set_missing_age(data_train)
data_train = set_Cabin_type(data_train)