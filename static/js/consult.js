const msg = document.getElementById('mssg')
const img = document.querySelector('.image')
const txt = document.getElementById('txt-output')

function clearInfo() {
    window.location.reload()
}

const consultUser = _ => {
    const idInput = document.getElementById('id_num').value
    //console.log(idInput)
    idInput === "" ? [img.style.display = 'none',
                      txt.innerText = ``,
                      msg.innerText = 'User not found'] : [img.style.display = 'inline',
                                                           txt.innerText = `user ${idInput} info`,
                                                           msg.innerText = '']
    
    /*const consultBtn = document.getElementById('btn-consult')
    idInput != "" ? consultBtn.disabled = true : consultBtn.disabled = false*/
}