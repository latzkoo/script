function matek(param) {
    if (param === undefined)
        return 0;
    else if (typeof param === "string")
        return 1;
    else if (typeof param === "number" && Number.isInteger(param)) {
        if (param % 2 === 0)
            return param ** param;
        else
            return (param - 1) ** 2;
    }

    return null;
}