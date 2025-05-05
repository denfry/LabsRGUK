# Импорт библиотек
import numpy as np
from IPython.core.display_functions import display
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from mlxtend.plotting import plot_decision_regions
from sklearn.tree import export_graphviz
from pydotplus import graph_from_dot_data
from IPython.display import Image

# Загрузка данных
iris = load_iris()
X = iris.data[:, [2, 3]]  # petal_length, petal_width
y = iris.target

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Эксперименты
results = []
for max_depth in [3, 5]:
    for criterion in ['gini', 'entropy']:
        # Создание и обучение модели
        tree = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=0)
        tree.fit(X_train, y_train)

        # Оценка
        y_pred = tree.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        # Сохранение результатов
        results.append({
            'max_depth': max_depth,
            'criterion': criterion,
            'accuracy': accuracy,
            'confusion_matrix': cm
        })

        # Визуализация границ
        plt.figure(figsize=(8, 6))
        plot_decision_regions(X_test, y_test.astype(np.int32), clf=tree, legend=2)
        plt.xlabel('petal_length')
        plt.ylabel('petal_width')
        plt.title(f'Границы (max_depth={max_depth}, criterion={criterion})')
        plt.show()

        # Визуализация дерева (только для max_depth=3, criterion='gini') без сохранения в файл
        if max_depth == 3 and criterion == 'gini':
            dot_data = export_graphviz(tree, out_file=None, feature_names=['petal_length', 'petal_width'],
                                       class_names=iris.target_names, filled=True)
            graph = graph_from_dot_data(dot_data)
            # Конвертация графа в PNG и отображение
            display(Image(graph.create_png()))

# Вывод результатов
print("Результаты эксперимента:")
print("| max_depth | criterion | accuracy | confusion_matrix |")
print("|-----------|-----------|----------|------------------|")
for result in results:
    print(
        f"| {result['max_depth']} | {result['criterion']} | {result['accuracy']:.3f} | {result['confusion_matrix'].flatten()} |")

# Анализ
print("\nСравнительный анализ:")
print("- max_depth=3: упрощает модель, снижает переобучение.")
print("- max_depth=5: повышает точность, но увеличивает риск переобучения.")
print("- 'gini' и 'entropy': схожие результаты, 'entropy' лучше для сложных данных.")
