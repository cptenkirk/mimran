/* Hier wird die JavaScript Funktion eingegeben*/
function appendOperation(operation /*hier wird eine Variable definiert, z.B. 1,2,3*/){ // hier wird mit dem JS auf das Element resultArea zugegriffen. 
    document/*dieses Dokument*/.getElementById/*Zugriff auf das Element resultArea*/('resultArea').innerHTML /* innerer HTML-Teil mit += anhängen*/ += operation /*von der Variable operation anhängen*/; 
  }

  /* Deklaration ergebnis-Funktion */

    function ergebnis() /* Durch den Button"="  */{
        let container = document.getElementById('resultArea');
        let ergebnis = eval(container.innerHTML);
        container.innerHTML = ergebnis.toFixed(8);
    }

        function Del() {
            let container = document.getElementById('resultArea');
            if (container.innerHTML.endsWith(' ')) { container.innerHTML = container.innerHTML.slice(0,-3); /* durch slice 0,-3 werden 3 Zeichen gelöscht */} else {
            container.innerHTML = container.innerHTML.slice(0,-1);  /* durch slice 0,-1 wird die letzte Zahl gelöscht */}
        }

            function erase() { //Funktion um den gesamten Inhalt zu löschen
                document.getElementById('resultArea').innerHTML = '';
            }

            document.addEventListener('DOMContentLoaded', function() {
                // Deine Funktionen hier
            });