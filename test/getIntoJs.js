
import fetch from "node-fetch"

const res = fetch("http://127.0.0.1:8080/time");

res.then((value1) => {
    return value1.json();
}).then((value2) => {
    // console.log(value2);

    for(let item of value2){
        console.log(item);
    }
})