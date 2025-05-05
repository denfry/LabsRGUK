# Импорт библиотек
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC
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
for C in [0.1, 1, 10]:
    for kernel, gamma in [('linear', None), ('rbf', 100.0)]:
        # Создание и обучение модели
        svm = SVC(C=C, kernel=kernel, gamma=gamma if gamma else 'scale', random_state=42)
        svm.fit(X_train, y_train)

        # Оценка
        y_pred = svm.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        # Сохранение результатов
        results.append({
            'C': C,
            'kernel': kernel,
            'gamma': gamma if gamma else 'scale',
            'accuracy': accuracy,
            'confusion_matrix': cm
        })

        # Визуализация границ
        plt.figure(figsize=(8, 6))
        plot_decision_regions(X_test, y_test.astype(np.int32), clf=svm, legend=2)
        plt.xlabel('petal_length (scaled)')
        plt.ylabel('petal_width (scaled)')
        plt.title(f'Границы SVM (C={C}, kernel={kernel}, gamma={gamma if gamma else "scale"})')
        plt.show()

# Вывод результатов
print("Результаты эксперимента:")
print("| C | kernel | gamma | accuracy | confusion_matrix |")
print("|---|--------|-------|----------|------------------|")
for result in results:
    print(
        f"| {result['C']} | {result['kernel']} | {result['gamma']} | {result['accuracy']:.3f} | {result['confusion_matrix'].flatten()} |")

# Анализ
print("\nСравнительный анализ:")
print("- C=0.1: большой зазор, ниже точность.")
print("- C=10: малый зазор, выше точность, риск переобучения.")
print("- linear: для линейно разделимых данных.")
print("- rbf (gamma=100.0): чувствителен, риск переобучения.")
