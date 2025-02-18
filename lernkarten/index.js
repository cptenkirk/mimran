window.onload = function() {
    const firstWord = allWords[0];
    updateWord(firstWord.word, firstWord.definition);
};

document.onclick = function(e) {
    const target = e.target.id; 
    if (target == 'add') createModal('addWord');
        if(target == 'mix') shuffle();
            if(target == 'edit') createModal('edit');
};

rechts.onclick = function(){
    zeigen.style.display = 'unset';
    definition.style.display = 'none';
    let nextIndex = allWords.findIndex(obj => obj.word.toLowerCase() ==  frage.textContent.toLowerCase()) + 1;
    if(nextIndex == allWords.length) nextIndex = 0;
    updateWord(allWords[nextIndex].word, allWords[nextIndex].definition, nextIndex + 1);
}

links.onclick = function(){
    zeigen.style.display = 'unset';
    definition.style.display = 'none';
    let prevIndex = allWords.findIndex(obj => obj.word.toLowerCase() == frage.textContent.toLowerCase()) - 1;
    if(prevIndex == -1) prevIndex = allWords.length - 1;
    updateWord(allWords[prevIndex].word, allWords[prevIndex].definition, prevIndex + 1);
}

zeigen.onclick = function(){
    zeigen.style.display = 'none';
    definition.style.display = 'block';
}

erase.onclick = function(){
    const index = cardpos.textContent - 1
    allWords.splice(index, 1)
    updateWord(allWords[0].word,allWords[0].definition)
}