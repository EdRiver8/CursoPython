const userForm = document.getElementById("userForm");

let users = [];

/** al cargar la pagina, muestre los datos de la db */
window.addEventListener("DOMContentLoaded", async () => {
  //console.log("loaded");
  const response = await fetch("/api/users");
  const data = await response.json();
  //console.log(data);// trae la info de la db en formato objeto
  users = data; // arreglo de objetos
  renderUser(users);
});

/** Enviar datos ingresados y actualizar lista de datos */
userForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  //console.log(e);
  username = userForm[0].value;
  email = userForm["email"].value;
  password = userForm["password"].value;
  console.log(username, email, password);

  const response = await fetch("/api/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });

  const data = await response.json();
  console.log(data);

  //users.push(data); // guarda el nuevo user al final
  users.unshift(data); // guarda el nuevo user inicio
  renderUser(users); // actualiza lista de users

  userForm.reset(); // Limpiar datos del form
});

/**
 * Mostrar lista de datos ingresados en la db
 */
function renderUser(users) {
  //console.log(users);
  const userList = document.querySelector("#userList");
  //console.log(userList);
  userList.innerHTML = "";
  users.forEach((user) => {
    const userItem = document.createElement("li");
    userItem.classList = "list-group-item list-group-item-dark m-2";
    userItem.innerHTML = `
        <header class='d-flex justify-content-between align-items-center'>
            <h3>${user.username}</h3>
            <div>
                <button class='btn btn-danger btn-sm'>Delete</button>
                <button class='btn btn-primary btn-sm'>Edit</button>
            </div>
        </header>
        <p>${user.email}</p>
        <p class='text-truncate'>${user.password}</p>
    `;
    userList.append(userItem);
  });
}
