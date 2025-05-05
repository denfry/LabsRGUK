# Импорт библиотек
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import PolynomialFeatures
from scipy.stats import pearsonr

# Загрузка данных
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# Для бинарной классификации оставим два класса
binary_mask = y != 2
X_binary = X[binary_mask]
y_binary = y[binary_mask]

# Корреляционный анализ
correlations = []
for feature in X_binary.columns:
    corr, _ = pearsonr(X_binary[feature], y_binary)
    correlations.append((feature, abs(corr)))
correlations.sort(key=lambda x: x[1], reverse=True)
print("Наиболее коррелированные признаки:", correlations[:2])

# Выбор двух признаков
selected_features = [correlations[0][0], correlations[1][0]]
X_selected = X_binary[selected_features]

# Масштабирование признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_selected)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_binary, test_size=0.3, random_state=42)

# 2.1 Бинарная линейная классификация по двум признакам
model_2features = LogisticRegression(random_state=42)
model_2features.fit(X_train, y_train)
y_pred_2features = model_2features.predict(X_test)
accuracy_2features = accuracy_score(y_test, y_pred_2features)
cm_2features = confusion_matrix(y_test, y_pred_2features)
print("Точность (2 признака):", accuracy_2features)
print("Матрица ошибок (2 признака):\n", cm_2features)

# Визуализация матрицы ошибок
plt.figure(figsize=(6, 4))
plt.imshow(cm_2features, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Матрица ошибок (2 признака)')
plt.colorbar()
plt.xlabel('Предсказанные классы')
plt.ylabel('Фактические классы')
plt.xticks([0, 1], ['0', '1'])
plt.yticks([0, 1], ['0', '1'])
for i in range(cm_2features.shape[0]):
    for j in range(cm_2features.shape[1]):
        plt.text(j, i, cm_2features[i, j], ha='center', va='center')
plt.show()

# Визуализация разделяющей линии
w0 = model_2features.intercept_[0]
w1, w2 = model_2features.coef_[0]
m = -w1 / w2
c = -w0 / w2
x1_line = np.array([X_train[:, 0].min(), X_train[:, 0].max()])
x2_line = m * x1_line + c

plt.figure(figsize=(8, 6))
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', label='Обучающие данные')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='bwr', marker='x', label='Тестовые данные')
plt.plot(x1_line, x2_line, 'k-', label='Разделяющая линия')
plt.xlabel(selected_features[0])
plt.ylabel(selected_features[1])
plt.title('Разделяющая линия (2 признака)')
plt.legend()
plt.show()

# 2.2 Бинарная линейная классификация по всем признакам
X_all_scaled = scaler.fit_transform(X_binary)
X_train_all, X_test_all, y_train_all, y_test_all = train_test_split(X_all_scaled, y_binary, test_size=0.3,
                                                                    random_state=42)
model_all = LogisticRegression(random_state=42)
model_all.fit(X_train_all, y_train_all)
y_pred_all = model_all.predict(X_test_all)
accuracy_all = accuracy_score(y_test_all, y_pred_all)
cm_all = confusion_matrix(y_test_all, y_pred_all)
print("Точность (все признаки):", accuracy_all)
print("Матрица ошибок (все признаки):\n", cm_all)

# Визуализация матрицы ошибок
plt.figure(figsize=(6, 4))
plt.imshow(cm_all, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Матрица ошибок (все признаки)')
plt.colorbar()
plt.xlabel('Предсказанные классы')
plt.ylabel('Фактические классы')
plt.xticks([0, 1], ['0', '1'])
plt.yticks([0, 1], ['0', '1'])
for i in range(cm_all.shape[0]):
    for j in range(cm_all.shape[1]):
        plt.text(j, i, cm_all[i, j], ha='center', va='center')
plt.show()

# 2.3 Полиномиальная бинарная классификация
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_scaled)
X_train_poly, X_test_poly, y_train_poly, y_test_poly = train_test_split(X_poly, y_binary, test_size=0.3,
                                                                        random_state=42)
model_poly = LogisticRegression(random_state=42)
model_poly.fit(X_train_poly, y_train_poly)
y_pred_poly = model_poly.predict(X_test_poly)
accuracy_poly = accuracy_score(y_test_poly, y_pred_poly)
cm_poly = confusion_matrix(y_test_poly, y_pred_poly)
print("Точность (полиномиальная):", accuracy_poly)
print("Матрица ошибок (полиномиальная):\n", cm_poly)

# Визуализация матрицы ошибок
plt.figure(figsize=(6, 4))
plt.imshow(cm_poly, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Матрица ошибок (полиномиальная)')
plt.colorbar()
plt.xlabel('Предсказанные классы')
plt.ylabel('Фактические классы')
plt.xticks([0, 1], ['0', '1'])
plt.yticks([0, 1], ['0', '1'])
for i in range(cm_poly.shape[0]):
    for j in range(cm_poly.shape[1]):
        plt.text(j, i, cm_poly[i, j], ha='center', va='center')
plt.show()
