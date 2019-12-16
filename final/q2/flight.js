class Flight {

    constructor(cost, time) {
        this.cost = cost;
        this.time = time;
    }

    compare(other) {
        if (other == null || other.cost == null || other.time == null) {
            console.log("Invalid Flight given. Valid Flight must contain a cost and time.");
            return 1;
        }

        if (this.cost > other.cost) {
            return 1;
        } else if (this.cost < other.cost) {
            return -1;
        } else {
            if (this.time > other.time) {
                return 1;
            } else if (this.time < other.time) {
                return -1;
            } else {
                return 0;
            }
        }
    }
}

module.exports.Flight = Flight;
