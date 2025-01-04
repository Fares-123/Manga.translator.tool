document
  .getElementById("uploadForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    // جلب القيم من الحقول
    const chapterLink = document.getElementById("chapterLink").value;
    const folderName = document.getElementById("folderName").value || "Default";
    const tags = document.getElementById("tags").value.split(",");
    const responseMessage = document.getElementById("responseMessage");

    // تحديث الرسالة أثناء المعالجة
    responseMessage.textContent = "جارٍ معالجة الفصل...";

    try {
      // إرسال البيانات إلى الخادم
      const response = await fetch("/process_and_upload", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ chapterLink, folderName, tags }),
      });

      // معالجة الرد من الخادم
      const result = await response.json();

      if (response.ok) {
        responseMessage.textContent = result.message;
      } else {
        responseMessage.textContent = `خطأ: ${result.error}`;
      }
    } catch (error) {
      // معالجة أي أخطاء أثناء الإرسال
      responseMessage.textContent = `حدث خطأ أثناء الإرسال: ${error.message}`;
    }
  });
