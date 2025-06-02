const { jsPDF } = window.jspdf;
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const convertedPreview = document.getElementById("convertedPreview");
const convertedCtx = convertedPreview.getContext("2d");
const imageUpload = document.getElementById("imageUpload");
const postUpload = document.getElementById("postUpload");
const convertBtn = document.getElementById("convertBtn");
const editBtn = document.getElementById("editBtn");
const convertPanel = document.getElementById("convertPanel");
const editPanel = document.getElementById("editPanel");
const compressionPreset = document.getElementById("compressionPreset");
const compressionSlider = document.getElementById("compressionSlider");
const compressionValue = document.getElementById("compressionValue");
const customCompression = document.getElementById("customCompression");
const format = document.getElementById("format");
const downloadConvertBtn = document.getElementById("downloadConvertBtn");
const originalSize = document.getElementById("originalSize");
const compressedSize = document.getElementById("compressedSize");
const originalPreview = document.getElementById("originalPreview");
const brightness = document.getElementById("brightness");
const contrast = document.getElementById("contrast");
const grayscale = document.getElementById("grayscale");
const sepia = document.getElementById("sepia");
const borderWidth = document.getElementById("borderWidth");
const borderColor = document.getElementById("borderColor");
const shape = document.getElementById("shape");
const widthInput = document.getElementById("width");
const heightInput = document.getElementById("height");
const widthUnit = document.getElementById("widthUnit");
const heightUnit = document.getElementById("heightUnit");
const dpi = document.getElementById("dpi");
const lockAspect = document.getElementById("lockAspect");
const sizeControls = document.getElementById("sizeControls");
const cropTemplate = document.getElementById("cropTemplate");
const cropImage = document.getElementById("cropImage");
const editCompressionPreset = document.getElementById("editCompressionPreset");
const editCompressionSlider = document.getElementById("editCompressionSlider");
const editCompressionValue = document.getElementById("editCompressionValue");
const editCustomCompression = document.getElementById("editCustomCompression");
const editFormat = document.getElementById("editFormat");
const downloadEditBtn = document.getElementById("downloadEditBtn");
const error = document.getElementById("error");
let img = new Image();
let originalFile = null;
let cropper = null;
let aspectRatio = 0;

imageUpload.addEventListener("change", (e) => {
    originalFile = e.target.files[0];
    if (!originalFile || !["image/png", "image/jpeg", "image/webp", "image/heic", "image/heif"].includes(originalFile.type)) {
        showError("Please upload a PNG, JPEG, WebP, or HEIC image.");
        return;
    }
    error.style.display = "none";
    img.src = URL.createObjectURL(originalFile);
    img.onload = () => {
        try {
            canvas.width = img.width;
            canvas.height = img.height;
            convertedPreview.width = img.width;
            convertedPreview.height = img.height;
            widthInput.value = img.width;
            heightInput.value = img.height;
            aspectRatio = img.width / img.height;
            resetCanvas();
            postUpload.classList.remove("hidden");
            canvas.style.display = "block";
            originalPreview.src = img.src;
            updateSizes();
            updateConvertedPreview();
            if (cropper) cropper.destroy();
            cropImage.src = img.src;
            cropImage.classList.remove("hidden");
            cropper = new Cropper(cropImage, {
                aspectRatio: cropTemplate.value === "square" ? 1 : cropTemplate.value === "rectangle" ? 4 / 3 : cropTemplate.value === "rectangle169" ? 16 / 9 : NaN,
                viewMode: 1,
                autoCropArea: 0.8,
            });
        } catch (err) {
            console.error("Image load error:", err);
            showError("Failed to load image.");
        }
    };
});

convertBtn.addEventListener("click", () => {
    convertPanel.classList.remove("hidden");
    editPanel.classList.add("hidden");
});

editBtn.addEventListener("click", () => {
    editPanel.classList.remove("hidden");
    convertPanel.classList.add("hidden");
});

compressionPreset.addEventListener("change", () => {
    customCompression.classList.toggle("hidden", compressionPreset.value !== "custom");
    if (compressionPreset.value !== "custom") {
        compressionSlider.value = compressionPreset.value * 100;
        compressionValue.textContent = `${compressionSlider.value}%`;
    }
    updateConvertedPreview();
});

compressionSlider.addEventListener("input", () => {
    compressionValue.textContent = `${compressionSlider.value}%`;
    updateConvertedPreview();
});

format.addEventListener("change", updateConvertedPreview);

editCompressionPreset.addEventListener("change", () => {
    editCustomCompression.classList.toggle("hidden", editCompressionPreset.value !== "custom");
    if (editCompressionPreset.value !== "custom") {
        editCompressionSlider.value = editCompressionPreset.value * 100;
        editCompressionValue.textContent = `${editCompressionSlider.value}%`;
    }
});

editCompressionSlider.addEventListener("input", () => {
    editCompressionValue.textContent = `${editCompressionSlider.value}%`;
});

[brightness, contrast, grayscale, sepia, borderWidth, borderColor].forEach(input => {
    input.addEventListener("input", applyEdits);
});

shape.addEventListener("change", () => {
    sizeControls.classList.toggle("hidden", shape.value === "original");
    if (shape.value === "square") {
        heightInput.value = widthInput.value;
        lockAspect.checked = true;
    }
    applyEdits();
});

