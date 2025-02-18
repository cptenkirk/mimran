let allWords = [
    {word: 'Welche  4-Phasen-Modelle gibt es beim Projektmanagement?', definition: 'Projektdefinition, Projektplanung, Projektdurchführung und Controlling und Projektabschluss.'},

    {word: 'Was beschreibt das 4-Phasen-Modell?', 


    definition: 'Sie beschreibt die grundlegenden Phasen beim Projektmanagement, sie ist eines der ersten grundlegenden Managementaufgaben in einem Projekt.'},

    {word: 'Was bezeichnet man als kritischer Pfad beim Netzplanen?', 
      
      definition: 'Kritischer Pfad auch als kritischer Weg bezeichnet, ist der Anfang bis zum Ende aller Netzpläne, auf dem die Summe aller Pufferzeiten minimal oder Null wird. Die Gesamtprojektdauer wird durch den kritischen Pfad bestimmt. '},

    {word: 'Was versteht man unter Forming im Projektmanagement?', 
      
      definition: 'Sie ist die Orientirungsphase, in der sich alle Gruppenmitglieder kennenlernen. In dieser Phase sind noch einiges unklar und die Aufgaben und Rollen sind noch nicht verteilt.'},

    {word: 'Was versteht man unter Storming im Projektmanagement?', 
      
      definition: 'Ist die Nahkampfphase, wo die Ziele nach und nach klarer werden. Eine Rollenverteilung wird gebildet und die Teammitglieder kommen sich näher. Der Projektleiter fungiert als Antreiber.'},

    {word: 'Was versteht man unter Norming im Projektmanagement?', 
      
      definition: 'Ist die Organisationsphase, in der klare Strukturen und Regeln im Team gebildet werden. Es werden wichtige Fragen für die Zielerreichung gestellt und die Einhaltung der Regeln werden definiert. die Projektleiter übertragen Mitarbeitern Aufgaben und besprechen diese.'},

    {word: 'Was versteht man unter Performing im Projektmanagement?',
      
      definition: 'Sie ist die Hochleistungsphase, in der die Selbstorganisation des Teams im Vordergrund steht. Das Team wird zunehmend kreativer und flexibler. Die Aufgaben der Mitglieder wurden kommuniziert. Die Leistungen werden jetzt eigenständig durchgeführt.'},


]

let frageElement = document.getElementById("frage"); // Globale Variable
let definitionElement = document.getElementById("definition"); // Globale Variable
let cardposElement = document.getElementById("cardpos"); // Globale Variable 

function updateWord(word, def, position = 1) {
    frageElement.textContent = word;
    definitionElement.textContent = def;
    cardposElement.textContent = position;
}


/* function createModal(type){
meinekarten.style.display = 'block';
if (type == 'add') {
    meinekarten.innerHTML = `
    <div class="karteikarten">
        <span id="closecard" class="close">&times;</span>
        Neue Frage: <input id="neu">
        Neue Auflösung: <input id="neuedef">
        <button id="save" type="submit">Save New Word</button>
      </div>`;

      closecard.onclick = () => meinekarten.style.display = 'none'
      save.onclick = function() {
        allWords.push({word: neu.value, definition: neuedef.value})
        meinekarten.style.display = 'none'
        updateWord(allWords[allWords.length -1].word, allWords[allWords.length -1].definition, allWords.length)
      };
}


if (type == 'edit') {
    meinekarten.innerHTML = 
    `
    <div class="karteikarten">
      <span id="closecard" class="close">&times;</span>
      Aktuelle Frage: <input id="aktuellefrage">
      Auflösung: <input id="aktuelledef">
      <button id="updatefrage" type="submit">Update</button>
    </div>
    ` 
    closecard.onclick = () => meinekarten.style.display = 'none'
    aktuellefrage.value = frage.textContent
    aktuelledef.value = definition.textContent
    updatefrage.onclick = function() {
       meinekarten.style.display = 'none'
       const index = cardpos.textContent - 1
       allWords[index] = {word: aktuellefrage.value, definition: aktuelledef.value}
       updateWord( allWords[index].word,  allWords[index].definition, index + 1)
    }
 }
}
 */
function shuffle() {
    allWords = allWords.sort((a,b) => 0.5 - Math.random())
    updateWord(allWords[0].word, allWords[0].definition)
}

document.addEventListener('DOMContentLoaded', (event) => {
  if (allWords.length > 0) {
      updateWord(allWords[0].word, allWords[0].definition, 1);
  }
});