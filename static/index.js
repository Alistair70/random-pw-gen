document.addEventListener('DOMContentLoaded', function() {
    const lengthSlider = document.getElementById('length');
    const lengthValue = document.getElementById('lengthValue');
    const includeSymbols = document.getElementById('includeSymbols');
    const includeNumbers = document.getElementById('includeNumbers');
    const includeUppercase = document.getElementById('includeUppercase');
    const generateButton = document.getElementById('generateButton');
    const passwordDisplay = document.getElementById('password');

    lengthSlider.addEventListener('input', updateLengthValue);

    function updateLengthValue() {
        lengthValue.textContent = lengthSlider.value;
    }

    generateButton.addEventListener('click', generatePassword);

    function generatePassword() {
        const length = lengthSlider.value;
        const includeSymbolsValue = includeSymbols.checked;
        const includeNumbersValue = includeNumbers.checked;
        const includeUppercaseValue = includeUppercase.checked;

        fetch('/gen_password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ length: length, includeSymbolsValue: includeSymbolsValue, 
                includeNumbersValue:includeNumbersValue, includeUppercaseValue:includeUppercaseValue })
        })
        .then(response => response.json())
        .then(data => 
        {
            passwordDisplay.textContent = data.password;
            passwordDisplay.style.color = "black";

        })

        
    }
});
