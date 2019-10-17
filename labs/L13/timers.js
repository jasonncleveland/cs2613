let str = "";

for (let i = 0; i < 60; i++) {
    console.log("\033c");
    str += "*";
    console.log(str);
}

console.log("all done!");
