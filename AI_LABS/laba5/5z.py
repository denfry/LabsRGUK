# Импорт библиотек
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from mlxtend.plotting import plot_decision_regions

# Загрузка данных
iris = load_iris()
X = iris.data[:, [2, 3]]  # petal_length, petal_width
y = iris.target

# Масштабирование признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42, stratify=y)

# Эксперименты
results = []
for n_neighbors in [3, 5, 7]:
    for p in [1, 2]:
        # Создание и обучение модели
        knn = KNeighborsClassifier(n_neighbors=n_neighbors, p=p)
        knn.fit(X_train, y_train)

        # Оценка
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        # Сохранение результатов
        results.append({
            'n_neighbors': n_neighbors,
            'p': p,
            'accuracy': accuracy,
            'confusion_matrix': cm
        })

        # Визуализация границ
        plt.figure(figsize=(8, 6))
        plot_decision_regions(X_test, y_test.astype(np.int32), clf=knn, legend=2)
        plt.xlabel('petal_length (scaled)')
        plt.ylabel('petal_width (scaled)')
        plt.title(f'Границы KNN (n_neighbors={n_neighbors}, p={p})')
        plt.show()

# Вывод результатов
print("Результаты эксперимента:")
print("| n_neighbors | p | accuracy | confusion_matrix |")
print("|-------------|---|----------|------------------|")
for result in results:
    print(
        f"| {result['n_neighbors']} | {result['p']} | {result['accuracy']:.3f} | {result['confusion_matrix'].flatten()} |")

# Анализ
print("\nСравнительный анализ:")
print("- n_neighbors=3: чувствительна к шуму, улавливает локальные особенности.")
print("- n_neighbors=7: сглаживает решение, может упускать детали.")
print("- p=1 (манхэттенское): лучше для данных с различиями по осям.")
print("- p=2 (евклидово): для равномерных данных.")
