document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("agreementForm");
  const previewBtn = document.getElementById("previewBtn");
  const generateBtn = document.getElementById("generateBtn");
  const previewModal = document.getElementById("previewModal");
  const loadingOverlay = document.getElementById("loadingOverlay");
  const closeBtn = document.querySelector(".close");
  const previewContent = document.getElementById("previewContent");

  const formatDate = (dateStr) => {
    const date = new Date(dateStr);
    if (!isNaN(date.getTime())) {
      const day = String(date.getDate()).padStart(2, "0");
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const year = String(date.getFullYear()).slice(-2);
      return `${day}-${month}-${year}`;
    }
    return date;
  };

  // Field mappings for better display names
  const fieldLabels = {
    agreement_number: "Agreement Number",
    agreement_date: "Agreement Date",
    name: "Full Name",
    nationality: "Nationality",
    phone: "Phone Number",
    citizen: "Residence Type",
    passport: "Passport/ID Number",
    remaining_date: "Remaining Date",
    v1: "Check-in Date",
    v2: "Check-out Date",
    v3: "Rent Description",
    v4: "Total Rent",
    v5: "Received Rent",
    v6: "Remaining Rent",
    v7: "Insurance/Deposit",
    v8: "Room Details",
  };

  // Preview functionality
  previewBtn.addEventListener("click", function () {
    const formData = new FormData(form);
    let previewHTML = "";

    for (let [key, value] of formData.entries()) {
      if (value.trim() !== "") {
        previewHTML += `
                    <div class="preview-item">
                        <div class="preview-label">${
                          fieldLabels[key] || key
                        }</div>
                        <div class="preview-value">${value}</div>
                    </div>
                `;
      }
    }

    if (previewHTML === "") {
      previewHTML =
        '<p style="text-align: center; color: #666;">Please fill in the form first to see a preview.</p>';
    }

    previewContent.innerHTML = previewHTML;
    previewModal.style.display = "block";
  });

  // Close modal
  closeBtn.addEventListener("click", function () {
    previewModal.style.display = "none";
  });

  // Close modal when clicking outside
  window.addEventListener("click", function (event) {
    if (event.target === previewModal) {
      previewModal.style.display = "none";
    }
  });

  // Form submission
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Validate form
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    // Show loading overlay
    loadingOverlay.style.display = "block";

    // Collect form data
    const formData = new FormData(form);
    const data = {};

    for (let [key, value] of formData.entries()) {
      if (key === "remaining_date") continue;
      if (["agreement_date", "v1", "v2"].includes(key)) {
        value = formatDate(value);
      }
      if (key === "v6" && formData.get("remaining_date")) {
        const date = formData.get("remaining_date");
        value = `${value} - WILL PAY ${formatDate(date)}`;
      }
      data[key] = value;
    }

    // Send data to backend
    generatePDF(data);
  });

  // Generate PDF function
  async function generatePDF(data) {
    try {
      const response = await fetch("/generate-pdf", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `${data.v8}-agreement.pdf`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

        showMessage("PDF generated successfully!", "success");
      } else {
        const errorData = await response.json();
        throw new Error(errorData.error || "Failed to generate PDF");
      }
    } catch (error) {
      console.error("Error generating PDF:", error);
      showMessage("Error generating PDF: " + error.message, "error");
    } finally {
      loadingOverlay.style.display = "none";
    }
  }

  // Show message function
  function showMessage(message, type) {
    // Remove existing messages
    const existingMessage = document.querySelector(".message");
    if (existingMessage) {
      existingMessage.remove();
    }

    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;

    const formContainer = document.querySelector(".form-container");
    formContainer.insertBefore(messageDiv, formContainer.firstChild);

    // Auto-remove message after 5 seconds
    setTimeout(() => {
      if (messageDiv.parentNode) {
        messageDiv.remove();
      }
    }, 5000);
  }

  // Real-time form validation
  const inputs = form.querySelectorAll("input, select, textarea");
  inputs.forEach((input) => {
    input.addEventListener("blur", function () {
      validateField(this);
    });

    input.addEventListener("input", function () {
      if (this.classList.contains("error")) {
        validateField(this);
      }
    });
  });

  function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;

    // Remove existing error styling
    field.classList.remove("error");

    // Custom validation rules
    let isValid = true;
    let errorMessage = "";

    switch (fieldName) {
      case "phone":
        if (value && !/^[\d\s\-\+\(\)]+$/.test(value)) {
          isValid = false;
          errorMessage = "Please enter a valid phone number";
        }
        break;

      case "v4":
      case "v5":
      case "v7":
        if ((value && isNaN(value)) || value < 0) {
          isValid = false;
          errorMessage = "Please enter a valid positive number";
        }
        break;

      case "v1":
      case "v2":
        if (value) {
          const date = new Date(value);
          if (isNaN(date.getTime())) {
            isValid = false;
            errorMessage = "Please enter a valid date";
          }
        }
        break;
    }

    if (!isValid) {
      field.classList.add("error");
      field.setCustomValidity(errorMessage);
    } else {
      field.setCustomValidity("");
    }
  }

  // Auto-format phone number
  const phoneInput = document.getElementById("phone");
  phoneInput.addEventListener("input", function (e) {
    let value = e.target.value.replace(/\D/g, "");
    if (value.length > 0) {
      // Format as needed (you can customize this)
      if (value.length <= 3) {
        value = value;
      } else if (value.length <= 6) {
        value = value.slice(0, 3) + "-" + value.slice(3);
      } else {
        value =
          value.slice(0, 3) +
          "-" +
          value.slice(3, 6) +
          "-" +
          value.slice(6, 10);
      }
    }
    e.target.value = value;
  });

  // Auto-calculate remaining balance
  const totalAmountInput = document.getElementById("v4");
  const advancePaymentInput = document.getElementById("v5");
  const remainingBalanceInput = document.getElementById("v6");

  function calculateRemainingBalance() {
    const total = parseFloat(totalAmountInput.value) || 0;
    const advance = parseFloat(advancePaymentInput.value) || 0;
    const remaining = total - advance;

    if (remaining >= 0) {
      remainingBalanceInput.value = remaining;
    }
  }

  totalAmountInput.addEventListener("input", calculateRemainingBalance);
  advancePaymentInput.addEventListener("input", calculateRemainingBalance);

  // Set default dates
  const today = new Date();
  const tomorrow = new Date(today);
  tomorrow.setDate(tomorrow.getDate() + 1);

  const checkInInput = document.getElementById("v1");
  const checkOutInput = document.getElementById("v2");

  checkInInput.value = today.toISOString().split("T")[0];
  checkOutInput.value = tomorrow.toISOString().split("T")[0];

  // Ensure check-out date is after check-in date
  checkInInput.addEventListener("change", function () {
    const checkInDate = new Date(this.value);
    const checkOutDate = new Date(checkOutInput.value);

    if (checkOutDate <= checkInDate) {
      const nextDay = new Date(checkInDate);
      nextDay.setDate(nextDay.getDate() + 1);
      checkOutInput.value = nextDay.toISOString().split("T")[0];
    }
  });

  // Keyboard shortcuts
  document.addEventListener("keydown", function (e) {
    // Ctrl/Cmd + Enter to submit form
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      generateBtn.click();
    }

    // Escape to close modal
    if (e.key === "Escape" && previewModal.style.display === "block") {
      previewModal.style.display = "none";
    }
  });
});
