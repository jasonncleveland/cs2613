function animate(iterations) {
    let i = 0;
    let str = "";
    let timer = null;

    function frame() {
        str += "*";
        i++;
        console.log("\033c");
        console.log(str);
        if (i >= iterations) {
            clearInterval(timer);
            console.log("all done!");
        }
    }

    timer = setInterval(frame, 300);
}

animate(20);
