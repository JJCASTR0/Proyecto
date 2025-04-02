document.getElementById('calc-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let x = document.getElementById('x').value;
    let z = document.getElementById('z').value;

    let formData = new FormData();
    formData.append('x', x);
    formData.append('z', z);

    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.result !== undefined) {
            document.getElementById('result').textContent = 'Resultado: Y = ' + data.result;
        } else {
            document.getElementById('result').textContent = 'Error: ' + data.error;
        }
    })
    .catch(error => console.error('Error:', error));
});