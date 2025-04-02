document.getElementById('multiplicar-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let numero = document.getElementById('numero').value;
    let formData = new FormData();
    formData.append('numero', numero);

    fetch('/multiplicar', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let resultadoDiv = document.getElementById('resultado');
        resultadoDiv.innerHTML = "";

        if (data.error) {
            resultadoDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
        } else {
            let tablaHTML = "<h3>Tabla de " + numero + "</h3><ul>";
            for (let clave in data) {
                tablaHTML += `<li>${clave} = ${data[clave]}</li>`;
            }
            tablaHTML += "</ul>";
            resultadoDiv.innerHTML = tablaHTML;
        }
    })
    .catch(error => console.error('Error:', error));
});