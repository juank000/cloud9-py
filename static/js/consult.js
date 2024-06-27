const msg = document.getElementById('mssg')
const img = document.querySelector('.image')
const txt = document.getElementById('txt-output')

function clearInfo() {
    window.location.reload()
}

const consultUser_ALT = _ => {
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

const consultUser = _ => {
    const idInput = document.getElementById('id_num').value
    const userObj = {"id":idInput}
    
    fetch('/consult_user', {
        'method':'post', // Do not use GET with sensitive data
        'headers':
        {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify(userObj)
    })
    .then(res => res.json())
    .then(data => {
        //alert(data.status) // status variable in control.py
        alert("Name fetched from the db: " + data.name) // name variable in control.py
    })
    .catch(err => alert("Error" + err))
}