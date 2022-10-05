//Código de troca de frase no HTML conforme a pontuação
let div_resultado = document.getElementById('resultado').innerHTML;
div_resultado = div_resultado.substring(21, 26);

if (parseFloat(div_resultado) < 2.99) {
    const text = 'Iniciante';
    document.querySelector('.result-text').innerHTML = text;
}
else if ((parseFloat(div_resultado) >= 3.00) && (parseFloat(div_resultado) <= 4.99)){
    const text = 'Básico';
    document.querySelector('.result-text').innerHTML = text;
}
else if ((parseFloat(div_resultado) >= 5.00) && (parseFloat(div_resultado) <= 6.99)){
    const text = 'Intermediário';
    document.querySelector('.result-text').innerHTML = text;
}
else if ((parseFloat(div_resultado) >= 7.00) && (parseFloat(div_resultado) <= 8.99)){
    const text = 'Intermediário Superior';
    document.querySelector('.result-text').innerHTML = text;
}
else if (parseFloat(div_resultado) >= 9.00){
    const text = 'Avançado';
    document.querySelector('.result-text').innerHTML = text;
}