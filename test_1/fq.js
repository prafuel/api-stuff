import fetch from 'node-fetch';

let url = "http://127.0.0.1:8000/"
const name = "bridge";
const path = "./bridge.jpg";

const sendData = async (name,path) => {

    const data = {
        "name": name,
        "path": path
    }

    const res = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    return res.json();
}

const res = sendData(name,path);

res.then((value)=>{
    console.log(value);
})