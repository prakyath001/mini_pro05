document.getElementById("uploadBtn").addEventListener("click", () => {
    document.getElementById("imageInput").click();
  });
  
  document.getElementById("imageInput").addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      // Display the image preview
      const reader = new FileReader();
      reader.onload = function (e) {
        const previewImage = document.getElementById("previewImage");
        previewImage.src = e.target.result;
      };
      reader.readAsDataURL(file);
  
      // Simulate image recognition
      setTimeout(() => {
        const resultText = document.getElementById("resultText");
        resultText.textContent = Recognized: ${recognizeImage(file.name)};
      }, 2000);
    }
  });
  
  // Placeholder for image recognition logic
  function recognizeImage(imageName) {
    // This is a dummy recognition logic
    if (imageName.toLowerCase().includes("cat")) {
      return "Cat detected!";
    } else if (imageName.toLowerCase().includes("dog")) {
      return "Dog detected!";
    } else {
      return "royal enfield";
    }
  }