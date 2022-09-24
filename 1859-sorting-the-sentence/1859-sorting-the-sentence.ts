function sortSentence(sentence: string): string {
    const words = sentence.split(' ')
    let sortedWords: string[] = []
    let sortedSentence = ''

    words.forEach(word => {
        const index = parseInt(word.charAt(word.length - 1))
        const onlyWord = word.slice(0, -1)
        sortedWords[index] = onlyWord;
    })
    sortedWords.forEach((word,index) => {
        if(index === (sortedWords.length - 1)) sortedSentence = sortedSentence.concat(word)
        else sortedSentence = sortedSentence.concat(word + ' ')
    })
    
    return sortedSentence;
};