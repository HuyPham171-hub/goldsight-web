// Load Plotly charts from JSON files for static deployment
window.loadPlotlyChart = async function(chartName, elementId) {
    try {
        const response = await fetch(`/assets/charts_cache/${chartName}.json`);
        if (!response.ok) {
            throw new Error(`Chart ${chartName} not found`);
        }
        const chartData = await response.json();
        Plotly.newPlot(elementId, chartData.data, chartData.layout, chartData.config || {});
    } catch (error) {
        console.error(`Error loading chart ${chartName}:`, error);
        const elem = document.getElementById(elementId);
        if (elem) {
            elem.innerHTML = `<div style="padding: 40px; text-align: center; color: #666;">
                Error loading chart: ${chartName}<br>
                <small>${error.message}</small>
            </div>`;
        }
    }
};
