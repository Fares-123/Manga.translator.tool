// جلب العناصر من الصفحة
const generateKeyBtn = document.getElementById("generateKeyBtn");
const fetchDataBtn = document.getElementById("fetchDataBtn");

// دالة لتوليد مفتاح RSA
generateKeyBtn.addEventListener("click", async () => {
    try {
        const response = await fetch("/generate-key");
        const data = await response.json();
        console.log("Generated Keys:", data);
        alert("RSA Key Generated! Check the console for details.");
    } catch (error) {
        console.error("Error generating key:", error);
        alert("Error generating RSA key.");
    }
});

// دالة لجلب البيانات
fetchDataBtn.addEventListener("click", async () => {
    try {
        const response = await fetch("/fetch-data");
        const data = await response.json();
        console.log("Fetched Data:", data);
        alert("Data Fetched! Check the console for details.");
    } catch (error) {
        console.error("Error fetching data:", error);
        alert("Error fetching data.");
    }
});
