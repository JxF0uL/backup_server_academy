function menuShow() {
    let menu = document.querySelectorAll('.menu')[0]
    
    if(menu.classList.contains('ativo')) {
        menu.classList.remove('ativo')
        document.querySelectorAll('.cabecalho')[0].classList.remove('ativo')

    } else {
        menu.classList.add('ativo')
        document.querySelectorAll('.cabecalho')[0].classList.add('ativo')
    }
}


