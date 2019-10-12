function timePlus(time1, time2) {
    let mins = (time1.mins + time2.mins) % 60;
    let hours = time1.hours + time2.hours + Math.floor((time1.mins + time2.mins) / 60);
    return { "hours": hours, "mins": mins };
}

console.log(timePlus({ hours: 10, mins: 30 }, { hours: 17, mins: 47 }));

function maketime(hours, mins) {
    let plus = function (other) {
        let raw = timePlus(this, other);
        return maketime(raw.hours, raw.mins);
    };

    return { "hours": hours, "mins": mins, "plus": plus };
}

let A = maketime(10, 30);
let B = maketime(17, 47);
let C = A.plus(B);
console.log(C);

let protoTime = {
    plus: function(other) {
        let raw = timePlus(this, other);
        return timeNew(raw.hours, raw.mins);
    }
};

function timeNew(hours, mins) {
    let obj = Object.create(protoTime);
    obj.hours = hours;
    obj.mins = mins;
    return obj;
}

let D = timeNew(21, 42);
let E = timeNew(17, 37);
let F = D.plus(E);
console.log(F);

function Time(hours, mins) {
    this.hours = hours;
    this.mins = mins;
}

Time.prototype.plus = function (other) {
    let raw = timePlus(this, other);
    return new Time(raw.hours, raw.mins);
};

let G = new Time(20, 59);
let H = new Time(11, 11);
let I = G.plus(H);
console.log(I);

class Time2 {
    constructor(hours, mins) {
        this.hours = hours;
        this.mins = mins;
    }

    plus(other) {
        let raw = timePlus(this, other);
        return new Time2(raw.hours, raw.mins);
    }
}

Time2;

let J = new Time2(5, 30);
let K = new Time2(11, 55);
let L = J.plus(K);
console.log(L);