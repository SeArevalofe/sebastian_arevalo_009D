document.addEventListener('DOMContentLoaded', () => {
    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const cartItemsElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    let total = 0;
  
    cartItems.forEach(item => {
      const li = document.createElement('li');
      li.classList.add('list-group-item');
      li.textContent = `${item.name} - ${item.price}$`;
      cartItemsElement.appendChild(li);
      total += item.price;
    });
  
    cartTotalElement.textContent = total;
  });