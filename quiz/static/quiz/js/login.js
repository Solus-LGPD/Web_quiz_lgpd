//Tratamento de login
const result = document.getElementById('fail-msg').innerHTML;
const divResult = document.getElementById('fail-msg');

    if(result == '1'){
        divResult.style.display = 'flex' ;
        const textSuccess = 'E-mail/Senha inválido';
        divResult.innerHTML = textSuccess;
    }

