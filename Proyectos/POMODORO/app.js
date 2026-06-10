



let minutos = 25;
let segundos = 0;

console.log(minutos)
console.log(segundos)

let temporizador = document.getElementById('temporizador');

console.log(temporizador)


let botonIniciar = document.getElementById('iniciar');
let intervalo;
let botonPausar = document.getElementById('pausar');
let botonReiniciar = document.getElementById('reiniciar');

botonIniciar.addEventListener('click', function () {

    intervalo = setInterval(function () {
        if (segundos === 0) {
            minutos -= 1;
            segundos = 59;
        } else {
            segundos -= 1;
        }

        temporizador.textContent = `${minutos}:${segundos}`;
    }, 1000);

    botonPausar.addEventListener('click', function () {
    clearInterval(intervalo);

    botonReiniciar.addEventListener('click', function () {
    clearInterval(intervalo);

    minutos = 25;
    segundos = 0;

    temporizador.textContent = '25:00';
});
});
});