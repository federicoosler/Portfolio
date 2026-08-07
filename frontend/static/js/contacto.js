const msg = document.querySelector('.mensaje-enviado');

if(msg){
  setTimeout(() => {
    msg.classList.add('oculto');
    setTimeout(() => {
      msg.style.display = 'none';
    }, 300);
  }, 3000);
};