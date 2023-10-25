const apiKey = 'c3bd064bdbe667db5bdd5ce43e1b5e4b';
const city = 'london';

// Get the forecast container element from the HTML
const forecastContainer = document.getElementById('forecast');

// Get the current date
const currentDate = new Date();

// Calculate the date for the next 5 days
const forecastDates = [];
for (let i = 1; i <= 5; i++) {
  const nextDate = new Date();
  nextDate.setDate(currentDate.getDate() + i);
  forecastDates.push(nextDate);
}

// Make the API request for each forecast date
forecastDates.forEach(date => {
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // Extract the relevant information from the API response
      const forecastDate = `${day}/${month}/${year}`;
      const temperature = data.main.temp_max;
      
      const description = data.weather[0].description;
      const pressure = data.main.pressure;
      const humidity = data.main.humidity;

      // Create a new forecast card element
      const forecastCard = document.createElement('div');
      forecastCard.classList.add('forecast-card');

      // Populate the forecast card with data
      forecastCard.innerHTML = `
        <h3>Date: ${forecastDate}</h3>
        <p>Temperature: ${temperature} Kelvin</p>
        <p>pressure: ${pressure}</p>
        <p>humidity: ${humidity}</p>
        <p>Description: ${description}</p>
      `;

      // Append the forecast card to the forecast container
      forecastContainer.appendChild(forecastCard);
    })
    .catch(error => console.log('Error:', error));
});
