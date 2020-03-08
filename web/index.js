let text_field = document.querySelector('#text-field'),
    input = document.querySelector('input'),
    submit = document.querySelector('button'),
    btns = document.querySelectorAll('.btn');

input.disabled = true;

btns[0].addEventListener('click', (e) => {
    input.disabled = true;
    submit.innerHTML = "Показать водителей";
    submit.addEventListener('click', (e) => {
        eel.get_drivers()((ret)=>{
            text_field.innerHTML = ''
            ret.forEach(element => {
                text_field.innerHTML += `${element} <br><br>`;
            });
        });
    })
})

btns[1].addEventListener('click', (e) => {
    input.disabled = false;
    input.placeholder = 'Введите фамилию';
    submit.innerHTML = "Показать  водителя";
    submit.addEventListener('click', (e) => {
        eel.get_drivers(lname=input.value)((ret)=>{
            text_field.innerHTML = ''
            ret.forEach(element => {
                text_field.innerHTML += `${element} <br><br>`;
            });
        });
    })
})

btns[2].addEventListener('click', (e) => {
    input.disabled = true;
    submit.innerHTML = "Показать водителей по штрафам";
    submit.addEventListener('click', (e) => {
        eel.get_by_fine()((ret)=>{
            text_field.innerHTML = ''
            ret.forEach(element => {
                text_field.innerHTML += `${element} <br><br>`;
            });
        });
    })
})

btns[3].addEventListener('click', (e) => {

    input.disabled = true;
    submit.innerHTML = "Показать водителей по похвалам";
    submit.addEventListener('click', (e) => {
        eel.get_by_commendation()((ret)=>{
            text_field.innerHTML = ''
            ret.forEach(element => {
                text_field.innerHTML += `${element} <br><br>`;
            });
        });
    })
})

btns[4].addEventListener('click', (e) => {

    input.disabled = false;
    input.placeholder = 'Введите улицу';
    submit.innerHTML = "Показать водителя";
    submit.addEventListener('click', (e) => {
        eel.get_by_area(input.value)((ret)=>{
            text_field.innerHTML = ''
            ret.forEach(element => {
                text_field.innerHTML += `${element} <br><br>`;
            });
        });
    })
})

btns[5].addEventListener('click', (e) => {

    input.disabled = false;
    input.placeholder = 'Введите номер авто';
    submit.innerHTML = "Показать авто";
    submit.addEventListener('click', (e) => {
        console.log(`->${typeof(input.value)}`)
        let str 
        eel.get_auto_by_num(input.value)((ret)=>{
            console.log(`->${input.value}`)
            console.log(ret)
            text_field.innerHTML = `${ret} <br><br>`;
        });
    })
})
