const apiUrl = "http://localhost:8000/users"; // Adjust the URL if needed

document.getElementById("save-user").addEventListener("click", function () {
    const userId = document.getElementById("user-id").value;

    const userData = {
        first_name: document.getElementById("first-name").value,
        last_name: document.getElementById("last-name").value,
        patronymic: document.getElementById("patronymic").value,
        age: document.getElementById("age").value,
        phone_number: document.getElementById("phone-number").value,
        email: document.getElementById("email").value,
        company: document.getElementById("company").value,
        profession: document.getElementById("profession").value,
    };

    if (userId) {
        // Update user
        fetch(`${apiUrl}/${userId}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        })
            .then(response => response.json())
            .then(data => {
                Swal.fire({
                    title: 'Успех!',
                    text: 'Пользователь обновлен!',
                    icon: 'success',
                    confirmButtonText: 'ОК'
                });
                loadUsers();
                clearForm();
            })
            .catch(error => console.error('Error:', error));

    } else {
        // Create user
        fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        })
            .then(response => response.json())
            .then(data => {
                Swal.fire({
                    title: 'Успех!',
                    text: 'Пользователь создан с ID ' + data.id,
                    icon: 'success',
                    confirmButtonText: 'ОК'
                });
                loadUsers();
                clearForm();
            })
            .catch(error => console.error('Error:', error));
    }
});

function loadUsers() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(users => {
            const userList = document.getElementById("user-list");
            userList.innerHTML = "";

            users.forEach(user => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${user.first_name}</td>
                    <td>${user.last_name}</td>
                    <td>${user.patronymic}</td>
                    <td>${user.age}</td>
                    <td>${user.email}</td>
                    <td>${user.phone_number}</td>
                    <td>${user.company}</td>
                    <td>${user.profession}</td>
                    <td>
                        <button onclick='editUser(${JSON.stringify(user)})'>Редактировать</button>
                        <button onclick='deleteUser(${user.id})'>Удалить</button>
                    </td>`;

                userList.appendChild(row);
            });
        })
        .catch(error => console.error('Error:', error));
}

function editUser(user) {
    document.getElementById("user-id").value = user.id;
    document.getElementById("first-name").value = user.first_name;
    document.getElementById("last-name").value = user.last_name;
    document.getElementById("age").value = user.age;
    document.getElementById("patronymic").value = user.patronymic || "";
    document.getElementById("phone-number").value = user.phone_number || "";
    document.getElementById("email").value = user.email || "";
    document.getElementById("company").value = user.company || "";
    document.getElementById("profession").value = user.profession || "";
}

function deleteUser(userId) {
    fetch(`${apiUrl}/${userId}`, {method: "DELETE"})
        .then(response => response.json())
        .then(data => {
            Swal.fire({
                title: 'Успех!',
                text: 'Пользователь удален!',
                icon: 'success',
                confirmButtonText: 'ОК'
            });
            loadUsers();
        })
        .catch(error => console.error('Error:', error));
}

function clearForm() {
    document.getElementById("user-id").value = "";
    document.getElementById("first-name").value = "";
    document.getElementById("last-name").value = "";
    document.getElementById("patronymic").value = "";
    document.getElementById("age").value = "";
    document.getElementById("phone-number").value = "";
    document.getElementById("email").value = "";
    document.getElementById("company").value = "";
    document.getElementById("profession").value = "";
}

// Load users on page load
loadUsers();
