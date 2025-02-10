function predictWaterUsage() {
    const inputFeatures = {
        SoilMoisture: parseFloat(document.getElementById('soilMoisture').value),
        SoilTemperature: parseFloat(document.getElementById('soilTemperature').value),
        AirTemperature: parseFloat(document.getElementById('airTemperature').value),
        Humidity: parseFloat(document.getElementById('humidity').value),
        pH: parseFloat(document.getElementById('ph').value),
        CropType: parseFloat(document.getElementById('cropType').value),
        SolarRadiation: parseFloat(document.getElementById('solarRadiation').value),
        WindSpeed: parseFloat(document.getElementById('windSpeed').value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputFeatures)
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction !== undefined) {
            document.getElementById('prediction-result').innerText = `The predicted water usage is ${data.prediction.toFixed(2)} units`;
        } else {
            document.getElementById('prediction-result').innerText = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        document.getElementById('prediction-result').innerText = `Error: ${error}`;
    });
}
