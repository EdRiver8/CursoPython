const userForm = document.getElementById("userForm");

let users = [];
let editing = false; // variable global para saber si se esta editando o creando por primera vez
let userId = null; // variable global para manipular el id del user a editar

/** al cargar la pagina, muestre los datos de la db */
window.addEventListener("DOMContentLoaded", async () => {
  //console.log("loaded");
  const response = await fetch("/api/users"); //cuando no se pone el metodo, por defecto es 'GET'
  const data = await response.json();
  //console.log(data);// trae la info de la db en formato objeto
  users = data; // arreglo de objetos
  renderUser(users);
});

/** Crear datos ingresados y actualizar lista de datos */
userForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  //console.log(e);
  username = userForm[0].value;
  email = userForm["email"].value;
  password = userForm["password"].value;
  //console.log(username, email, password);

  //sino se esta editando, se crea
  if (!editing) {
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
  } else {
    // si se esta editando se actualiza el user
    const response = await fetch(`/api/users/${userId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        password,
      }),
    });
    const updateUser = await response.json();
    users = users.map((user) =>
      user.id === updateUser.id ? updateUser : user
    );
    editing = false; // para dejar de editar
    userId = null; // no guarde el ultimo id
  }

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
                <button class='btn-delete btn btn-danger btn-sm'>Delete</button>
                <button class='btn-edit btn btn-primary btn-sm'>Edit</button>
            </div>
        </header>
        <p>${user.email}</p>
        <p class='text-truncate'>${user.password}</p>
    `;

    // Eliminar un dato del backend
    const btnDelete = userItem.querySelector(".btn-delete");
    btnDelete.addEventListener("click", async (e) => {
      const response = await fetch(`/api/users/${user.id}`, {
        method: "DELETE",
      });

      const data = await response.json();
      console.log(data);
      // usar filter para quitar elementos, donde se cumpla la igualdad
      // los que no cumplen los guarda en una nueva lista
      users = users.filter((user) => user.id !== data.id);
      renderUser(users);
    });

    // Editar un dato almacenado
    const btnEdit = userItem.querySelector(".btn-edit");
    btnEdit.addEventListener("click", async () => {
      // traemos los datos de la db
      const response = await fetch(`/api/users/${user.id}`);
      const data = await response.json();

      userForm["username"].value = data.username;
      userForm["email"].value = data.email;

      editing = true;
      userId = data.id;
      console.log(data.username);
    });

    userList.append(userItem);
  });
}
