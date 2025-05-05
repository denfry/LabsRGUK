# Импорт библиотек
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Создание синтетических данных
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Создание и обучение модели
model = LogisticRegression(random_state=42)
model.fit(x, y)

# Получение коэффициентов
print("Свободный коэффициент:", model.intercept_)
print("Коэффициент при x:", model.coef_)

# Предсказание вероятностей и классов
probabilities = np.round(model.predict_proba(x), 2)
print("Вероятности (0, 1):", probabilities)
predictions = model.predict(x)
print("Предсказанные классы:", predictions)

# Оценка точности
accuracy = model.score(x, y)
print("Точность модели:", accuracy)

# Матрица ошибок
cm = confusion_matrix(y, predictions)
print("Матрица ошибок:\n", cm)

# Визуализация матрицы ошибок
plt.figure(figsize=(6, 4))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Матрица ошибок')
plt.colorbar()
plt.xlabel('Предсказанные классы')
plt.ylabel('Фактические классы')
plt.xticks([0, 1], ['0', '1'])
plt.yticks([0, 1], ['0', '1'])
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha='center', va='center')
plt.show()

# Визуализация данных и разделяющей линии
w0 = model.intercept_[0]
w1 = model.coef_[0][0]
m = -w1 / 1  # Наклон
c = -w0 / 1  # Сдвиг
x_line = np.array([min(x), max(x)])
y_line = m * x_line + c

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=y, cmap='bwr', label='Данные')
plt.plot(x_line, y_line, 'k-', label='Разделяющая линия')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Разделяющая линия логистической регрессии')
plt.legend()
plt.show()
