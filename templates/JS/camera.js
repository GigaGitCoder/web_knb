
        function handleButtonClick() {
            // Отключаем кнопку, чтобы предотвратить повторные нажатия
            document.getElementById("readyButton").disabled = true;
    
            // Задержка в 3 секунды перед вызовом функции
            setTimeout(generateComputerChoice, 3000);
        }
    
        function generateComputerChoice() {
            // Ваша логика для генерации выбора компьютера
            console.log("Компьютер сделал выбор!");
            // Включаем кнопку обратно
            document.getElementById("readyButton").disabled = false;
        }