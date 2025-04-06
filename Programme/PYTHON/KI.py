from sklearn.datasets import load_digits # Importierung der Funktion "load_digits" aus dem Modul "datasets" der Bibliothek von "scikit-learn". loas-digits ist eine Funktion, die den vorinstallierten Datensatz mit handgeschriebenen Ziffern lädt. Sklearn ist der bekannteste Bibliothek für KI Programmierung.



import matplotlib.pyplot as plt # "matplotlib.pyplot as plt" Hier wird das Modul pyplot aus der Bibliothek matplotlib importiert und gibt ihm das Alias plt (das "as" verkürzt die Schreibweise des Bibliotheks). 
# matplotlib ist eine Bibliothek für die Erstellung von Visualisierungen (Diagrammen, Grafiken usw.) In diesem Codeausschnitt wird matplotlib nich direkt für die Visualisierung verwendet.

import numpy as np # Dies importiert die Bibliothek "NumPy" und gibt ihr das Alias np. Sie wird häufig für die Arbeit mit Arrays und Matrizen verwendet, wie sie in Bilddaten des Datensatzes vorkommen.

digits = load_digits() # hier werden Datensätze aus der scikit-learn-Bibliothek geladen. Der Datensatz enthält handgeschriebene Bilder mit den Ziffern 0-9. 

print(digits["data"][0]) # Der gesamte Datensatz wird ausgegeben, der verschiedene Informationen enthält.

print(digits.keys()) # gibt die Schlüssel (Attribute) des Datensatzes aus, wie z.B. "data" Die Pixeldaten der Bilder und "target" wo die tatsächlichen Ziffern, die in Bildern dargestellt werden.

print(digits["target"][0]) # gibt die Zielvariable (die Tatsächliche Ziffer) des ersten Bildes im Datensatz aus.

print(digits["data"].shape) # gibt die Form des "data"-Arrays aus, was die Anzahl der Bilder und die Anzahl der Pixel pro Bild angibt.

def plot_image(pixelmap, ax = None): # dies ruft die plot-image-Funktion auf, um das erste Bild im Dtensatz anzuzeigen. Sie akzeptiert zwei Argumente, "pixelmap" dies ist der 1D Array, der Pixeldaten des anzuzeigenden Bildes enthält. ax: Dies ist ein optionales Argument, das ein Matplotlib-Axes-Objekt darstellt. Wenn es nicht angegeben wird, wird das aktuelle Axes-Objekt verwendet.
    if not ax: # Diese Zeilen prüfen, ob das ax-Argument angegeben wurde. 
        ax = plt.gca()# Wenn nicht, wird plt.gca() verwendet, um das aktuelle Axes-Objekte abzurufen. Dadurch kann die Funktion entweder mit einem vorhandenen Axes-Objekt oder ohne aufgerufen werden.

    ax.set_yticks([]);ax.set_xticks([]) # xticks Beschriftung der x Achse und yticks Beschriftung der y Achse. Sie entfernt die Beschriftung der y-Achse und der x-Achse. Dadurch wird ein sauberes Bild ohne Achsenmarkierung angezeigt.
    ax.imshow(np.reshape(pixelmap, (8,8))) # Die Kernzeile der Funktion. Sie nimmt das pixelmap-Array, formt es mit np.reshape in ein 8x8-Array um und zeigt es als Bild mit ax.imshow() an.

plot_image(digits["data"][0]) # Diese Zeile ruft die Funktion plot_image auf und übergibt das erste Bild aus dem digits-Dtensatz als pixelmap-Argument. Es wird davon ausgegangen, dass der digits-Datensatz ein Dictonary ist, das Bilddaten unter dem Schlüssel "data" enthält.
plt.show() # plt.show() diese Zeile zeigt das mit plot_image erstellte Bild an.

""" Machine Learning """

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(digits["data"], digits["target"], test_size=0.3)

X_test.shape 

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

clf.fit(X_train, Y_train)

n = 3

plot_image(X_test[n])
pred = clf.predict(X_test[n].reshape(1, -1))
pred[3]

from sklearn.metrics import accuracy_score as accus
pred = clf.predict(X_test)
accus(Y_test, pred)