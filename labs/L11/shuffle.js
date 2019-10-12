function shuffle (array) {
    for (let dest = array.length - 1; dest > 0; dest--) {
        let source = Math.floor(Math.random() * dest);
        let tmp = array[dest];
        array[dest] = array[source];
        array[source] = tmp;
    }
}

exports.shuffle = shuffle;
