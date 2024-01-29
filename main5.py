import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

# print(df.head())

# print(df.shape)
# print(df.columns)
# print(df.dtypes)

filtered_df = df['DEPARTMENT_ID'].value_counts
# print(filtered_df)

average_salary_by_departments = df.groupby('DEPARTMENT_ID')['SALARY'].mean().round(2)
# print(average_salary_by_departments)

employees_by_salary = df[df['SALARY']>3000]
# print(employees_by_salary)

# plt.figure(figsize = (12, 6))
# average_salary_by_departments.plot(kind='bar')
# plt.title('vidutine alga pagal skyriu')
# plt.xlabel('skyrius')
# plt.ylabel('vidutinis atlyginimas')
# plt.xticks(rotation=0)
# plt.show()


df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'], format= '%d-%b-%y')
df['year'] = df['HIRE_DATE'].dt.year
employee_count_by_year = df.groupby('year').size()

plt.figure(figsize = (12, 6))
employee_count_by_year.plot(kind='line')
plt.title('darbuotoju augimo grafikas')
plt.xlabel('metai')
plt.ylabel('darbuotojai')
#plt.xticks(rotation=0)
plt.grid(True)
plt.show()
