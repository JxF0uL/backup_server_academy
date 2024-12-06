document.querySelectorAll('.botao-item').forEach((item,index) => { 
    document.querySelectorAll('.botao-item')[index].addEventListener('click', () => {
        for(var i = 0; i < document.querySelectorAll('.botao-item').length; i++) {
            if(i == index) {
                document.querySelectorAll('.card-depoimento')[i].classList.add('ativo')
                document.querySelectorAll('.botao-item')[i].classList.add('ativo')
            } else {
                document.querySelectorAll('.card-depoimento')[i].classList.remove('ativo')
                document.querySelectorAll('.botao-item')[i].classList.remove('ativo')
            }
        }
        
    })
})