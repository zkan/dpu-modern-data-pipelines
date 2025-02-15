import pandas as pd


df = pd.read_csv("titanic.csv")
print(df.head())

# วิธีการเรียกดูค่าใน Column
# df["Survived"]
# df.Survived

df.info()

passenger_id_not_null = df.PassengerId.notnull()
dq_passenger_id = passenger_id_not_null.sum() / len(df)
print(f"Data Quality of PassengerId: {dq_passenger_id}")

survived_not_null = df.Survived.notnull()
dq_survived = survived_not_null.sum() / len(df)
print(f"Data Quality of Survived: {dq_survived}")

dq_pclass = df.Pclass.notnull().sum() / len(df)
print(f"Data Quality of Pclass: {dq_pclass}")

age_not_null = df.Age.notnull()
dq_age = age_not_null.sum() / len(df)
print(f"Data Quality of Age: {dq_age}")

cabin_not_null = df.Cabin.notnull()
dq_cabin = cabin_not_null.sum() / len(df)
print(f"Data Quality of Cabin: {dq_cabin}")

embarked_not_null = df.Embarked.notnull()
dq_embarked = embarked_not_null.sum() / len(df)
print(f"Data Quality of Embarked: {dq_embarked}")

print(f"Completeness: {(dq_passenger_id + dq_survived + dq_pclass + dq_age + dq_cabin + dq_embarked) / 6}")

print(df.Age.max(), df.Age.min())
# print(df[df.Age == 0.42])