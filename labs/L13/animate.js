const village = require("./village");

function animate(state, robot, memory, count) {
    // your code goes here
    if (state.parcels.length == 0) {
        console.log(`Done in ${count} turns`);
    } else {
        let action = robot(state, memory);
        state = state.move(action.direction);
        memory = action.memory;
        console.log("\033c");
        console.log(state.toString());
        setTimeout(function () { animate(state, robot, memory, count + 1); }, 1000);
    }
}

animate(village.VillageState.random(), village.randomRobot, [], 0);