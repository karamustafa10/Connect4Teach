document.addEventListener("DOMContentLoaded", function () {
    // Üyelik tipi seçimini dinle
    const membershipSelect = document.querySelector("select[name='membership_type']");
    membershipSelect.addEventListener("change", function () {
        const selectedOption = this.value;
        const extraFieldDiv = document.getElementById("extra-field");

        // Ek alanı temizle
        extraFieldDiv.innerHTML = "";

        // Seçilen üyelik tipine göre ilgili alanı ekle
        if (selectedOption === "teacher") {
            extraFieldDiv.innerHTML = `
                <label for="field_info" class="form-label">Alan Bilgisi</label>
                <input type="text" class="form-control" name="field_info" required>
            `;
        } else if (selectedOption === "student") {
            extraFieldDiv.innerHTML = `
                <label for="field_info" class="form-label">Sınıf Bilgisi</label>
                <input type="text" class="form-control" name="field_info" required>
            `;
        }
    });
});
