const village = require("./village");

function measureRobot(state, robot, memory) {
    for (let turn = 0;; turn++) {
        if (state.parcels.length == 0) {
            return turn;
        }
        let action = robot(state, memory);
        state = state.move(action.direction);
        memory = action.memory;
    }
}

function compareRobots(robot1, memory1, robot2, memory2) {
    // your code goes here
    const num_tests = 5;
    let average1 = 0;
    let average2 = 0;

    for (let i = 0; i < num_tests; i++) {
        const states = village.VillageState.random();
        average1 += measureRobot(states, robot1, memory1);
        average2 += measureRobot(states, robot2, memory2);
    }

    console.log(`Robot 1 Average: ${average1 / num_tests} turns`);
    console.log(`Robot 2 Average: ${average2 / num_tests} turns`);
}

compareRobots(village.routeRobot, [], village.randomRobot, []);