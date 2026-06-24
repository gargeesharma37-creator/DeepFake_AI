async function detectVoice() {

    const fileInput = document.getElementById("audioFile");
    const result = document.getElementById("result");

    if (!fileInput.files.length) {
        result.innerText = "Please choose an audio file.";
        return;
    }

    try {

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        result.innerText =
            "Prediction: " + data.prediction;

    }
    catch (error) {

        console.log(error);

        result.innerText =
            "Error connecting to backend";
    }
}


async function detectVideo() {

    alert("Video button clicked");

    const fileInput =
        document.getElementById("videoFile");

    const result =
        document.getElementById("videoResult");

    if (!fileInput.files.length) {

        result.innerText =
            "Please choose a video.";

        return;
    }

    const formData = new FormData();

    formData.append(
        "file",
        fileInput.files[0]
    );

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict-video",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        result.innerText =
            data.prediction;

    }

    catch (error) {

        console.log(error);

        result.innerText =
            "Error connecting to backend";
    }
}