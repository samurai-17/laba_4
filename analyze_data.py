import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
# Загрузка набора данных
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = pd.read_csv(url)

# Просмотр первых нескольких строк
print(data.head())

# Проверка на пропущенные значения
print(data.isnull().sum())

# Заполняем пропуски в возрасте средним значением
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Преобразуем категориальные переменные
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)


# Установим стиль графиков
sns.set(style="whitegrid")

# Распределение возраста
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Распределение возраста пассажиров')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

# Процент выживаемости по классам
plt.figure(figsize=(8, 5))
sns.barplot(x='Pclass', y='Survived', data=data, ci=None)
plt.title('Процент выживаемости по классам')
plt.xlabel('Класс')
plt.ylabel('Процент выживания')
plt.show()


# Создаем таблицу сопряженности
contingency_table = pd.crosstab(data['Survived'], data['Sex_male'])

# Применяем тест хи-квадрат
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f'Статистика хи-квадрат: {chi2}')
print(f'p-значение: {p}')

# Интерпретация
alpha = 0.05
if p < alpha:
    print("Мы отклоняем нулевую гипотезу. Существуют статистически значимые различия в выживаемости между мужчинами и женщинами.")
else:
    print("Мы не отклоняем нулевую гипотезу. Нет статистически значимых различий в выживаемости между мужчинами и женщинами.")