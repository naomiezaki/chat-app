let socket = io.connect('http://'+document.domain+':'+location.port);

// let d = new Date(year, month, day, hours, minutes);



socket.on('connect', ()=>{
    socket.emit('my event', {
        data:'User Connected'
    })
    let form = $('form').on('submit',(e)=>{
        e.preventDefault()
        let user_name = localStorage.getItem('username')
        let user_input = $('input.message').val()
        // let msg_date = d.getDate();
        socket.emit('my event', {
            user_name:user_name,
            message:user_input
        })
        $('input.message').val('').focus()
    })
})

socket.on('my response', (msg)=>{
    console.log(msg)
    if(typeof msg.user_name !== 'undefined'){
        $('h3').remove()
        $('div.message_holder').append('<div><b style"color:#000">'+msg.user_name+':'+'</b> &nbsp &nbsp'+'<label class="message-bubble">'+msg.message+'</label>'+'</div>')                    
    }
})