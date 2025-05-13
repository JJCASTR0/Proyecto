// Definir una constante global para la URL base
const BASE_URL = "http://127.0.0.1:5000";

/**
 * Función para visualizar los datos en la tabla.
 * Recorre los registros de "baul" y genera las filas HTML para mostrar.
 * 
 * @param {Object} data - Datos a visualizar, debe contener una propiedad 'baul' con los registros.
 */
function visualizar(data) {
    let tabla = ""; // Inicializa la variable para almacenar el HTML de la tabla

    // Recorre cada elemento en el array "baul" y crea una fila de tabla
    data.baul.forEach(item => {
        tabla += `
            <tr data-id="${item.id_baul}">
                <td>${item.id_baul}</td>
                <td>${item.plataforma}</td>
                <td>${item.usuario}</td>
                <td>${item.clave}</td>
                <td>
                    <button type='button' class="btn btn-info" 
                        onclick="location.href='edit.html?variable1=${item.id_baul}'">
                        <img src='Imagenes/editar.svg' height='30' width='30'/>
                    </button>
                </td>
                <td>
                    <button type='button' class="btn btn-warning" 
                        onclick="eliminar(${item.id_baul})">
                        <img src='Imagenes/eliminar.svg' height='30' width='30'/>
                    </button>
                </td>
            </tr>`;
    });
    // Inserta las filas generadas en el cuerpo de la tabla
    document.getElementById('data').innerHTML = tabla;
}

/**
 * Función para realizar una consulta general (GET) y visualizar todos los registros.
 * 
 * Realiza una solicitud GET a la API para obtener todos los registros y luego llama a la función 
 * `visualizar` para mostrarlos en la tabla.
 */
function consulta_general() {
    fetch(`${BASE_URL}/`) // Realiza una solicitud GET al endpoint
        .then(response => {
            if (!response.ok) throw new Error(`Error: ${response.status}`); // Manejo de errores HTTP
            return response.json(); // Convierte la respuesta en JSON
        })
        .then(data => visualizar(data)) // Muestra los datos en la tabla
        .catch(error => console.error('Error:', error)); // Captura y muestra errores en la consola
}

/**
 * Función para eliminar un registro (DELETE).
 * 
 * Elimina un registro específico de la base de datos mediante una solicitud DELETE.
 * 
 * @param {number} id - El ID del registro que se desea eliminar.
 */
function eliminar(id) {
    fetch(`${BASE_URL}/eliminar/${id}`, { method: 'DELETE' }) // Solicitud DELETE
    .then(response => {
        if (!response.ok) throw new Error(`Error: ${response.status}`); // Manejo de errores HTTP
        return response.json();
    })
    .then(res => {
        actualizarDOM(id); // Elimina el elemento directamente del DOM
        swal("Mensaje", `Registro ${res.mensaje} exitosamente`, "success"); // Notificación de éxito
    })
    .catch(error => console.error('Error:', error)); // Captura y muestra errores en la consola
}

/**
 * Función para actualizar el DOM después de eliminar un elemento.
 * 
 * Elimina la fila correspondiente al registro eliminado sin recargar la página.
 * 
 * @param {number} id - El ID del registro eliminado.
 */
function actualizarDOM(id) {
    const row = document.querySelector(`tr[data-id="${id}"]`);
    if (row) row.remove(); // Elimina directamente la fila del DOM
}

/**
 * Función para registrar un nuevo registro (POST).
 * 
 * Registra un nuevo registro en la base de datos mediante una solicitud POST.
 */
function registrar() {
    // Obtiene los valores de los campos de entrada
    const plat = document.getElementById("plataforma").value;
    const usua = document.getElementById("usuario").value;
    const clav = document.getElementById("clave").value;

    // Crea el objeto de datos
    const data = {
        plataforma: plat,
        usuario: usua,
        clave: clav
    };

    fetch(`${BASE_URL}/registro`, {
        method: "POST", // Método HTTP POST para registrar
        body: JSON.stringify(data), // Convierte el objeto a JSON
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        return response.json();
    })
    .then(response => {
        if (response.mensaje === "Error") {
            swal("Mensaje", "Error en el registro", "error"); // Alerta de error
        } else {
            consulta_general(); // Refresca la tabla de datos sin recargar la página
            swal("Mensaje", "Registro agregado exitosamente", "success"); // Alerta de éxito
        }
    })
    .catch(error => console.error('Error:', error)); // Captura errores
}

/**
 * Función para consultar un registro individual (GET).
 * 
 * Consulta un registro individual basado en su ID y muestra sus datos en los campos de entrada.
 * 
 * @param {number} id - El ID del registro que se desea consultar.
 */
function consulta_individual(id) {
    fetch(`${BASE_URL}/consulta_individual/${id}`) // Solicitud GET al endpoint
        .then(response => {
            if (!response.ok) throw new Error(`Error: ${response.status}`); 
            return response.json(); // Convierte la respuesta en JSON
        })
        .then(data => {
            // Rellena los campos de entrada con los valores obtenidos
            document.getElementById("plataforma").value = data.baul.plataforma;
            document.getElementById("usuario").value = data.baul.usuario;
            document.getElementById("clave").value = data.baul.clave;
        })
        .catch(error => console.error('Error:', error)); // Captura errores
}

/**
 * Función para modificar un registro existente (PUT).
 * 
 * Modifica un registro existente en la base de datos mediante una solicitud PUT.
 * 
 * @param {number} id - El ID del registro que se desea modificar.
 */
function modificar(id) {
    // Obtiene los valores de los campos de entrada
    const plat = document.getElementById("plataforma").value;
    const usua = document.getElementById("usuario").value;
    const clav = document.getElementById("clave").value;

    // Crea el objeto de datos
    const data = {
        plataforma: plat,
        usuario: usua,
        clave: clav
    };

    fetch(`${BASE_URL}/actualizar/${id}`, {
        method: "PUT", // Método HTTP PUT para actualizar
        body: JSON.stringify(data), // Convierte el objeto a JSON
        headers: {
            "content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        return response.json();
    })
    .then(response => {
        if(!response.mensaje === "Error"){
            swal("Mensaje", "Error al actualizar el registro", "error"); // Alerta de error
        } else {
            consulta_general(); // Refresca la tabla de datos sin recargar la página
            swal("Mensaje", "Registro actualizado exitosamente", "success"); // Alerta de éxito
        }
    })
    .catch(error => console.error('Error', error)); // Captura errores
}