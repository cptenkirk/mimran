import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Daten erstellen
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

# Modell erstellen und trainieren
model = LinearRegression()
model.fit(x, y)

# Vorhersagen treffen
y_pred = model.predict(x)

# Visualisierung
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()

# Modell-Parameter
print('Steigung:', model.coef_)
print('Achsenabschnitt:', model.intercept_)