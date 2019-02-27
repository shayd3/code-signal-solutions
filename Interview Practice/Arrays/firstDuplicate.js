function firstDuplicate(arr) {
    var cache = {}
    for (let item of arr) {
        if (cache[item]) {
            return item;
        } else {
            cache[item] = item;
        }
    }
    return -1
}
