function popUpShow(class_name) {
    let popUp = document.getElementsByClassName(`${class_name}`)[0]
    
    if(popUp.classList.contains('ativo')) {
        popUp.classList.remove('ativo')
    } else {
        popUp.classList.add('ativo')
    }
}
