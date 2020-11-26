function clear(arr) {
    if (arr === undefined)
        return 0;

    let out = [];
    arr.reverse().forEach(item => {
        if (typeof item === "string")
            item = item.trim();

        if ((typeof item === "string" && item.length >= 1) || typeof item === "number")
            out.push(typeof item === "string" ? item.substr(0,2).toUpperCase() : item);
    })

    return out;
}