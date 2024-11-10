import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { fetchForecast } from '../services/apiService';

const SalesChart = () => {
    const [chartData, setChartData] = useState({});

    useEffect(() => {
        const loadForecast = async () => {
            const forecastData = await fetchForecast();
            if (forecastData) {
                setChartData({
                    labels: Object.keys(forecastData),
                    datasets: [
                        {
                            label: 'Forecasted Sales',
                            data: Object.values(forecastData),
                            borderColor: 'rgba(75,192,192,1)',
                            fill: false,
                        },
                    ],
                });
            }
        };
        loadForecast();
    }, []);

    return <Line data={chartData} />;
};

export default SalesChart;
