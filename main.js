 /* validacion registro de usuario*/ 
$(document).ready(function(){
  $("#form1").submit(function(event){
    var name = $("#name").val();
    var lastName = $("#lastName").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var isValid = true; 
    if(name == "") {
      $("#advertenciaNombre").text("Por favor, ingrese su nombre.");
      isValid = false;
    } else {
      $("#advertenciaNombre").text(""); 
    }

    
    if(lastName == "") {
      $("#advertenciaApellido").text("Por favor, ingrese su apellido.");
      isValid = false;
    } else {
      $("#advertenciaApellido").text(""); 
    }

    
    if(email == "") {
      $("#advertenciaCorreo").text("Por favor, ingrese su correo electrónico.");
      isValid = false;
    } else {
      $("#advertenciaCorreo").text(""); 
    }

    
    if(password == "") {
      $("#contraseñaAdvertencia").text("Por favor, ingrese su contraseña.");
      isValid = false;
    } else {
      $("#contraseñaAdvertencia").text("");
    }

    
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email != "" && !emailPattern.test(email)) {
      $("#emailWarning").text("Por favor, ingrese un correo electrónico válido.");
      isValid = false;
    }

  
    if(!isValid) {
      event.preventDefault();
    } else {
      alert("Registrado con exito");
    }
  });
});






 /* Aqui hay una funcion que consiste en añadir productos al carrito*/ 


document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', (e) => {
      const name = e.target.getAttribute('data-name');
      const price = parseFloat(e.target.getAttribute('data-price'));

      const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
      cartItems.push({ name, price });
      localStorage.setItem('cartItems', JSON.stringify(cartItems));

      alert(`${name} ha sido añadido al carrito`);
    });
  });
});







