// src/LocationButton.js
import React, { useState } from 'react';

const LocationButton = () => {
    const [latitude, setLatitude] = useState(null);
    const [longitude, setLongitude] = useState(null);
    const [error, setError] = useState('');

    const getLocation = async () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                async (position) => {
                    // Get the user's actual coordinates
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;

                    // Update state with actual coordinates
                    setLatitude(lat);
                    setLongitude(lon);

                    // Send coordinates to backend (this could be used for additional logic, if needed)
                    try {
                        const response = await fetch('/locations/coordinates/', {
                            method: 'POST',  // Using POST to send data
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ latitude: lat, longitude: lon }),
                        });
                        if (!response.ok) {
                            throw new Error('Failed to send coordinates to backend');
                        }
                        // Optionally handle the response from the backend if needed
                    } catch (err) {
                        setError('Failed to send location to backend');
                    }
                },
                (error) => {
                    setError('Unable to retrieve your location');
                }
            );
        } else {
            setError('Geolocation is not supported by this browser.');
        }
    };

    return (
        <div>
            <button onClick={getLocation}>Get Coordinates</button>

            {error && <p>{error}</p>}

            {latitude && longitude && (
                <div>
                    <h3>Your Coordinates:</h3>
                    <p>Latitude: {latitude}</p>
                    <p>Longitude: {longitude}</p>
                </div>
            )}
        </div>
    );
};

export default LocationButton;
