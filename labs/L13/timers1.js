function loop(i, str) {
    if (i > 0) {
        console.log("\033c");
        console.log(str);
        setTimeout(function() { loop(i - 1, str + "*"); }, 100);
    } else {
        console.log("all done!");
    }
}

loop(20, "*");
