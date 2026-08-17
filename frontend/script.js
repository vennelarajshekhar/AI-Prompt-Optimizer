async function generatePrompt(){

    const prompt = document.getElementById("prompt").value;

    const response = await fetch("http://127.0.0.1:8000/generate-prompt",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            prompt:prompt
        })

    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
    data.optimized_prompt;

}