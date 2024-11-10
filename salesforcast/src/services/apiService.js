import axios from 'axios';

export const fetchForecast = async () => {
    try {
        const response = await axios.get('http://localhost:5000/forecast');
        return response.data;
    } catch (error) {
        console.error("Error fetching forecast:", error);
        return null;
    }
};
