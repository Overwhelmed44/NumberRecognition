window.onload = () => {
    const shape = [28, 28];
    const canvas = document.getElementById('canvas');
    const clear = document.getElementById('clear');
    var predictions = document.getElementById('predictions');
    var layers = [];
    var layer;
    var child;
    var mouseDown = false;

    for (let n = 0; n < shape[0]; n++) {
        children = [];
        layer = document.createElement('div');
        layer.classList.add('layer')
        for (let m = 0; m < shape[1]; m++) {
            const child = document.createElement('div');
            child.classList.add(['p']);

            layer.appendChild(child);
        }
        layers.push(layer);
        canvas.appendChild(layer);
    }

    for (let n = 0; n < 10; n++) {
        child = document.createElement('p');
        child.innerHTML = `${n} = 0.0`;
        predictions.appendChild(child);
    }
    child = document.createElement('p');
    child.innerHTML = 'Prediction: -';
    child.style.fontWeight = '600';
    predictions.appendChild(child);

    const socket = new WebSocket('ws://' + window.location.host + '/ws');

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
        const prediction = JSON.parse(message.data);
        for (let n = 0; n < 10; n++) {
            predictions.children[n].innerHTML = `${n} = ${prediction[n]}`;
            predictions.children[n].style.fontWeight = '500';
        }
        const p = prediction['l'];
        predictions.children[10].innerHTML = `Prediction: ${p}`;
        predictions.children[p].style.fontWeight = '600';
    }

    canvas.addEventListener('dragstart', (ev) => ev.preventDefault());
    canvas.addEventListener('dragend', (ev) => ev.preventDefault());

    clear.addEventListener('click', () => {
        for (const layer of layers) {
            for (const pixel of layer.children) {
                pixel.classList.remove('f');
            }
        }
        var c;
        for (let n = 0; n < 10; n++) {
            c = predictions.children[n];
            c.innerHTML = `${n} = 0.0`;
            c.style.fontWeight = '500';
        }
        predictions.children[10].innerHTML = 'Prediction: -';
        socket.send(new Uint8Array(0));
    })
}