var canvas;
var clear ;
var set;
var main;
var modal ;
var width ;
var height;
var predic;
var layers = [];
var layer;
var predictions;
var mouseDown = false;
var socket;


function mainF() {
    for (let n = 0; n < height; n++) {
        children = [];
        layer = document.createElement('div');
        layer.classList.add('layer')
        for (let m = 0; m < width; m++) {
            const child = document.createElement('div');
            child.classList.add(['p']);

            layer.appendChild(child);
        }
        layers.push(layer);
        canvas.appendChild(layer);
    }

    document.addEventListener('mousedown', () => mouseDown = true);
    document.addEventListener('mouseup', () => mouseDown = false);

    canvas.addEventListener('mouseover', async (ev) => {
        if (mouseDown) {
            const target = ev.target;
            target.classList.add('f')

            const parent = target.parentElement;
            const y = [...parent.parentElement.children].indexOf(parent);
            const x = [...parent.children].indexOf(target); 
            socket.send(new Uint8Array([y, x]));
        }
    })

    socket.onmessage = async (message) => {
        const prediction = message.data;
        predictions.children[0].innerHTML = `Prediction: ${prediction}`;
    }

    canvas.addEventListener('dragstart', (ev) => ev.preventDefault());
    canvas.addEventListener('dragend', (ev) => ev.preventDefault());

    clear.addEventListener('click', () => {
        for (const layer of layers) {
            for (const pixel of layer.children) {
                pixel.classList.remove('f');
            }
        }
        predictions.children[0].innerHTML = 'Prediction: -';
        socket.send(new Uint8Array(0));
    })
}


window.onload = () => {
    canvas = document.getElementById('canvas');
    clear = document.getElementById('clear');
    set = document.getElementById('set');
    main = document.getElementById('main');
    modal = document.getElementById('modal');
    width = document.getElementById('width');
    height = document.getElementById('height');
    predictions = document.getElementById('predictions');
    socket = new WebSocket('ws://' + window.location.host + '/ws');
    
    set.addEventListener('click', () => {
        height = Math.min(60, parseInt(height.value));
        width = Math.min(120, parseInt(width.value));

        socket.send(new Uint8Array([height, width]))

        modal.style.display = 'none';
        main.style.display = 'block';

        mainF()
    });
}