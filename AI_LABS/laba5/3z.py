# Импорт библиотек
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from mlxtend.plotting import plot_decision_regions

# Генерация данных
np.random.seed(42)
class1_x = np.random.normal(loc=0, scale=1, size=(200, 2))
class1_y = np.zeros(200)
class2_x = np.random.normal(loc=2, scale=1, size=(100, 2))
class2_y = np.ones(100)
train_data = np.vstack((class1_x, class2_x))
train_labels = np.hstack((class1_y, class2_y))

# График разброса данных
plt.figure(figsize=(8, 6))
plt.scatter(train_data[:, 0], train_data[:, 1], c=train_labels, cmap='bwr')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Разброс данных')
plt.show()

# Эксперименты
results = []
for max_depth in [3, 5]:
    for criterion in ['gini', 'entropy']:
        # Создание и обучение модели
        tree = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=42)
        tree.fit(train_data, train_labels)

        # Оценка
        y_pred = tree.predict(train_data)
        accuracy = accuracy_score(train_labels, y_pred)
        cm = confusion_matrix(train_labels, y_pred)

        # Сохранение результатов
        results.append({
            'max_depth': max_depth,
            'criterion': criterion,
            'accuracy': accuracy,
            'confusion_matrix': cm
        })

        # Визуализация границ
        plt.figure(figsize=(8, 6))
        plot_decision_regions(train_data, train_labels.astype(np.int32), clf=tree, legend=2)
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.title(f'Границы (max_depth={max_depth}, criterion={criterion})')
        plt.show()

# Вывод результатов
print("Результаты эксперимента:")
print("| max_depth | criterion | accuracy | confusion_matrix |")
print("|-----------|-----------|----------|------------------|")
for result in results:
    print(
        f"| {result['max_depth']} | {result['criterion']} | {result['accuracy']:.3f} | {result['confusion_matrix'].flatten()} |")

# Анализ
print("\nСравнительный анализ:")
print("- max_depth=3: проще, меньше переобучение, но ниже точность.")
print("- max_depth=5: сложнее, выше точность, но риск переобучения.")
print("- 'gini': быстрее, 'entropy': точнее на сложных данных.")
