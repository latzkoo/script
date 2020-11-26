class Nyuszi {
    constructor(repa = 0) {
        this._repa = repa;
        this.vendegek = [];
    }

    get repa() {
        return this._repa;
    }

    ultet(repa = 1) {
        this._repa += repa;
    }

    vendeg(nev) {
        if (typeof nev === "string")
            this.vendegek.push(nev);
    }

    etet() {
        while (this.repa >= 1 && this.vendegek.length >= 1) {
            this.vendegek.shift();
            this._repa--;
        }
    }
}