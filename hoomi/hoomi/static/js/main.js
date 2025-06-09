// Property data fetch and show on the index.html using Axios
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

function fetchProperties() {
    axios.get('http://127.0.0.1:8000/property/properties/')
        .then(response => {
            console.log("Fetched properties:", response.data);
            const data = Array.isArray(response.data) ? response.data : response.data.results || [];
            renderProperties(data);
        })
        .catch(error => {
            console.error("Error fetching properties:", error);
        });
}

function renderProperties(properties) {
    const container = document.getElementById("propertyList");
    if (!container) {
        console.error("Element with id 'propertyList' not found.");
        return;
    }

    container.innerHTML = ''; // Clear any existing content

    if (!properties.length) {
        container.innerHTML = "<p>No properties available.</p>";
        return;
    }

    properties.forEach(property => {
        const card = document.createElement("div");
        card.classList.add("property-card");

        card.innerHTML = `
        <h3>${property.title}</h3>
        <p><strong>Type:</strong> ${property.property_type}</p>
        <p><strong>Price:</strong> ₹${property.price_per_month} / month</p>
        <p><strong>Location:</strong> ${property.city}, ${property.state}</p>
        <p><strong>Bedrooms:</strong> ${property.bedrooms} | <strong>Bathrooms:</strong> ${property.bathrooms}</p>
        <p><strong>Available From:</strong> ${property.available_from}</p>
      `;

        container.appendChild(card);
    });
}
