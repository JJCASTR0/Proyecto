document.addEventListener("DOMContentLoaded", function () {
    let figuraSelect = document.getElementById("figura");
    let inputsDiv = document.getElementById("inputs");
    let calcularBtn = document.getElementById("calcular");
    let resultadoDiv = document.getElementById("resultado");

    function actualizarInputs() {
        let figura = figuraSelect.value;
        inputsDiv.innerHTML = "";

        if (figura === "circulo") {
            inputsDiv.innerHTML = `
                <label for="radio">Radio:</label>
                <input type="number" id="radio" name="radio" required>
            `;
        } else if (figura === "cuadrado") {
            inputsDiv.innerHTML = `
                <label for="lado">Lado:</label>
                <input type="number" id="lado" name="lado" required>
            `;
        } else if (figura === "triangulo") {
            inputsDiv.innerHTML = `
                <label for="base">Base:</label>
                <input type="number" id="base" name="base" required>
                <label for="altura">Altura:</label>
                <input type="number" id="altura" name="altura" required>
            `;
        }
    }

    figuraSelect.addEventListener("change", actualizarInputs);
    actualizarInputs();

    calcularBtn.addEventListener("click", function () {
        let figura = figuraSelect.value;
        let formData = new FormData();
        formData.append("figura", figura);

        if (figura === "circulo") {
            let radio = document.getElementById("radio").value;
            formData.append("radio", radio);
        } else if (figura === "cuadrado") {
            let lado = document.getElementById("lado").value;
            formData.append("lado", lado);
        } else if (figura === "triangulo") {
            let base = document.getElementById("base").value;
            let altura = document.getElementById("altura").value;
            formData.append("base", base);
            formData.append("altura", altura);
        }

        fetch("/calcular_area", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultadoDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
            } else {
                resultadoDiv.innerHTML = `<p>El área del ${data.figura} es: <strong>${data.area}</strong></p>`;
            }
        })
        .catch(error => console.error("Error:", error));
    });
});