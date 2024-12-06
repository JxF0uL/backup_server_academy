document.querySelectorAll('.botao-card').forEach((item,index) => { 
    document.querySelectorAll('.botao-card')[index].addEventListener('click', () => {

        for(var i = 0; i < document.querySelectorAll('.botao-card').length; i++) {
            if(i == index) {
                document.querySelectorAll('.pratica-card')[i].classList.add('ativo')
                document.querySelectorAll('.botao-card')[i].classList.add('ativo')
            } else {
                document.querySelectorAll('.pratica-card')[i].classList.remove('ativo')
                document.querySelectorAll('.botao-card')[i].classList.remove('ativo')
            }
        }
        
    })
})