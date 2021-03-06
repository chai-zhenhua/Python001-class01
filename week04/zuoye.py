import pandas as pd
import numpy as np

data = pd.DataFrame({
    "id": [x for x in np.random.randint(500, 1500, 20)],
    "age": [y for y in np.random.randint(25, 35, 20)],
    "order_id": [z for z in np.random.randint(1000, 1020, 20)]
})

# SELECT * FROM data;
print(data)

# SELECT * FROM data LIMIT(10);
print(data[:10])

# SELECT id FROM data;
print(data[['id']])

# SELECT COUNT(id) FROM data;
print(data['id'].count())

# SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id'] < 1000) & (data['age'] < 30)])

table1 = pd.DataFrame({
    "id": [x for x in np.random.randint(500, 1500, 20)],
    "age": [y for y in np.random.randint(25, 35, 20)],
    "order_id": [z for z in np.random.randint(1000, 1020, 20)]
})

table2 = pd.DataFrame({
    "id": [x for x in np.random.randint(500, 1500, 20)],
    "age": [y for y in np.random.randint(25, 35, 20)],
    "order_id": [z for z in np.random.randint(1000, 1020, 20)]
})

# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1.groupby('id').agg({'order_id': pd.Series.unique})

# SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1, table2, on='id')

# SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2])

# DELETE FROM table1 WHERE id=10;
table1 = table1[table1['id'] == 10]

# ALTER TABLE table1 DROP COLUMN column_name;
table1.drop(columns=['id'], axis=1)