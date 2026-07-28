const msg = document.querySelector('.mensaje-enviado');
setTimeout(() => {
  msg.classList.add('oculto');
  setTimeout(() => {
    msg.style.display = 'none';
  }, 300);
}, 3000);