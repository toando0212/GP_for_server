const ctx = document.getElementById('coordinateChart').getContext('2d');
        const data = {
            datasets: [
                {
                    label: 'Current Position',
                    data: [],
                    backgroundColor: 'rgba(255, 0, 0, 0.8)',
                    borderColor: 'rgba(255, 0, 0, 1)',
                    borderWidth: 2,
                    pointRadius: 8,
                    showLine: false
                },
                {
                    label: 'Floor Plan',
                    data: [
                        { x: -1, y: 0 },
                        { x: -1, y: 4 },
                        { x: 28, y: 4 },
                        { x: 28, y: 0 },
                        { x: -1, y: 0 }
                    ],
                    backgroundColor: 'rgba(240, 240, 240, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0
                },
                {
                    label: 'Elevator',
                    data: [
                        { x: 0, y: 0 },
                        { x: 0, y: -4 },
                        { x: 7, y: -4 },
                        { x: 7, y: 0 },
                        { x: 0, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Lab Room 1',
                    data: [
                        { x: 7, y: 0 },
                        { x: 7, y: -4 },
                        { x: 15, y: -4 },
                        { x: 15, y: 0 },
                        { x: 7, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Lab Room 2',
                    data: [
                        { x: 15, y: 0 },
                        { x: 15, y: -4 },
                        { x: 27, y: -4 },
                        { x: 27, y: 0 },
                        { x: 15, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'WC Men 1',
                    data: [
                        { x: -1, y: -2 },
                        { x: -4, y: -2 },
                        { x: -4, y: -7 },
                        { x: -1, y: -7 },
                        { x: -1, y: -2 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'WC Women 1',
                    data: [
                        { x: -1, y: -4 },
                        { x: -1, y: -7 },
                        { x: 4, y: -7 },
                        { x: 4, y: -4 },
                        { x: -1, y: -4 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Storage Room 1',
                    data: [
                        { x: -4, y: 0 },
                        { x: -4, y: -2 },
                        { x: -1, y: -2 },
                        { x: -1, y: 0 },
                        { x: -4, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'WC Men 2',
                    data: [
                        { x: 27, y: -4 },
                        { x: 27, y: -7 },
                        { x: 31, y: -7 },
                        { x: 31, y: -3 },
                        { x: 28, y: -3 },
                        { x: 28, y: -4 },
                        { x: 27, y: -4 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'WC Women 2',
                    data: [
                        { x: 28, y: -1 },
                        { x: 28, y: -3 },
                        { x: 31, y: -3 },
                        { x: 31, y: -1 },
                        { x: 28, y: -1 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Phòng kỹ thuật',
                    data: [
                        { x: 28, y: 0 },
                        { x: 28, y: -1 },
                        { x: 31, y: -1 },
                        { x: 31, y: 0 },
                        { x: 28, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Thang bộ',
                    data: [
                        { x: -1, y: 0 },
                        { x: -1, y: 4 },
                        { x: -3, y: 4 },
                        { x: -3, y: 0 },
                        { x: -1, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Thang bộ',
                    data: [
                        { x: 28, y: 0 },
                        { x: 28, y: 4 },
                        { x: 30, y: 4 },
                        { x: 30, y: 0 },
                        { x: 28, y: 0 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Phòng họp',
                    data: [
                        { x: -4, y: 4 },
                        { x: -4, y: 7 },
                        { x: 8, y: 7 },
                        { x: 8, y: 4 },
                        { x: -4, y: 4 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Phòng hỗ trợ',
                    data: [
                        { x: 8, y: 7 },
                        { x: 8, y: 4 },
                        { x: 13, y: 4 },
                        { x: 13, y: 7 },
                        { x: 8, y: 7 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'Phòng thí nghiệm 3',
                    data: [
                        { x: 13, y: 4 },
                        { x: 13, y: 7 },
                        { x: 20, y: 7 },
                        { x: 20, y: 4 },
                        { x: 13, y: 4 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
                {
                    label: 'ICT Lab',
                    data: [
                        { x: 20, y: 4 },
                        { x: 20, y: 7 },
                        { x: 31, y: 7 },
                        { x: 31, y: 4 },
                        { x: 20, y: 4 }
                    ],
                    backgroundColor: 'rgba(200, 200, 200, 0.3)',
                    borderColor: 'rgba(100, 100, 100, 1)',
                    borderWidth: 2,
                    fill: true,
                    showLine: true,
                    pointRadius: 0,
                    tension: 0
                },
            ]
        };

        const config = {
            type: 'scatter',
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    annotation: {
                        annotations: {
                            room1Label: {
                                type: 'label',
                                content: 'Elevator',
                                xValue: 3.5,
                                yValue: -2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            room4Label: {
                                type: 'label',
                                content: 'Men\'s Restroom 1',
                                xValue: -2.5,
                                yValue: -4.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            labRoom1Label: {
                                type: 'label',
                                content: 'Laboratory Room 1',
                                xValue: 11,
                                yValue: -2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            labRoom2Label: {
                                type: 'label',
                                content: 'Laboratory Room 2',
                                xValue: 21,
                                yValue: -2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            wcWomen1Label: {
                                type: 'label',
                                content: 'Women\'s Restroom 1',
                                xValue: 1.5,
                                yValue: -5.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            storageRoom1Label: {
                                type: 'label',
                                content: 'Storage Room',
                                xValue: -2.5,
                                yValue: -1,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 4,
                                borderRadius: 4
                            },
                            wcMen2Label: {
                                type: 'label',
                                content: 'Men\'s Restroom 2',
                                xValue: 29,
                                yValue: -5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            wcWomen2Label: {
                                type: 'label',
                                content: 'Women\'s Restroom 2',
                                xValue: 29.5,
                                yValue: -2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            rightStairsLabel: {
                                type: 'label',
                                content: 'Stairs',
                                xValue: 29,
                                yValue: 2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 4,
                                borderRadius: 4
                            },
                            meetingRoomLabel: {
                                type: 'label',
                                content: 'Meeting Room',
                                xValue: 3,
                                yValue: 5.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            supportRoomLabel: {
                                type: 'label',
                                content: 'Support Room',
                                xValue: 10.5,
                                yValue: 5.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            labRoom3Label: {
                                type: 'label',
                                content: 'Laboratory Room 3',
                                xValue: 16.5,
                                yValue: 5.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            ictLabLabel: {
                                type: 'label',
                                content: 'ICT Lab',
                                xValue: 25.5,
                                yValue: 5.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                            leftStairsLabel: {
                                type: 'label',
                                content: 'Stairs',
                                xValue: -2,
                                yValue: 2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 4,
                                borderRadius: 4
                            },
                            floorLabel: {
                                type: 'label',
                                content: 'Corridor Lobby',
                                xValue: 13.5,
                                yValue: 2,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 4,
                                borderRadius: 4
                            },
                            phongKyThuatLabel: {
                                type: 'label',
                                content: 'Technical Room',
                                xValue: 29.5,
                                yValue: -0.5,
                                backgroundColor: 'rgba(0, 0, 0, 0.1)',
                                font: {
                                    size: 10,
                                    weight: 'bold'
                                },
                                color: '#34495e',
                                padding: 6,
                                borderRadius: 4
                            },
                        }
                    }
                },
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom',
                        min: -8,
                        max: 32,
                        ticks: {
                            stepSize: 1
                        },
                        grid: {
                            color: 'rgba(200, 200, 200, 0.5)'
                        }
                    },
                    y: {
                        min: -10,
                        max: 10,
                        ticks: {
                            stepSize: 1
                        },
                        grid: {
                            color: 'rgba(200, 200, 200, 0.5)'
                        }
                    }
                }
            }
        };

        const coordinateChart = new Chart(ctx, config);

        function updateCoordinates() {
    fetch('/coordinates')
        .then(response => response.json())
        .then(data => {
            const x = data.x; // Tọa độ X mới
            const y = data.y; // Tọa độ Y mới

            // Thêm tọa độ mới vào dataset
            coordinateChart.data.datasets[0].data.push({ x: x, y: y });

            // Cập nhật biểu đồ
            coordinateChart.update();
        })
        .catch(error => console.error('Error fetching coordinates:', error));
}

// Gọi hàm cập nhật mỗi giây
setInterval(updateCoordinates, 1000);