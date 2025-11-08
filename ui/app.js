const btn = document.getElementById("analyzeBtn");
const resultBox = document.getElementById("resultBox");

btn.addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;

    if (!text.trim()) {
        alert("Enter a narrative");
        return;
    }

    // Dummy inference (placeholder) — replace with API call
    const mock = {
        cluster: 5,
        label: "Runway Ops / Clearance",
        keywords: ["runway", "short", "tower", "final"],
        summary: "Likely departure/landing clearance confusion near runway."
    };

    document.getElementById("clusterId").innerText = mock.cluster;
    document.getElementById("clusterLabel").innerText = mock.label;
    document.getElementById("keywords").innerText = mock.keywords.join(", ");
    document.getElementById("summaryText").innerText = mock.summary;

    resultBox.classList.remove("hidden");
});