widthInput.addEventListener("input", () => {
    if (lockAspect.checked && shape.value !== "original") {
        heightInput.value = Math.round(widthInput.value / aspectRatio);
    }
    applyEdits();
});

heightInput.addEventListener("input", () => {
    if (lockAspect.checked && shape.value !== "original") {
        widthInput.value = Math.round(heightInput.value * aspectRatio);
    }
    applyEdits();
});

[widthUnit, heightUnit, dpi].forEach(input => {
    input.addEventListener("input", applyEdits);
});

cropTemplate.addEventListener("change", () => {
    if (cropper) {
        cropper.setAspectRatio(
            cropTemplate.value === "square" ? 1 :
                cropTemplate.value === "rectangle" ? 4 / 3 :
                    cropTemplate.value === "rectangle169" ? 16 / 9 : NaN
        );
    }
});

downloadConvertBtn.addEventListener("click", downloadImage);
downloadEditBtn.addEventListener("click", downloadImage);

function resetCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0);
}

function applyEdits() {
    try {
        let width = img.width;
        let height = img.height;

        if (shape.value !== "original") {
            const unit = widthUnit.value;
            const w = parseFloat(widthInput.value) || 100;
            const h = parseFloat(heightInput.value) || 100;
            const d = parseInt(dpi.value) || 300;
            if (unit === "cm") {
                width = (w * d) / 2.54;
                height = (h * d) / 2.54;
            } else if (unit === "in") {
                width = w * d;
                height = h * d;
            } else {
                width = w;
                height = h;
            }
            if (shape.value === "square") height = width;
        }

        canvas.width = width + (parseInt(borderWidth.value) * 2);
        canvas.height = height + (parseInt(borderWidth.value) * 2);
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        if (borderWidth.value > 0) {
            ctx.fillStyle = borderColor.value;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        ctx.filter = `
      brightness(${brightness.value}%)
      contrast(${contrast.value}%)
      grayscale(${grayscale.value}%)
      sepia(${sepia.value}%)
    `;
        ctx.drawImage(img, parseInt(borderWidth.value), parseInt(borderWidth.value), width, height);
        error.style.display = "none";
    } catch (err) {
        console.error("Edit error:", err);
        showError("Failed to apply edits.");
    }
}

function updateConvertedPreview() {
    try {
        const quality = compressionPreset.value === "custom" ? compressionSlider.value / 100 : parseFloat(compressionPreset.value);
        convertedPreview.width = img.width;
        convertedPreview.height = img.height;
        convertedCtx.clearRect(0, 0, convertedPreview.width, convertedPreview.height);
        convertedCtx.drawImage(img, 0, 0);
        const dataUrl = convertedPreview.toDataURL(`image/${format.value === "pdf" ? "png" : format.value}`, quality);
        const size = Math.round((dataUrl.length * 3 / 4) / 1024);
        compressedSize.textContent = `${size} KB`;
        originalSize.textContent = originalFile ? `${Math.round(originalFile.size / 1024)} KB` : "0 KB";
    } catch (err) {
        console.error("Preview error:", err);
        showError("Failed to update preview.");
    }
}

function downloadImage(e) {
    const isEdit = e.target.id === "downloadEditBtn";
    const quality = isEdit ?
        (editCompressionPreset.value === "custom" ? editCompressionSlider.value / 100 : parseFloat(editCompressionPreset.value)) :
        (compressionPreset.value === "custom" ? compressionSlider.value / 100 : parseFloat(compressionPreset.value));
    const outputFormat = isEdit ? editFormat.value : format.value;

    if (isEdit && cropper) {
        const cropped = cropper.getCroppedCanvas();
        canvas.width = cropped.width;
        canvas.height = cropped.height;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(cropped, 0, 0);
        img.src = canvas.toDataURL("image/png");
        img.onload = () => {
            applyEdits();
            performDownload(outputFormat, quality);
        };
    } else {
        applyEdits();
        performDownload(outputFormat, quality);
    }
}

function performDownload(outputFormat, quality) {
    if (outputFormat === "pdf") {
        const pdf = new jsPDF({
            orientation: canvas.width > canvas.height ? "landscape" : "portrait",
            unit: "px",
            format: [canvas.width, canvas.height]
        });
        pdf.addImage(canvas.toDataURL("image/png"), "PNG", 0, 0, canvas.width, canvas.height);
        pdf.save("edited-image.pdf");
    } else if (outputFormat === "gif") {
        const gif = new GIF({
            workers: 2,
            quality: 10,
            width: canvas.width,
            height: canvas.height
        });
        gif.addFrame(canvas, { delay: 200 });
        gif.on("finished", (blob) => {
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "edited-image.gif";
            link.click();
        });
        gif.render();
    } else {
        const dataUrl = canvas.toDataURL(`image/${outputFormat}`, quality);
        const link = document.createElement("a");
        link.href = dataUrl;
        link.download = `edited-image.${outputFormat}`;
        link.click();
    }
}

function showError(message) {
    error.textContent = message;
    error.style.display = "block";
}

console.log("Image Editing App script loaded.");