async function detectVoice() {

    const result = document.getElementById("result");

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict"
        );

        const data = await response.json();

        result.innerText =
            "Prediction: " + data.prediction;

    }

    catch(error) {

        result.innerText =
            "Backend not running!";

    }

}